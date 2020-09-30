# Django-Forms

Project - Pizza Online bestellen

## 1 - Getting Started with Forms

### 1 - Starting a new project

* `pip3 install django`
* `django-admin startproject PizzaOnline`

### 2 - Making forms from scratch

* `django-admin startapp Pizza`
* Home-Page und Order-Page - in `url.py` die Pfade vergeben
* `from Pizza import views`
* in `urlpatterns` infügen:
  * `path("",views.home, name="home"),`
  * `path("order", views.order, name="order"),`
* in `settings.py` `INSTALLED_APPS` einfügen
  * `Pizza,` damit es im Project bekannt wird
* in `views.py` Views erstellen:

```python
def home(request):
    return render(request, "Pizza/home.html")
def order(request):
    return render(request, "Pizza/order.html")
```

* in *Pizza/templates*
  * *home.html* erstellen

  ```html
  <h1>Nandia's Garden</h1>
  <a href="{% url 'order' %}">Order a Pizaa</a>
  ```

  * *order.html* erstellen
  
  ```html
  <h1>Order a Pizaa</h1>
  ```

### 3 - Form fields + 4 - Submitting forms

* zuerst normale HTML-Form erstellen:

```html
<h1>Order a Pizza</h1>
<form action="{% url 'order' %}" method="POST"> <!-- action wohin (an Welche URL es gesendet werden soll, default ist die aktuelle URL), POST ist wenn State geändert wird. -->
    {% csrf_token %} <!-- ist Django-Ding gegen Cross-Site Scripting -->
    <label for="topping1">Topping 1: </label> <!-- sollte mit input-id übereinstimmen-->
    <input id="topping1" type="text" name="topping1">
    <label for="topping2">Topping 2: </label> <!-- sollte mit input-id übereinstimmen-->
    <input id="topping2" type="text" name="topping2">
    <label for="size">Size: </label> <!-- sollte mit input-id übereinstimmen-->
    <select id="size" name="size">
        <option value="Small">Small</option>
        <option value="Medium">Medium</option>
        <option value="Big">Big</option>
    </select>

    <input type="submit" value="Order Pizza">
</form>
```

### 5 - Django form class

* 3 + 4 geht in Django einfacher:
  * in *forms.py*
  
  ```python
  from django import forms
  class PizzaForm(forms.Form):
      topping1 = forms.CharField(label="Topping 1", max_length=100)
      topping2 = forms.CharField(label="Topping 2", max_length=100)
      size = forms.ChoiceField(label="Size", choises=[("Small", "Small"), ("Medium", "Medium"), ("Big", "Big")])
  ```

  * in *views.py* ergänzen mit

  ```python
  from .forms import PizzaForm
  def order(request):
      form = PizzaForm()
      return render(request, "Pizza/order.html", {"pizzaform":form})
  ```
  
  * Html aus 3+4 anpassen
  
  ```html
  <h1>Order a Pizza</h1>
  <h2>{{ note }} </h2>
  
  <form action="{% url 'order' %}" method="POST"> <!-- action wohin (an Welche URL es gesendet werden soll, default ist die aktuelle URL), POST ist wenn State geändert wird. -->
    {% csrf_token %} <!-- ist Django-Ding gegen Cross-Site Scripting -->
    {% pizzaform %}
    <input type="submit" value="Order Pizza">
  </form>
    ```

### 6 - Using submitted data

* in *view.py* POST/GET-Reqest behandel

```python
    def home(request):
        return render(request, "Pizza/home.html")
    def order(request):
        if request.method == "POST":
            filled_form = PizzaForm(request.POST)
            if filled_form.is_valid():
                note = "Thanks for Ordering! Your %s %s and %s pizza is on its way!" %(filled_form_cleaned_data['size'],filled_form_cleaned_data['topping1'], filled_form_cleaned_data['topping1'],)
            new_form = PizzaForm()
            return render(request, "Pizza/order.html", {"pizzaform":new_form, "note":note})
        else:
            form = PizzaForm()
            return render(request, "Pizza/order.html", {"pizzaform":form})
```

## 2 - Working with Advanced Form Features

### 1 - Adding models

* Damit man die Eingaben seichern kannt muss man Models erstellen also in *models.py*

```python
from django.db import models

class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping1 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE) # on_delete=models.CASCADE - wenn Pizza gelöscht wird, wird auch Size in DB gelöscht

```

* damit diese Model auch in /admin angezeigt wird => in *admin.py* einfügen:

```python
from django.contrib import admin

from .models import Pizza, Size

admin.site.register(Pizza)
admin.site.register(Size)
```

* wenn man eine Änderung in Models macht => muss man Migrationen machen
  * `python3 manage.py migrate`
  * `python3 manage.py createsuperuser` - damit man Sachen mit admin über /admin eingeben kann
    * namen eingeben
    * password eingeben
    * dann eventuell über /admin *Small*, *Medium* *Big* eingeben

### 2 - Model forms

* Form aus Model erstellen d.h *from.py* aus 1.5 verändern

```python
from django import forms
from .models import Pizza
#class PizzaForm(forms.Form):
#    topping1 = forms.CharField(label="Topping 1", max_length=100)
#    topping2 = forms.CharField(label="Topping 2", max_length=100)
#    size = forms.ChoiceField(label="Size", choises=[("Small", "Small"), ("Medium", "Medium"), ("Big", "Big")])
class PizzaForm(forms.ModelForm):
    # Metadaten für die Form
    class Meta:
        model = Pizza
        fields = ['topping1', "topping2", "size"]
        label = {"topping1": "Topping 1", "topping2": "Topping 2" } # da sonst der Label-Test aus name oder id genommen wird
```

### 3 - Working with widgets

* in *forms.py*

```python
class PizzaForm(forms.Form):
    topping1-1 = forms.CharField(label="Topping 1", max_length=100, widget=forms.PasswordInput)
    topping1-2 = forms.CharField(label="Topping 1", max_length=100, widget=forms.Textarea)
    topping2 = forms.CharField

    toppings = forms.MultipleChoiseFiled([choises=('pep','Pepperoni'),('cheese', 'Cheese'),('olives','Olives')], widget=forms.CheckboxSelectMultiple)

    (label="Topping 2", max_length=100)
    size = forms.ChoiceField(label="Size", choises=[("Small", "Small"), ("Medium", "Medium"), ("Big", "Big")])
```

* also mit Widgets kann man die Standard-Funktion der Form verändern

### 4 - Advanced widgets

```python
class PizzaForm(forms.ModelForm):
    # Metadaten für die Form


    class Meta:
        model = Pizza
        fields = ['topping1', "topping2", "size"]
        label = {"topping1": "Topping 1", "topping2": "Topping 2" } # da sonst der Label-Test aus name oder id genommen wird
        widgets1 = {'topping1':forms.Textarea} # welches Widget zu welchem Feld angwendet wird
        #ODER
        #widgets2 = {'size': forms.CheckboxSelectMultiple}
```

```python
import .models import Pizza, Size

class PizzaForm(forms.ModelForm):
    # Metadaten für die Form

    size = forms.ModelChoiseField(query=Size.objects, empty_label=None, widget=forms.CheckboxSelectMultiple) # oder widget=forms.RadioSelect

    class Meta:
        model = Pizza
        fields = ['topping1', "topping2", "size"]
        label = {"topping1": "Topping 1", "topping2": "Topping 2" }

```

### 5 - Forms and files

* in *order.html*

```html
<form enctype="multiple/form-data" action="{% url 'order' %}" method="post"> <!-- User kann Dateien hochladen

</form>
```

* `pip install pillow` um mit Images zu arbeiten
* Server neu starten

```python
class PizzaForm(forms.ModelForm):

    image = forms.ImageField()

    # Metadaten für die Form
    class Meta:
        model = Pizza
        fields = ['topping1', "topping2", "size"]
        label = {"topping1": "Topping 1", "topping2": "Topping 2" } 
```

* in *views.py*

```python
def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, request.FILES)
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = "Thanks for Ordering! Your %s %s and %s pizza is on its way!" %(filled_form_cleaned_data['size'],filled_form_cleaned_data['topping1'], filled_form_cleaned_data['topping1'],)
        new_form = PizzaForm()
        return render(request, "Pizza/order.html", {"pizzaform":new_form, "note":note})
    else:
        form = PizzaForm()
        return render(request, "Pizza/order.html", {"pizzaform":form})

```

### 6 - Formsets: Multiple forms on a page

* mehrere gleiche Formen
* in *order.html*

```html
<h1>Order a Pizza</h1>

<h2>{{ note }} </h2>

<form action="{% url 'order' %}" method="POST"> <!-- action wohin (an Welche URL es gesendet werden soll, default ist die aktuelle URL), POST ist wenn State geändert wird. -->
    {% csrf_token %} <!-- ist Django-Ding gegen Cross-Site Scripting -->
    {{ pizzaform }}
    <input type="submit" value="Order Pizza">
</form>

<br>

Want more than one pizza?

<form action="{% url 'pizzas' %}" method="GET"
    {{ multiple_form }}
    <input type="submit" value="Get Pizzas">
</form>
```

* in *urls.py* ergänzen
  * `path('pizzas', views.pizzas, name="pizzas"),`
* in *form.py* die Form dafür erstellen

```python
class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
```

* in *views.py* diese Klasse jetzt auch zum Rendern bringen (also *views.py ergänzen)

```python
from .forms import PizzaForm, MultiplePizzaForm

def order(request):
    if request.method == "POST":
        multiple_form = MultipleForm()(request.POST, request.FILES)
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = "Thanks for Ordering! Your %s %s and %s pizza is on its way!" %(filled_form_cleaned_data['size'],filled_form_cleaned_data['topping1'], filled_form_cleaned_data['topping1'],)
        new_form = PizzaForm()
        return render(request, "Pizza/order.html", {"pizzaform":new_form, "note":note, 'multiple_form': multiple_form})
    else:
        form = PizzaForm()
        return render(request, "Pizza/order.html", {"pizzaform":form, 'multiple_form': multiple_form})
```

### 7 - Formset views + 8 - Controlling the number of formsets

* in *views.py* noch die Funktion zum Rander von *pizzas* erstellen

```python
from django.forms import formset_factory

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number'] 
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data["topping1"])
            note = "Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"
        return render(request, "pizza/pizzas.html", {"note": note, "formset":formset})
    else:
        return render(request, "pizza/pizzas.html", { "formset":formset})
```

* in *templates/Pizza* noch *pizzas.html* erstellen

```html
<h1>Order Pizzas</h1>
<h2>{{ note }}</h2>

<form action="{% url 'pizzas' %}" method="POST">
    {% csrf_token %}
    {{ formset.management_form }}

    {% for form in formset %}
        {{ form }}
        <br>
    {% endfor %}
    <input type="submit" value="Order Pizzas">
</form>
```

* als Bsp bei Bestellung von einer Pizza die Sachen speichern: (in *view.py* *def order(request)* ergänzen)

```python
def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.saved() # man kann über admin-Seite schauen, was gespeichert wurde
            note = "Thanks for Ordering! Your %s %s and %s pizza is on its way!" %(filled_form_cleaned_data['size'],filled_form_cleaned_data['topping1'], filled_form_cleaned_data['topping1'],)
        new_form = PizzaForm()
        return render(request, "Pizza/order.html", {"pizzaform":new_form, "note":note})
    else:
        form = PizzaForm()
        return render(request, "Pizza/order.html", {"pizzaform":form})
```

### 9 - Editing objects

* Neue Seite zum Bearbeiten der Bestellungen erstellen (also *urls.py* ergänzen)
* `path("order/<int.pk>", views.edit_order, name="edit_order")`
* die *views.py* ergänzen

```python
from .models import Pizza

def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.saved() # man kann über admin-Seite schauen, was gespeichert wurde
            created_pizza_pk = created_pizza.id
            note = "Thanks for Ordering! Your %s %s and %s pizza is on its way!" %(filled_form_cleaned_data['size'],filled_form_cleaned_data['topping1'], filled_form_cleaned_data['topping1'],)
            new_form = PizzaForm()
        return render(request, "Pizza/order.html", {"created_pizza_pk":created_pizza_pk, "pizzaform":new_form, "note":note})
    else:
        form = PizzaForm()
        return render(request, "Pizza/order.html", {"pizzaform":form})

def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance = pizza)
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form

    return render(request, "Pizza/edit_order.html", {"pizzaform":form, "pizza":pizza})
```

### 10 - Input confirmation

* *order.html* bearbeiten

```html
<h1>Order a Pizza</h1>

{% if created_pizza_pk %}
<a href="{% url 'edit_order' created_pizza_pk %}">Edit your order</a>

<h2>{{ note }} </h2>

<form action="{% url 'order' %}" method="POST"> <!-- action wohin (an Welche URL es gesendet werden soll, default ist die aktuelle URL), POST ist wenn State geändert wird. -->
    {% csrf_token %} <!-- ist Django-Ding gegen Cross-Site Scripting -->
    {% pizzaform %}
    <input type="submit" value="Order Pizza">
</form>

<br>

Want more than one pizza?

<form action="{% url 'pizzas' %}" method="GET"
    {{ multiple_form }}
    <input type="submit" value="Get Pizzas">
</form>
```

* */templates/Pizza/edit_order.html* erstellen

```html
<h1>Edit a Pizza</h1>

<h2> {{ note }} </h2>

<form action="{% url 'edit-order' pizza.id %}" method="POST"> <!-- action wohin (an Welche URL es gesendet werden soll, default ist die aktuelle URL), POST ist wenn State geändert wird. -->
    {% csrf_token %} <!-- ist Django-Ding gegen Cross-Site Scripting -->
    {% pizzaform %}
    <input type="submit" value="Edit Pizza">
</form>
```

* in *view.py* *def edit_order(..)* bearbeiten

```python
def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance = pizza)
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = "Order has been updated"
    return render(request, "Pizza/edit_order.html", {"note":note, "pizzaform":form, "pizza":pizza})
```

## 3 - Customizing and Styling Form Apearance

### 1 - Local validation and errors

* alles was auf dem Client (Browser) passiert
* das mann man über *forms.py* eisntellen
  * `email = forms.EmailField()`
  * `url = forms.URLField()`
* damit die Browser-Validation ausgeschaltet wird =>
  * `<form ... novalidate>...</form>`

### 2 - Server-based errors

* in diesen rander-Funktionen die Validation programmieren
* Bsp: *views.py* -> *def order(request):

```python
def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.saved() # man kann über admin-Seite schauen, was gespeichert wurde
            created_pizza_pk = created_pizza.id
            note = "Thanks for Ordering! Your %s %s and %s pizza is on its way!" %(filled_form_cleaned_data['size'],filled_form_cleaned_data['topping1'], filled_form_cleaned_data['topping1'],)
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None

            note = "Pizza order hat failed, try agian"

        return render(request, "Pizza/order.html", {"created_pizza_pk":created_pizza_pk, "pizzaform":filled_form, "note":note})
    else:
        form = PizzaForm()
        return render(request, "Pizza/order.html", {"pizzaform":form})
```

### 3 - Form rendering

* anders als Standard-Form ausgabe:
    1. in *order.html*

    ```html
    <h1>Order a Pizza</h1>

    {% if created_pizza_pk %}
    <a href="{% url 'edit_order' created_pizza_pk %}">Edit your order</a>

    <h2>{{ note }} </h2>

    <form action="{% url 'order' %}" method="POST"> <!-- action wohin (an Welche URL es gesendet werden soll, default ist die aktuelle URL), POST ist wenn State geändert wird. -->
        {% csrf_token %} <!-- ist Django-Ding gegen Cross-Site Scripting -->
        {% pizzaform.as_p %}
        <input type="submit" value="Order Pizza">
    </form>

    <br>

    Want more than one pizza?

    <form action="{% url 'pizzas' %}" method="GET"
        {{ multiple_form }}
        <input type="submit" value="Get Pizzas">
    </form>
    ```  

  * `{% pizzaform.as_p %}` - `.as_p` - als Paragaph darstellen

  ```html
  <table>
  {% pizzaform.as_table %}
  </table>
    ```

  ```html
  <ul> <ol>
  {% pizzaform.as_ul %}
  </ul> </ol>
  ```

### 4 - Customizing forms

* in *order.html*
  * der Trick ist, dass man die einezelnen Elemente der Form einzeln eibinden, statt als ganzes Element
  
  ```html
  <h1>Order a Pizza</h1>

  {% if created_pizza_pk %}
  <a href="{% url 'edit_order' created_pizza_pk %}">Edit your order</a>

  <h2>{{ note }} </h2>

  <form action="{% url 'order' %}" method="POST"> <!-- action wohin (an Welche URL es gesendet werden soll, default ist die aktuelle URL), POST ist wenn State geändert wird. -->
    {% csrf_token %} <!-- ist Django-Ding gegen Cross-Site Scripting -->
    {{ pizzaform.topping1.errors }}
    {{ pizzaform.topping1.label_tag }}
    {{ pizzaform.topping1 }}
    {{ pizzaform.topping1.errors }} <!-- zeigt Validation-Errors an -->

    {{ pizzaform.topping2.errors }}
    {{ pizzaform.topping2.label_tag }}
    {{ pizzaform.topping2 }}

    <label for "{{ pizzaform.size.id_label }}">Size:</label>
    {{ pizzaform.size.errors }}
    {{ pizzaform.topping1 }}
      <input type="submit" value="Order Pizza">
  </form>

  <br>

  Want more than one pizza?

  <form action="{% url 'pizzas' %}" method="GET"
      {{ multiple_form }}
      <input type="submit" value="Get Pizzas">
  </form>
    ```

  * Also man kann nur Einzelne Elemente des ganezen Klassen-Objekt in *.html* holen  

### 5 - Spicing up forms with CSS

* Hier wird *bootstrap* benutzt
* Vorgehen:
    1. `pip isntall django-widget-tweaks`
    2. von Bootstrap *Get Startet* -> Copy
    3. in *settings.py* App hinzufügen:
        `'widget_tweaks',`
    4. in *order.html* Bootstrap-Copy reinkopieren.
    5. den eigenen Code von *order.html* in `<body>` von Bootstrap reinkopieren, eventuell etwas weiter einpassen
    6. Widget-Tweaks laden
        1. {% load widget_tweaks %} am Anfang von `<body>`
    7. `{{ pizzaform }}` in for-Loop holen d.h ersetzen durch:
        1.

        ```html
        <div class="container"> <!-- noch bevor Form -->

            <div class="form-group">
                {% for field in pizzaform %}
                    {{ filed.errors }}
                    {{ field.label_error }} 
                    {% render_field field class="form-control" %} <!--hier wird widget_tweaks gerufen -->
                {% endfor %}
            </div>
        </div>
        ```

### 6 - Homepage styling

* */template/BASE.html* erstellen
* Da in *order.html schon Bootstrap eingefügt ist den Inhalt von oben bis `<body>` + ab `</body>` bzw. relavenem Inahlt für alle Seiten erstemal hierrein kopieren, dann:

```html
<nav class="navbar navbar-expand-lg navbar-dark">

</nav> <!-- für Navigation -->

{% block "body" %}
{% endblock %}

```

* in *order.html* `{% extends "pizza/BASE.html"}`

### 7 - Form styling

* eigentlich überall `{% extends "pizza/BASE.html"}` und `{% block "body" %}`
* dann noch `STATIC_ROOT` einrichten + `python manage.py collectstatic`
