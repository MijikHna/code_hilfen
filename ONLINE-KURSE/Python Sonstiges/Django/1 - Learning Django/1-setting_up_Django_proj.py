#1 - what is django
#www.djangoproject.com
# = Python-Framework
#Framework = Sammlung von Tools, um Webseiten zu bauen
#Django-Tools: ORM (Object-relational Mapping) = um DB-Anfragen zu machen, URL-routing = welcher Logik soll gefolt werden, abhängig von der URL-eingabe, HTML-Templating = HTML-Präsentation, Form-Handling, Testing-Tools
#!Django = Tool, was in Python geschrieben ist <- keine Sprache, kein WebServer (aber enhält eingebaueten WebServer)

print()
#2 - install python and django
#python.org -> herunterladen und installieren
#<- mit pip3: pip3 install django==1.11.7

print()
#3 - create a Django project
#django-admin startproject ProjectName  = Wird Ordner für Django-Projekt angelegt mit folgenden Dateien darin: (djang-admin.py startproject WisdomPets)
#manane.py = führt Befehle des Projekt aus
#ProjectName/__init__.py = Ordner enthält Python-Dateien
#ProjectName/wsgi.py = Provides a hook for Web Server
#ProjectName/settings.py = konfiguriert Django
#ProjectName/urls.py = routet Requests abhängig von URL

#python3 manage.py runserver = Server Starten und da Django ausführen

print()
#4 - create a Django app
#Django-App = Ordner mit Python Dateien

#python3 manage.py startapp appName => es Wurde ordner mit appName erstellt (pyhon3 manage.py startapp Adoptions)
#<- ProjectName/settings.py -> zu INSTALLED_APPS gehen und appName, am Ende der Liste eintragen

#AppName-Ordner hat:
#1-app.py = Konfiguration und Initialisierung
#2-models.py = Data layer -> DB-Schema und DB-Anfragen machen
#3-admin.py = Administratives Interface =
#4-urls.py = URL routing
#5-views.py = Control layer = Logik um mit den Requests umzugehen und HTML-Responses erstellen
#6-tests.py = App testen
#7-migrations/ = enhält Migrations-Dateie <- DB-Dateien, wenn man DB-Schema ändert
