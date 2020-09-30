# Portfolio with Django

als Editor Atom

- `django-admin startproject portfolio`

## 2 Creating Django App

### 1 - Start a new project in Django

- `django-admin startproject portfolio`
- Root-Folder umbenenen => `portfolio` zu `portfolio-project`
- `python manage.py runserver`

### 2 - Creating a Django app in a project

- `django-admin startapp jobs` - man sollte für Apps Plural benutzen
- in settings.py `INSTALLED_APPS`-Array ergänzen

### 3 - Setting up URL in your Django project

```python urls.py
import jobs.views

urlpatterns = [
    # ...
    path('lala', jobs.views.lala, name="lala"),
]
```

```python view.py
from django.shortcuts import render

def lala(request):
    return render(request, 'lala.html', )
```

- jobs/templates
  - jobs/templates/jobs
    - jobs/templates/jobs/lala.html erstellen

## 3 - Django and Databases

### 1 - Creating the models in DjangoTemplates

- DB um Jobs zu speichern
- Model = Klasse, die in DB gepeichert wird:

  - in _/portfolio-project/models.py_ erstellen <- kann man mehrer Classen erstellen.

  ```py
  class Job(models.Model):
    image = models.ImageField(upload_to='images/') # Image; image-Attribute vom Typ models.ImageField(); upload_to = wo Images gespeichert werden sollen
    summary = models.CharField(max_length=200) # Summary für Descrition
  ```

- wenn man ImageField verwendet braucht Python Lib `Pillow`

### 2-Postgres setup for Django

- per Default steht in _setttings.py_ welche DB genutzt wird
- Postgres:
  1. installieren (auf Mac gibt es eine User-Freundliche postgres.app)
  2. `sudo su - postgres` - sich als user postgres anmelden
  3. `psql` - sich mit DB verbinden
  4. `\conninfo` - Verbindungsinfo anzeigen
  5. `\password postgres` - Passwort für User postgres vergeben/ändern
  6. als user postgres -> `creatdb dbname` = DB erstellen
  7. als user postgres -> `dropdb dbname` = DB löschen

### 3-Connecting your Django project to Postgres

- bei _settings.py_ noch Postgres einfügen:
- in DATABASE

```py
'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'portfoliodb', # Name der DB
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': 'localhost',
    'PORT': '5432',
}
```

- damit Django sich mit Postgres verbinden kann braucht er psycopg2-binary =>:
  - `pip3 install psycopg2-binary` oder `pip3 install psycopg2`

### 4-Make Django migrations and migrate

- Migrationen = Wege um DB für Django-Projekte zu setzen
  - `python3 manage.py makemigrations` - Ausführen, wenn man Änderungen im Model macht = Es wird Migration erstellt, wenn etwas geändert wurde = wird eine Datei in `/migrations/xxx_initial.py` mit Befehlen, was auf DB angewendet werden soll
  - `python3 manage.py migrate` - die Migrationen ausführen
- Migrationen = Models zu Tabellen in DB schreiben.
- Alle Apps ( = `INSTALLED_APPS`), die DB brauchen haben Models, die dann in DB geschrieben werden sollen.

### 5-Setting up an admin panel in Django

Um sich in localhost\admin anmelden zu können => zuerste admin-user erstellen

- Admin-APP ist in:
  1. INSTALLED_APP
  2. Url ist in `urls.py`
- `python3 manage.py createsuperuser`
- `admin -> django1234`
- man kann dann über localhost/admin an der DB arbeiten:
  1. auch User und Gruppen, da ja eigentlich auch Models der admin-APP
  2. damit die Admin-APP auch eigene Models verwalten kann:
     1. in `admin.py` einfügen:
        1. `from .models import Jobs` - `.` für gucke in diesem Verzeichnis
        2. `admin.site.register(Jobs)` - dieses Model bei Admin-App/Seite registrieren

### 6-Creating model objects via the admin panel in Django

- der Admin der APP (nicht des Projects) verwaltet die Models =>admin.py öffnen und
  - `form .models import Jobs` - Klasse Jobs aus models.py einbinden
  - `admin.site.register(Jobs)` - den Admin über die Jobs-Klasse wissen lassen

### 7-Pulling objects from the database in Django

- in _view.py_ Code schreiben, um Jobs anzuzeigen

```py
def homepage(request):
    # alle jobs aus DB holen
    jobs = Jobs.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
```

```html home.html
<h1>All Jobs</h1>

<!-- for-Loop für jobs-->
{% for job in jobs.all %} {{ job.summary }} {% endfor %}
```

## 4 - Designing your Django Project

### 1 - Bootstrap overview and installation

- Bootstrap-Example-Pages benutzen:
  - [https://getbootstrap.com/] -> Examples -> z.B Album auswählen -> View Page-source -> alles Auswählen und z.B in eigenenes home.html einfügen
- Bootstrap selbst einfügen:

  - [https://getbootstrap.com/] -> Get Started -> CSS-Link kopieren -> JS kopieren. -> so anpassen wie man es möchte.

- Bsp Components anzeigen und Source-Code kopieren und bei home.html kopieren und anpassen mit den Django-Templates

### 3 - Adding static images to your Django Projects

- in _/jobs_ Ordner _static_ erstellen (eventuell darin noch _images_ Ordner erstellen)
- Django sagen, wo statische Sachen liegen => in _setttings.py_ einstellen:
- `STATIC_URL = '/static'` - das ist URL für static
- `STATIC_ROOT = os.path.join(BASE_DIR, "static")` - wo static aber wirklic gespeichert werden soll
- noch in _urls.py_ sagen wo es die Static-Sachen finden kann:

```py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### 4 - Collectstatic in Django

1. `python3 manage.py collectstatic` - alle Statischen Dateien in `/PROJECTNAME/static` bringen bzw. zum gemeinsamen `/static` Order, denn man mit `STATIC_ROOT` eingestellt. Eventuell müssen alle `/static`-s Ordners in den gemeinsamen `/static` Ordner bringen. Also als Folge sollte globaler Ordner `/static` erstellt werden.
2. auf der HTML-Seite ganz oben eingeben:
   - `#{% load static %}`
   - und dann es so benutzen: `<img src="{% static 'Per_Foto.jpg' %}" alt="">`
     - Also muss dann so `{% static 'image/Per_Foto.jpg' %}` benutzen

### 5 - Bootstrap as a static asset in Django

- Bootstrap herunterladen und selber hosten => nicht auf Bootstrap-Host angewiesen
  - Bootstrap, jQuery, Popper.js herunterladen und in _/static_ ablegen
  - und als `{% static '../../name.css/js' %}` einfügen

### 6 - Finishing touches in Django design

```html
<div class="row">
  {% for job in jobs.all %}
  <div ...>
    <span>{{ job.summary }}</span>

    <img ... src="{{ job.image.url }}" />
    ...
    <span>{{ job.summary }}</span>
  </div>
  {% endfor %}
</div>
```

- In `settings.py` folgendes Einfügen für Images usw.:
  `MEDIA_URL = "/media/"` - URL media nennen
  `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')` bzw. `MEDIA_ROOT = BASE_DIR` - Link zu dieser URL ist BASE_DIR

```py
urlpatterns =[
    ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 5 - Object datails in Django

### 1 - Connecting URLs and template in Django

- zu _/admin_ gehen und Einträge (hier Jobs einfügen)
- in _models.py_ Funktion `__str__` für Model hinzufügen, damit in _/admin_ die Einträge etwas aussagekräftiger angezeigt werden:

```py
def __str__(self):
    return self.summary
```

- neuen Path einfügen in _/urls.py_:

```py
urlpatterns =[
    ...
    path('/jobs/<int:job_id>', jobs.views.detail, name="detail")  #/jobs/<int:job_id>` - wenn man *jobs/x* eingibt und *x* ist ein *int* => wird diese *int* in *job_id* gespeichert
```

- => für `/jobs` neue Funktion/URL in views.py `jobs/:id` erstellen. Da man hier `job_id` als `int` festgelegt hat => wird Djangos-Default **404** angezeigt => eigene **404** erstellen

```py view.py
def detail(request, job_id): # job_id ist mapping name für id von path()
    print(job_id)
    return render(request, 'jobs/home.html')
```

### 2 - Creating views in Django

- mit `jobs_id` den richtigen Job aus DB holen.
- `from django.shortcuts import get_object_or_404` - Funktion importieren; diese Funktion holt bestimmtes Object aus DB, wenn nicht geklappt => wird 404 angezeigt.
- <- diese Funktion dann in ls.py\_ `detail()` aufrufen.
- `job_detail = get_object_or_404(Job, pk=job_id)` - `pk`=PrimaryKey; `Job` = Objekt-Typ
- in _/migration/XXX_initial.py_ kann man schauen, aus welchen Feldern die DB besteht. (migratoins.CreateMode)
- man braucht ein Template _detail.html_
- auch `detail()` entsprechend anpassen

### 3 - Designing objects detail views

- von _home.html_ etwas in _detail.html_ kopieren und anpassen
- `<a href="{% url 'home'}"` - _home_ ist name=".." von path in _urls.py_

### 4 - URL paths with parameters

- `{{ }}` benutzen, wenn man Variablen aus Code in Template einfügen möchte => oft die Parameter in den Funktionen von _urls.py_ also: `<img src={{ job.image.url }}></img>`
- `<a href="{% url 'detail' job.id %}">` - in _.html_ eingeben. => wenn `detail(requset job.id)` wird **job_id** übergeben

### Next Step

- djangoproject.com schauen:
  - Klassenbasierte views
  - Authentifikation
  - Rest APIs
- Webseite deployen = Online stellen mit:
  - Digital Ocean ode AWS
  - Heroku
  - Python Anywhere
