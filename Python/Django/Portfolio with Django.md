### 3 - Django and Databases
#### 1 - Creating the models in DjangoTemplates
* DB um Jobs zu speichern
* Model = Klasse, die in DB gepeichert wird:
    * in `/portfolio-project/models.py` erstellen <- kann man mehrer Classen erstellen.

#### 2-Postgres setup for Django:
* per Default steht in *setttings.py* welche DB genutzt wird
* Postgres:
    1. installieren
    2. `sudo su - postgres` - sich als user postgres anmelden
    3. `psql` - sich mit DB verbinden
    4. `\conninfo` - Verbindungsinfo anzeigen
    5. `\password postgres` - Passwort für User postgres vergeben/ändern
    6. als user postgres -> `creatdb dbname` = DB erstellen
    7. als user postgres -> `dropdb dbname` = DB löschen

#### 3-Connecting your Django project to Postgres:
* bei `settings.py` noch Postgres einfügen:
* in DATABASE
```python
'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'portfoliodb',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': 'localhost',
    'PORT': '5432',
}
```
* damit Django sich mit Postgres verbinden kann bracht er psycopg2-binary =>:
    * `pip3 install psycopg2-binary`

#### 4-Make Django migrations and migrate:
* Migrationen = Wege um DB für Django-Projekte zu setzen
    * `python3 manage.py makemigrations`  = Ausführen, wenn man Änderungen im Model macht.
    * `python3 manage.py migrate` = die Migrationen ausführen

#### 5-Setting up an admin panel in Django:
Um sich in localhost\admin anmelden zu können => zuerste admin-user erstellen
* `python3 manage.py createsuperuser`
* `admin -> django1234`

#### 6-Creating model objects via the admin panel in Django:
* der Admin der APPP (nicht des Projects) verwaltet das Model =>admin.py öffnen und
    * `form .models import Jobs` - Klasse Jobs aus models.py einbinden
    * `admin.site.register(Jobs)` - den Admin über die Jobs-Klasse wissen lassen

#### 7-Pulling objects from the database in Django:
* in *view.py* Code schreiben, um Jobs anzuzeigen

### 3 - Django and Databases
#### 1 - Bootstrap overview and isntallation
* Bootstrap-Example-Pages benutzen:
    * https://getbootstrap.com/ -> Examples -> z.B Album auswählen -> View Page-source -> alles Auswählen und z.B in eigenenes home.html einfügen
* Bootstrap selbst einfügen:
    * https://getbootstrap.com/ -> Get Started -> CSS-Link kopieren -> JS kopieren. -> so anpassen wie man es möchte.

####2 - Page layout and template in Django

####3 - Adding static images to your Django Projects
* in */jobs* Order static erstellen (eventuel darin noch images)
* Django sagen, wo statische Sachen liegen => in *setttings.py* einstellen:
* `STATIC_URL`
* `STATIC_ROOT = os.path.join(BASE_DIR, "static")`
* noch in *urls.py* sagen wo es die Static-Sachen finden kann:
* `from django.conf import settings`
* `from django.conf.urls.static import static`
* \+ am Ende von `urlpatterns =[] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)`

####4 - Collectstatic in Django
1. `python3 manage.py collectstatic` - alle Statischen Dateien in */portfolio-project/static* bringen bzw. zum Order, denn man mit *STATIC_ROOT* eingestellt
2. auf der HTML-Seite ganz oben eingeben:
    * `#{% load static %}`
    #und dann es so benutzen: `<img src="{% static 'Per_Foto.jpg' %}" alt="">` 
* => als Folge sollte globaler Ordner *static* erstellt werden.
ODER
* muss dann so `{% static 'image/Per_Foto.jpg' %}` benutzen

#### 5 - Bootstrap as a static asset in Django
* Bootstrap herunterladen und selber hosten => nicht auf Bootstrap-Host angewiesen
    * Bootstrap herunterladen, jquery (Link speichern utner), popper.js.org (Link speichern unter)
    * und als `{% static '../../name.css' %}` einfügen

#### 6 - Finishing touches in Django design
* In `settings.py` folgendes Einfügen:
`#MEDIA_URL = "/media/"` - URL media nennen
`#MEDIA_ROOT = BASE_DIR` - Link zu dieser URL ist BASE_DIR
* `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` - dem URL-Patterns sagen, dass es jetzt noch */media/ gibt*.

### 5 - Object datails in Django
#### 1 - Connecting URLs and template in Django:
* zu */admin* gehen und Einträge (hier Jobs einfügen)
* in models.py Funktion für Model hinzufügen, damit in /admin die Einträge etwas aussagekräftiger angezeigt werden
```python
def __str__(self):
    return self.summary
```   
* neuen Path einfügen in /portfolio/urls.py:
    * `path('/jobs/<int:job_id>', jobs.views.detail, name="detail")  #/jobs/<int:job_id>` - wenn man *jobs/x* eingibt und *x* ist ein *int* => wird diese *int* in *job_id* gespeichert
    * => in *jobs* neue Funktion *detail* erstellen

#### 2 - Creating views in Django:
* mit *jobs_id* den richtigen Job aus DB holen.
* `from django.shortcuts import get_object_or_404` - Funktion importieren; diese Funktion holt bestimmtes Object aus DB, wenn nicht geklappt => wird 404 angezeigt.
* <- diese Funktion dann in *urls.py detail():* aufrufen.
* `job_detail = get_object_or_404(Job, pk=job_id)` -  `pk`=PrimaryKey; `Job` = Objekt-Typ
* in */migration/XXX_initial.py* kann man schauen, aus welchen Feldern die DB besteht. (migratoins.CreateMode)
* man braucht ein Template detail.html

#### 3 - Designing objects detail views:
* von *home.html* etwas in *detail.html* kopieren und anpassen
* `<a href="{% url 'home'}"` - *home* ist name=".." von path in *urls.py*

####4 - URL paths with parameters:
* `{{  }}` benutzen, wenn man Variablen aus Code in Template einfügen möchte => oft die Parameter in den Funktionen von urls.py
* `<a href="{% url 'detail' job.id %}">` - in *.html* eingeben. => wenn `detail(requset job.id)` wird *job_id* übergeben


### Next Step:
* djangoproject.com schauen:
    * Klassenbasierte views
    * Authentifikation
    * Rest APIs
* Webseite deployen = Online stellen mit:
    * Digital Ocean ode AWS
    * Heroku
    * Python Anywhere
