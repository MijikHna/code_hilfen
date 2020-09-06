#### Was wird benötigt:
1. Python 3.7.4
2. Django
3. VirtualEnv
4. Flexmonster Pivot Table + Charts (JS-Bibs)
5. SQlite = DB

`__init__.py` Python als Package behandeln  

`request` - ist Instanze von `HttpRequestObject`, die Info über den Request hat (Request Methode (GET/POST)).
`render` - sucht nach HTML Templates in **templates**  

Mit Django ORM kann man DBs benutzen die SQL-Sprache können  

Migration - eine Datei die beschreibt, welche Änderungen an DB ausgeführt werden sollen. (`python manage.py makemigrations dashboard` + `python manage.py migrate dashboard` (dabe werden die Änderungen zu DB tatsächlich gemacht))  

`python manage.py shell` - Shell öffnen nur Zugriff auf Djang-Project/App hat

#### Daten mit Flexmonster verbinden:
= Daten aus Model zum Data Visualisation Tool **Flexmonster** verbinden. d.h. Backend und Flexmonster miteinander kommunizieren lassen. Es gibt zwei Möglichkeiten dazu.
1. **request-response cycle** benutzen = Python und Django Template Engine benutzen um JS-Code direkt in Template einzubinden
2. **async request(AJAX)** benutzen. Das Daten in JSON returnt. (Ist besserer Weg)  

Flexmonster hat speziele Eigenschaft für Daten, mit der man Feld Daten Typen, Captions und Multi-Level Hierarchien einstellen kann
```json
mapping: {
    "product_category": {
        "caption": "Product Category",
        "type": "string"
    },
    "payment_method": {
        "caption": "Payment Method",
        "type": "string"
    },
    "shipping_cost": {
        "caption": "Shipping Cost",
        "type": "number"
    },
    "unit_price": {
        "caption": "Unit Price",
        "type": "number"
    }
}
```
Code kann man hier anschauen: https://github.com/veronikaro/django-dashboard-app
FreeCode-Link: https://www.freecodecamp.org/news/how-to-create-an-analytics-dashboard-in-django-app/