### 1 -Setting up Django Project
#### 1 - what is django
* www.djangoproject.com
* Python-Framework
* Framework - Sammlung von Tools, um Webseiten zu bauen
* Django-Tools: 
    + ORM (Object-relational Mapping) - um DB-Anfragen zu machen, 
    + URL-routing = welcher Logik soll gefolt werden, abhängig von der URL-eingabe, 
    + HTML-Templating = HTML-Präsentation, 
    + Form-Handling, 
    + Testing-Tools
* !!! Django:
    * Tool, was in Python geschrieben ist <- keine Sprache, 
    * kein WebServer (aber enhält eingebaueten WebServer)
#### 2 - install python and django
* von python.org -> herunterladen und installieren
ODER
* mit pip3: `pip3 install django==1.11.7`
    * installiert auch `pytz`-Library für Timezone Support 

#### 3 - create a Django project
* `django-admin startproject ProjectName` (wisdompets) - Wird Ordner für Django-Projekt angelegt mit folgenden Dateien darin: (djang-admin.py startproject WisdomPets)
    * `manane.py` - führt Befehle des Projekt aus
    * *ProjectName/__init__.py* - sagt Python, dass dieser Ordner enthält Python-Dateien
    * *ProjectName/wsgi.py* - Provides a hook for Web Server z.B für Apache oder Nginx
    * *ProjectName/settings.py* - konfiguriert Django
    * *ProjectName/urls.py* - routet Requests abhängig von URL
* `python3 manage.py runserver` - Server Starten und da Django ausführen

#### 4 - create a Django app
* Django-App - Ordner mit Python Dateien, APP = Komponente
* `python3 manage.py startapp appName` (adoptions)- es wird ordner mit appName erstellt (pyhon3 manage.py startapp Adoptions)
* in *ProjectName/settings.py* zu INSTALLED_APPS gehen und appName, am Ende der Liste eintragen
* AppName-Ordner hat:
    + *apps.py* - Konfiguration und Initialisierung - kontroliert Settings der App 
    + *models.py* - Data layer -> DB-Schema  und Anfragen erstellen und DB-Anfragen machen
    + *admin.py* - Administratives Interface
    + *urls.py* - URL routing für die APP
    + *views.py* - Control layer bzw. Logik und Controll-Flow um mit den Requests umzugehen und HTML-Responses erstellen
    + *tests.py* - App testen
    + *migrations/* - enhält Migrations-Dateie, wenn man DB-Schema ändert

### 2 - Working with Django models and admin
#### 1 - models, routing, view and templates
* Django benutze eigetlich Models <-> View <-> Controller - Architektur nennt es aber etwas anders:
    1. URL-Patterns
    2. Veiws 
    3. Templates
    4. Models
* Architekture des Framework verstehen.
    + Django benutut Model View Controler aus 4 Teielen:
        1. URL Patterns: *projectOrdner/urls.py* - Wenn Django-App bekommt Web-Requests => werden URL Patterns benutzt => Controll-Flow und sendet ws an Views
        2. Views:  *projectOrdner/views.py* - Logik bzw. Kontrollfluss der App <- sind Funktionen bekommen als Param HTTP-Req und erzeugen HTTP-Response. Kann Models benutzen um DB-Anfragen zu machen. 
        3. Templates: *projectOrdner/adoptions/templates/* - HTML mit Template-Syntax
        4. Models: *projectOrdner/adoptions/models.py* - Um DB-Angragen zu machen kann View die Models dafür benutzen. Django-Model ist Klass mit Attributen, das DB-Schema definiert => ~ Build-In Methoden um DB-Anfragen zu machen
    + Bsp: Vorgehensweise:
        1. http://yoursite.com/ -> wird in URL schauen, welche View für / er benutzen soll -> View wird dann eventuell DB-Anfragen mittels Models machen -> DB-Antwort werden in home/index.html eingesetzt
* Verlauf:
    * URL-Pattern = urls.py (Controller) -> Views + Models = views.py + models.py (Model + View) -> Templates = /templates (View)

#### 2 - Django models
* Data Layer der App
    * definiet DB-Struktur
    * erlaubt DB-Anfragen
* models ist Klasse die von django.db.models.model erbt
    * ~Excel-Tabelle
* Model-Klasse ersteleln:
    1. django.db.model imortieren:
    2. eigene Klasse erstellen, die von models.model erbt + eigene Attribute erstellen:
* Bsp:
```python
from django.db import models
class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    #<- es gibt noch andere Datentypen in models + ForeignKey und ManytoMany-Attrib:
    #Datenfelder können auch andere/mehrere Param. bekommen:
    models.CharField(max_length=10, null=True, blank=True) #blank=True = Feld kann leer sein
    #weitere Attr:
    #max_length
    #null = Feld kann als null gespeichert werden
    #blank = zu True => Feld ist nicht erforderlich
    #choices = Wert begrenzen, die in diesem Feld gespeichert werden können
    # <- siehe https.//docs.djangoproject.com
```
+ mögiche Felder
* `models.IntegerField()`
* `models.DecimalField()`
* `models.CharField()` - braucht `max_length`
* `models.TextField()`
* `models.EmailField()`
* `models.URLField()`
* `models.BooleanField()`
* `models.DateTimeField()`
* `models.ForeignKey()` - id von andere Tabele
* `models.ManyToMany()`
* Attribte:
    * `max_length=10` 
    * `null=True` - 
    * `blank=True` - Field ist nicht zwingend
    * `default`
    * `choises`
    * <- kann man Doku chechen => Models -> Field types

#### 3 - Django fields

#### 4 - implements models and fields
* Bsp:
```python
class Pet(models.Model):
    SEX_CHOISES = [("M", "Male"), ("F", "Female")]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    bredd = models.CharField(max_length=30, blank=True)
    desc = models.TexField()
    sex = models.CharField(choises = SEX_CHOISES, max_lenght=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null = True)
    vaccinations = models.ManyToManyField("Vaccine", blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
```

#### 5 - Django migrations
* Models = Struktur der DB
* Migrations = Skripte um DB-Struktur zu verändern:
* Initial Migration = DB-Tabellen aus dem Model zu erstellen
* Wann Migrations nötig:
    1. DB-Scheme erstellen
    2. neue Felder in DB-Tabellen erstellen
    3. Felder löschen
    4. Felder ändern
* Migrations-Ablauf -> Generiert Migrations-Files und speicher sie in migration-Order. Migrations-Command schreibt alles in DB
* Migration-Command-Syntax: `migrate APPNAME NUMMER`
    * `NUMMER` ist die Reihenfolge der Änderung von Models
* Migratinsbefehle:
    * `python manage.py makemigrations` = erzeugt Migrationsdateien = schauet Model-Felder an und aktuellen Stand der DB
    * `python manage.py migrate`
    * `python manage.py showmigrations` - [] = Migration wurde noch nicht ausgeführt.
* Migration für Bestimmte APP und Nummer laufen:
    * `migrate appName Nummer`
* Wenn Migration-Datei erstellt, aber nicht ausgeführt => unapplyed Migration

* Bsp - Vorgehensweise:
    1. in Terminal zum Projekt navigieren -> `python3 manage.py makemigrations` eingeben. -> wird ind `../migrations/` Datei `0001_initial.py` erstellt -> `python3 manage.py showmigrations` = zeigt alle Möglichen Migrationen an in Gruppen; [ ] = wurde noch nicht angewendet -> `python3 manage.py migrate` = alle Migrationen anwenden

#### 6 - Import CSV data
* Skript ist in Übungs-Files => management-Ordner + .csv-Datei
    * eigentlich nur eine Python-Datei: *load_pet_data.py* 
* `python3 manage.py load_pet_data.py`

#### 7 - work with the Django admin
* Admin-Interface für Project erstellen
    1. AppName/admin.py öffenen  (erste Zeile importiert admin-Modul von django.contrib)
    2. Eigene Imports machen
    ```python
    form .models imports Pet

    @admin.register(Pet)
    class PetAdmin(admin.ModelAdmin):
        # pass
        list_display = [ "name", "species", "breed", "age", "sex" ]
    ```
    * in models.py
    ```python
    class Vaccine(models.Model):
        # code ...

        def __str__(self):
            return self.name
    ```

        + < - siehe admin.py
        + ...
    3. - SuperUser erstellen um in Admin-Interface anzumelden
        * `python3 manage.py createsuperuser`:
            * `name: project-root`
            * `passw: djangolernen`
        * => localhost:8000/admin

#### 8 - Query data with Django ORM
* DB-Querys mit in Django implementierten Funktionen:
* im Kurs in Shell:
    1. `python3 manage.py shell` = wird python-Shell aufgemacht
    2. `from Adoptions.models import Pet`
* Django-Models haben ein Attribute object mit Funktionen für DB-Querys
     `Pet.object.all()` - returnt alle Instantenzen von Pet (=> ein Array)
    3. `pets = Pet.objects.all()`
    4. `pet = pets[0]`
    5. `pet.name; pet.description`
    * Django macht auch ein ID für jedes Model, startet bei 1 (eigentlich Primar Key):
    1. `pet.id`
* Einzelne Queries machen
    * `pet = Pet.objects.get(id=1)` - falls falsche ID => Exception
        * !! get() kann nur ein Object zurückgeben (also kein Array). Also falls:
    * `Pet.objects.get(age=1)` - werden mehrere Pets returnt => MultipleObjectException
    * `get()` ist eigentlich für id-es gut
        *  man kann im *views.py* diese Exceptions checken
    * `pet.vaccinations.all()`
    * => diese Exception müssen im Code dann beachtet werden z.B try-catch

### 3 - Building URL handlers and view
#### 1 - Understand URL patterns
* URL-Patterns abfertigen Requests zu Views
* benutzen Reguläsre Ausdrücke um URL zu interpretieren:
* `ducky = String` der ducky enthält
* `\d` - eine Zahl
* `\d+` - merhrere Zahlen
* `^admin/` z.B `admin/xxx/xxx` ist Match <- admin muss am Anfang stehen
* `suffix$` - suffix muss am Ende stehen
* `^$` - leeres String = beginnt mit nichts + endet mit nichts
* **pythex.org** = Reguläre Audrucke in Python:
* Bsp für URLS:
    1. *url.py* hat urlpatterns-Var, die Liste Aufrufe für `url()` enhält. 
        * `url()` - hat drei Params
            1. regEx für URL das `/` am Ende ist egal
            2. view.xxx - welche View-Funktion wird aufgerufen.
            3. name-Param - für Templates 
        * Bsp:
            * `url(r'^$', views.home, name='index')` - - r=RawString => brauchen keine \\ für Escape-Seq z.B wenn man Enter sagen will.
```python
urlpatterns=[
    #url() hat drei Param:
    #1 - Reguläre Audrück um Requests zu spezifizieren -> r'^$' = leerer String (r = raw-String(d.h benutzt kein / als Escape-Charakter))
    #2 - Welche View soll aufgerufen werden <- heißt welche Funktion in View.
    #3 - für Templates
    url(r'^$', views.home, name="index")

    #<- urlpatterns hat mehrere url() <- es wird geschaut, welche Reguläre Expression zutreffend ist und entsprechende View aufgerufen
]
```
* wenn man falsche URL eingibt => wird Debug-URL mit Error-Hinweise kommen <- Falls man in Config Debug auf false macht => kommt einfach 404-Seite

#### 2 - Implements URL patterns
* urls.py
```python
import adoptions import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^adoptions/(\d+)/', views.pet_detail, name="per_detail"), # (\+d) damit man es parsen kann und an views weitergeben kann
]
```
* views.py
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>Home View</p>)

def pet_details(request, id):
    return HttpResponse('<p>Per_Detail View with id {} </p>'.format(id))
```

#### 3 - Implements Django views
* im Beispiel wurden template-Files und Views-Namen gleich genannt <- ist aber nicht erforderlich
* templates in *AppOrnder/templates* erstellten <- eventuell zuerst Ordner templates erstellen
* views.py
```python
from django.http import HttpResponse

from .models import Pet # jetzt kann man Queries machen

form django.http import Http404
def home(request):
    pets = Pets.objects.all()
    return render(request, 'thome.html' {'pets': pets}) # request, tempalteaName.html, Dictionary

def pet_details(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')

    return render(requset, 'pet_deatil.html', {'pet': pet})
```
* templates home.thml
```html
Home 
```
* tempate per_detail.html
```html
Pet detail
```

### 4 - Building Django Templates
#### 1 - Django Templates
* sind html-Dateien mit spezieller Syntax
* Syntax:
    1. `{{ variable }}`
    2. `{% tag %}` z.B für Ifs, Whiles. for-s
    3. `{{ variable|filter }}` - für Filters 
* Wenn `view.py` render aufruft => render füllt Template mit Parametern und Template erzeugt html-Datei
#Template Syntax:
```html
1. {{ variable }}
<h3> {{ pet.name }} </h3>


2. {% tag %}  #für Loops und If-s
{% for pet in pets %}
    <li>{{ pet.name }} </li>
{% endfor %}  #ist notwendig um das Ende des Loops zu markieren

{% url 'index' %} => Ausgabe. / (index aus url(, , name="index"))
{% url 'pet_detail' pet.id %} => Ausgabe /adoptions/1/ (pfad aus url(, , name="pet_detail"))


3. {{ variable|filter }} #Temlate-Filter = nimmt String an und return String zurück wie Pipe in Bash <- um Format zu veränder z.B bei Datum
<h3> {{ pet.name|capfirst }} </h3> #=>pet.name benutzt eingebauten Filter capfirst = erster Bushstabe 
wird dann immer groß
```
* großes Bsp alle 3 zusammengefasst
```html
<ul>
    {% for pet in pets %}
    <li>
        <a href="{% url 'pet_detail' pet.id $ %}">
            {{ pet.name|capfirst }}
        </a>
    </li>
    {% endfor %}
</ul>
```

* manche Template-Tags haben keinen end-Tag => rendern nur String
    * sollte in `url.py` stehen
    * `{% url "index" %}` - hier wird `name="index"` benutzt. <- URL-Tag mit Argument home wird Pfad zu home-View generieren => Output: /
    * `{% url "pet_detail" pet.id %}` - Output */adoption/pet.id/*

* Base-Template von Django (*base.html*):
```html
<!doctype html>
<html>
    <head>
        <!-- meta tags and so on -->
    </head>
    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>

# -> dann kann man in weiteren Templates Base-Template benutzen:
{% extends "base.html" %} #muss erste Zeile im Template sein
{% block content %}
    <h3>Animals available for adoption</h3>
    <!--more content -->
{% endblock content %}
```
* <- jedesmal wenn man `{%block blockName% benutzt}` => wird der Block blockName von dem Eltern überschrieben

#### 2 - Implement Django Templates
* templates home.thml
```html
Home 
```
* tempate per_detail.html
```html
Pet detail
```
#### 3 - Structure Templates
* *base.html* erstellen und andere Templates von diesem Erben lassen

#### 4 - Integrate CSS and JavaScript
* statische Dateien = CSS und JS zuerst über *ProjectName/ProjectName/settings.py* einstellen:
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")  #BASE_DIR ist oben in settings.py definiert (meist ist ProjectName/ProjectName); join() ist die python-Funktion um Pfade zu bauen
]
```
* dann in *base.html* als erste Zeile einfügen:
`{% load static %}`
* jetzt kann man in hrefs, links usw. die Dateien die in static-Ordner den HTML-Tags vergeben mit:
`"{% static "style.css" %}"`

### Weitere Tipps:
* Tipps zu Lernen:
* Pythoen, SQL, Rest
* Django-Doku + Django-Tutorial checken:
* Tipps welche Django-Settings sollte man ändern:
* DEBUG:
    * `DATABASES: <- PostgreSQL, MySQL`
