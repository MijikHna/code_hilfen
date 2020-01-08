#1 - Connecting URLs and template in Django:
    # zu /admin gehen und Einträge (hier Jobs einfügen)

    #in models.py Funktion für Model hinzufügen, damit in /admin die Einträge etwas aussagekräftiger angezeigt werden

    def __str__(self):
        return self.summary

    #neuen Path einfügen in /portfolio/urls.py:
    path('/jobs/<int:job_id>', jobs.views.detail, name="detail")  #/jobs/<int:job_id> = wenn man jobs/x eingibt und x ist ein int => wird diese int in job_id gespeichert
    #=> in jobs neue Funktion deail erstellen

#2 - Creating views in Django:
    #mit jobs_id den richtigen Job aus DB holen.
    from django.shortcuts import get_object_or_404 # Funktion importieren; diese Funktion holt bestimmtes Object aus DB, wenn nicht geklappt => wird 404 angezeigt.
    #<- diese Funktion dan in urls.py detail(): aufrufen.
    job_detail = get_object_or_404(Job, pk=job_id) #<- pk=PrimaryKey; Job = Objekt-Typ
    #<- in /migration/XXX_initial.py kann man schauen, aus welchen Feldern die DB besteht. (migratoins.CreateMode)
    #man braucht ein Template detail.html

#3 - Designing objects detail views:
    #von home.html etwas in detail.html kopieren und anpassen
    <a href="{% url 'home'}" #<-- home ist name=".." von path in urls.py

#4 - URL paths with parameters:
    #{{  }} <- benutzen, wenn man Variablen aus Code in Template einfügen möchte => oft die Parameter in den Funktionen von urls.py

    <a href="{% url 'detail' job.id %}">  # in .html eingeben. => wenn detail(requset job.id) wird job_id übergeben


#Next Step:
    # djangoproject.com schauen:
        #Klassenbasierte views
        #Authentifikation
        #Rest APIs
    #Webseite deployen = Online stellen
        #mit:
            #Digital Ocean ode AWS
            #Heroku
            #Python Anywhere
