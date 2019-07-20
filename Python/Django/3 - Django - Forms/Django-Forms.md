Project - Pizza Online bestellen
### 1 - Getting Started with Forms
#### 1 - Starting a new project
* `pip3 install django`
* `django-admin startproject PizzaOnline`
#### 2 - Making forms from scratch
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
* 
#### 3 - Form fields + 4 - Submitting forms
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
#### 5 - Django form class
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
#### 6 - Using submitted data
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
            return render(request, "Pizza/order.html", {"pizzaform":new_form}, {"note":note})
        else:
            form = PizzaForm()
            return render(request, "Pizza/order.html", {"pizzaform":form})
```

### 2 - Working with Advanced Form Features
#### 1 - Adding models
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
#### 2 - Model forms
* Form aus Model erstellen d.h *from.py* aus 1.5 verändern
*
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

#### 3 - Working with widgets
#### 4 - Advanced widgets
#### 5 - Forms and files
#### 6 - Formsets: Multiple forms on a page
#### 7 - Formset views
#### 8 - Controlling the number of formsets
#### 9 - Editing objects
#### 10 - Input confirmation

### 3 - Customizing and Styling Form Apearance
#### 1 - Local validation and errors
#### 2 - Server-based errors
#### 3 - Form rendering
#### 4 - Customizing forms
#### 5 - Spicing up forms with CSS
#### 6 - Homepage styling
#### 7 - From styling