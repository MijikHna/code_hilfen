#1 - models, routing, view and templates
#Architekture des Framework verstehenself.
#Django benutut Model View Controler aus 4 Teielen:
#1) URL Patterns: projectOrdner/urls.py
#Wenn Django-App bekommt Web-Requests => werden URL Patterns benutzt
#2) Views:  projectOrdner/views.py
#Logik bzw. Kontrollfluss der App <- sind Funktionen bekommen als Param HTTP-Req und erzeugen HTTP-Response
#3) Templates: projectOrdner/adoptions/templates/
#HTML mit Template-Syntax
#4) Models: projectOrdner/adoptions/models.py
#Um DB-Angragen zu machen kann View die Models dafür benutzen. Django-Model ist Klass mit Attributen, das DB-Schema definiert => ~ Build-In Methoden um DB-Anfragen zu machen
#Bsp: Vorgehensweise:
#http://yoursite.com/ -> wird in URL schauen, welche View für / er benutzen soll -> View wird dann eventuell DB-Anfragen mittels Models machen -> DB-Antwort werden in home/index.html eingesetzt
print()
#2 - Django models
# Data Layer der App
# definiet DB-Struktur
# erlaubt DB-Anfragen
# models ist Klasse die von django.db.models.model erbt
#~Excel-Tabelle
#Model-Klasse ersteleln:
# 1- django.db.model imortieren:
# 2- eigene Klasse erstellen, die von models.model erbt + eigene Attribute erstellen:
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

print()
#3 - Django fields

print()
#4 - implements models and fields

print()
#5 - Django migrations
#Models = Struktur der DB
#Migrations = Skripte um DB-Struktur zu verändern:
#Initial Migration = DB-Tabellen aus dem Model zu erstellen
#Wann Migrations nötig:
# 1 - DB-Scheme erstellen
# 2 - neue Felder in DB-Tabellen erstellen
# 3 - Felder löschen
# 4 - Felder ändern

#Migratinsbefehle:
#python manage.py makemigrations = erzeugt Migrationsdateien = schauet Model-Felder and und aktuellen Stand der DB
#python manage.py migrate
#python manage.py showmigrations

#Migration für Bestimmte APP und Nummer laufen:
#migrate appName Nummer
#Wenn Migration-Datei erstellt, aber nicht ausgeführt => unapplyed Migration

#Bsp -> Vorgehensweise:
#in Terminal zum Projekt navigieren -> python3 manage.py makemigrations eingeben. -> wird ind ../migrations/ Datei 0001_initial.py erstellt -> python3 manage.py showmigrations = zeigt alle Möglichen Migrationen an in Gruppen; [ ] = wurd noch nicht angewendet -> python3 manage.py migrate = alle Migrationen anwenden



print()
#6 - Import CSV data

print()
#7 - work with the Django admin
#Admin-Interface für Project erstellen
# 1- AppName/admin.py öffenen  (erste Zeile importiert admin-Modul von django.contrib)
# 2 - Eigene Imports machen
#< - siehe admin.py
# ...
#3 - SuperUser erstellen um in Admin-Interface anzumelden
# python3 manage.py createsuperuser:
#name: project-root
#passw: djangolernen
#=> localhost:8000/admin


print()
#8 - Query data with Django ORM
#= DB-Querys mit in Django implementierten Funktionen:
#im Kurs in Shell:
#python3 manage.py shell = wird python-Shell aufgemacht
#from Adoptions.models import Pet
    #Django-Models haben ein Attribute object mit Funktionen für DB-Querys
#Pet.object.all() = returnt alle Instantenzen von Pet (=> ein Array)
#pets = Pet.objects.all()
#pet = pets[0]
#pet.name; pet.description

#Django macht auch ein ID für jedes Model, startet bei 1 (eigentlich Primar Key):
#pet.id

#Einzelne Queries machen
#pet = Pet.objects.get(id=1) <- falls falsche ID => Exception
#!! get() kann nur ein Object zurückgeben (also kein Array). Also falls:
#Pet.objects.get(age=1) => werden mehrere Pets returnt => MultipleObjectException
#=> get() ist eigentlich für id-es gut
# <- man kann im views.py diese Exceptions checken

#pet.vaccinations.all()
