#1 - Bootstrap overview and isntallation
    #=Bootstrap-Example-Pages benutzen:
        #https://getbootstrap.com/ -> Examples -> z.B Album auswählen -> View Page-source -> alles Auswählen und z.B in eigenenes home.html einfügen
    #Bootstrap selbst einfügen:
        #https://getbootstrap.com/ -> Get Started -> CSS-Link kopieren -> JS kopieren. -> so anpassen wie man es möchte.

#2 - Page layout and template in Django

#3 - Adding static images to your Django Projects
    #in /jobs Order static erstellen (eventuel darin noch images)
    #Django sagen, wo statische Sachen liegen => in setttings.py einstellen:
    #STATIC_URL
    #STATIC_ROOT = os.path.join(BASE_DIR, "static")
    #noch in urls.py sagen wo es die Static-Sachen finden kann:
        #from django.conf import settings
        #from django.conf.urls.static import static
        #+ am Ende von urlpatterns =[] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#4 - Collectstatic in Django
    #python3 manage.py collectstatic  = alle Statischen Dateien in /portfolio-project/static bringen bzw. zum Order, denn man mit STATIC_ROOT eingestellt

    #auf der HTML-Seite ganz oben eingeben:
    #{% load static %}
    #und dann es so benutzen:
        #<img src="{% static 'Per_Foto.jpg' %}" alt="">
    #=> als Folge sollte globaler Ordner static erstellt werden.

    #<- Bei mir hat es nicht geklappt => muss dann {% static 'image/Per_Foto.jpg' %} benutzen

#5 - Bootstrap as a static asset in Django
    #=Bootstrap herunterladen und selber hosten => nicht auf Bootstrap-Host angewiesen
    #bootstrap herunterladen, jquery (Link speichern utner), popper.js.org (Link speichern unter)
    #und als {% static '../../name.css' %} einfügen

#6 - Finishing touches in Django design
    #In settings.py folgendes Einfügen:
        #MEDIA_URL = "/media/"  = URL media nennen
        #MEDIA_ROOT = BASE_DIR = Link zu dieser URL ist BASE_DIR

        #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #dem URL-Patterns sagen, dass es jetzt noch /media/ gibt.
