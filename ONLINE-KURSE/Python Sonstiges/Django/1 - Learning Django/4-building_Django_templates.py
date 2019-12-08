#1 - Django Templates
# = sind html-Dateien mit spezieller Syntax
#Wenn view.py render aufruft => render füllt Template mit Parametern und Template erzeugt html-Datei
#Template Syntax:
{{ variable }}
<h3> {{ pet.name }} </h3>

{% tag %}  #für Loops und If-s
{% for pet in pets %}
    <li>{{ pet.name }} </li>
{% endfor %}  #ist notwendig um das Ende des Loops zu markieren

{{ variable|filter}} #Temlate-Filter = nimmt String an und return String zurück wie Pipe in Bash <- um Format zu veränder z.B bei Datum
<h3> {{pet.name|capfirst}} </h3> #=>pet.name benutzt eingebauten Filter capfirst = erster Bushstabe wird groß

#manche Template-Tags haben keinen end-Tag => rendern nur String
    #sollte in url.py stehen
{% url "index" %}  #hier wird name="index" benutzt. <- URL-Tag mit Argument home wird Pfad zu home-View generieren => Output: /
{% url "pet_detail" pet.id %} => Output /adoption/pet.id/

#Base-Template von Django (base.html):
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
#<- jedesmal wenn man {%block blockName% benutzt} => wird der Block blockName von dem Eltern überschrieben

print()
#2 - Implement Django Templates

print()

#3 - Structure Templates
# = base.html erstellen und andere Templates von diesem Erben lassen

print()

#4 - Integrate CSS and JavaScript
#statische Dateien = CSS und JS zuerst über ProjectName/ProjectName/settings.py einstellen:
#STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")  #BASE_DIR ist oben in settings.py definiert (meist ist ProjectName/ProjectName); join() ist die python-Funktion um Pfade zu bauen
]

#dann in base.html als erste Zeile einfügen:
{% load static %}
#jetzt kann man in hrefs, links usw. die Dateien die in static-Ordner den HTML-Tags vergeben mit:
"{% static "style.css" %}"


#Weitere Tipps:
#Tipps zu Lernen:
#Pythoen, SQL, Rest
#Django-Doku + Django-Tutorial checken:

#Tipps welche Django-Settings sollte man ändern:
# DEBUG:
#DATABASES: <- PostgreSQL, MySQL
