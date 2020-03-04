### 1 - Advanced Class-Based Views
#### 1 - The course overview
* basiet auf dem offizielen Django-Tutorial
#### 2 - Extending class-based views
* in models.py
```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.questin_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choise_text
```
* in view.py
```python
from django.views import generic # Klasse generic von django.views importieren 

from .models import Question

'''
# Funktional-Based View
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
'''

#Class-Based-View
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5] # wenigsten ersten 5

'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
# oder 
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
'''
class DetailView(generic.DetailView):
    model = Question # welches Model man benutzt 
    template_name = "polls/detail.html" //welche URL das ist

class DeleteView(generic.DeleteView):
    model = Question
    success_url = "/polls/"
```
+ 1 - Class-Based-Views vs. 2 - Funtional-Based-Views
    1. Class
        * weniger Setup
        * mehr "magic" Abstraktion -> Logik schwerer zu verstehen
        * eingebautes Error-Handling
        * mehr Modular
        * Stabile generische API

    2. Funtional - 
        * mehr Setup
        * weniger Abstraktion
        + braucht Error-Checking -> try-execpt
        * weniger Modular
* in urls.py
```python
from . import views

app_name = "polls"

# 
urlpatterns = [
    url(r'^$', views.IndexView.as_view()), # aus view die Klasse IndexView holen und die Funktion as_view() aufrufen
    url(r'^(?P<pk>[0-9]+)/$', views.IndexView.as_view()),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.IndexView.as_view() name="delete"),
]
```
* Fazit:
    1. Class-based-Views sind aus mehreren *views* und *Mixins* gebildet
#### 3 - Using mixins
* Wiese mixins benutzen:
    1. modulare Funktioanalität -> Reusability, 
        * Funktionalität wird in Mixin ausgelagert und der Mixin bei Bedarf wieder benutzt + Wiederholung des Codes vermeiden
* MRO - Method Resolution Order 
    * Bsp für MRO -> mro_example.py
    ```python
    class Parent1:
        def speak(self):
            print("I am Parent1")
        def talk(self):
            print("Parent1 talking)

    class Parent2:
        def speak(self):
            print("I am Parent2)
            return super(Parent2, self).speak() # so wird auch die Funktion speak() von Parent1 aufgerufen

    class Child(Parent2, Parent1):
        pass
    
    child = Child()
    
    child.speak() # hier wird Parent2.speak aufgerufen, da Parent2 als erstes inherited wird <- das ist MRO -> Es schauet zuerst ob Parent2 die aufgerufen Funktion hat, wenn nicht geht es zu Parent1 
    child.talk()
* in mixins.py
    * diese Klasse aus mixins.py wird in view.py bei IndexView inherited, deswegen hier `return super()`
```python
from django.contrib.auth.views import redirect_to_login

class RequireLoginMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect_to_login(request.get_full_path())
        return super(RequireLoginMixin, self).dispatch(request, *args, **kwargs)
```

#### 4 - Creating custom CBVs
* *generic.View* ist die Basis Generic-View, hat wenige Methoden, ist einfacht mit HTTP-Verbs (GET, POST, PUT, DELETE) zu erweitern. 
* in view.py noch die Klasse *VoteView*, *ResultsView erstellen
```python
class VoteView(generic.View):
    def get_queryset(self, choice_id):
        return Choise.objects.get(pk=choise_id)
    
    def post(self, request, pk):
        question_id = pk
        choise_id = request.POST.get("choise", None)
        try:
            query = self.get_queryset(choise_id)
        except (KeyError, Choise.DoesNotExist):
            return redirect("polls:detail", pk=question_id)
        else:
            queryset.votes += 1
            queryset.save()
            return redirect("polls:results", pk=question_id)
'''
# Django-Tutorial Code Funktional-Based-View
# man kann nich sehen ob es GET, POST usw. war man muss mit if request.method == "POST" erweitern

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''       
from django.views.generic.base import TemplateResponseMixin
class ResultView(TemplateResponseMixin, genereic.View):
    template_name = "polls/results.html"

    def get_queryset(self, question_id):
        return Question.objects:get(pk=question_id)
    
    def get(self, request_id):
        queryset = self.get_queryset(pk)
        context = {"question": queryset}
        return self.render_to_response(context)
```
#### 5 - Building switchboard views
* in suplimentary/dispatch.py
```python
class View:
    http_method_names = [u'get', u'post', u"put", u"patch", u"delete", u"head", u"options", u"trace"]

    '''
        View.as_view() - (in urls.py) Klassed-Based-Views aufrufen. Es würde die dispatch() (unten) aufrufen und diese mit allen nötigen Parametrn füttern, die in URL erhalten sind 
    '''


    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
```
* view.py ergänzen:
```python
#Sinn der Klasse, je nachdem ob get oder post wird ResultView.as_view() oder VoteView.as_view() aufgerufen
class SwitchboardView(generic.View):
    def get(self, request, pk):
        view = ResultView.as_view()
        return view(request, pk)
    
    def post(self, request, pk):
        view = VoteView.as_view()
        return view(request, pk)
```
* noch urls.py ergänzen
```python
url(r'^(?P<pk>[0-9]+)/vote/$', views.SwitchboardView.as_view()),
url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
```
* SwitchBoardViews sinvoll, wenn man viele Klassen haben, in SwitchBoard ist dann "alles" in einzelnen Klassen ist nur eine HTTP-Methode (GET,POST)
* 
#### 6 - Getting help with class-based views
* Documentatin von Django für Class-based views
* ccbv.co.uk - classy-call based views
* django-braces auf github -> hat Mixens für Django-Class-Based-Views

### 2 - Building a REST API
#### 1 - Using Django REST framework to scaffold
* 
#### 2 - CBVs in Django REST framework
#### 3 - Authentication with DRF

### 3 - GraphQL: An Alternative API
#### 1 - Intoduction to GraphQL
#### 2 - Building a basic schema
#### 3 - Building custom objects
#### 4 - Working with mutations

### 4 - Optimizing your Environment
#### 1 - Pipenv: The new pip
#### 2 - Separating setting files
#### 3 - Custom Pipenv environment

### 5 - Tests, Tests, Tests
#### 1 - Why testing matters
#### 2 - How Django handles testing
#### 3 - Testing models
#### 4 - Testing views
#### 5 - Testing it all together

### 6 - Securing Django
#### 1 - Security in Django
#### 2 - Security the Django admin
#### 3 - Planning for failure