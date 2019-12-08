from django.contrib import admin

# Register your models here.

#eigene Klasse Pet aus dem Modul models.py, das im selben Ordner liegt importieren
from .models import Pet



#eigene Admin-Interface für Pets machen
@admin.register(Pet) #Klasse mit Admin registrieren, um zu sagen, mit welchem Modul es assoziert ist (hier mit Pet) (mit Hilfe des Dekoraters (Argument ist Model-Klasse))
class PetAdmin(admin.ModelAdmin):
    #ModelAdmin hat Attr list_display = welche Felder auf dem List-Screen angezeigt werden
    #sonst per Default wird einfach "Pet object angezeigt"
    list_display = ["name", "species", "breed", "age", "sex"]
