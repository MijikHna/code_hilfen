#1 - Understand URL patterns
# URL-Patterns abfertigen Requests zu Views
#benutzen Reguläsre Ausdrücke um URL zu interpretieren:
#ducky = String der ducky enthält
#\d = eine Zahl
#\d+ = merhrere Zahlen
#^admin/ = admin/xxx/xxx <- admin muss am Anfang stehen
#suffix$ = suffix muss am Ende stehen
#^$ = leeres String = beginnt mit nichts + endet mit nichts
#pythex.org = Reguläre Audrucke in Python:
#Bsp für URLS:
    #url.py hat urlpatterns-Var, die Liste Aufrufe für url() enhält.
urlpatterns=[
    #url() hat drei Param:
    #1 - Reguläre Audrück um Requests zu spezifizieren -> r'^$' = leerer String (r = raw-String(d.h benutzt kein / als Escape-Charakter))
    #2 - Welche View soll aufgerufen werden <- heißt welche Funktion in View.
    #3 - für Templates
    url(r'^$', views.home, name="index")

    #<- urlpatterns hat mehrere url() <- es wird geschaut, welche Reguläre Expression zutreffend ist und entsprechende View aufgerufen
]

#wenn man falsche URL eingibt => wird Debug-URL mit Error-Hinweise kommen <- Falls man in Config Debug auf false macht => kommt einfach 404-Seite

#2 - Implements URL patterns

#3 - Implements Django views
#im Beispiel wurden template-Files und Views-Namen gleich genannt <- ist aber nicht erforderlich
#templates in AppOrnder/templates erstellten <- eventuell zuerst Ordner templates erstellen
