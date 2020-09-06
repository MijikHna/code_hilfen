#### Intro
* was wird benutzt:
    1. Flask - Web-Store in Flask
    2. Testing mit Faker und Factory Boy

#### Project:
* zwei Model
    1. **Category**
    2. **Product**

* DB: Sqlite
    * als Driver wird **sqlalchemy** benutzt

#### Einführung Unittests auf Python
* Bib für Unit-Tests: **pytest** und **unittest** (es gibt auch viele andere für extra für Flask oder Django)
    * hier wird pytest verwednet:
    ```py test_XXXX.py
    def test_something():
        assert 2 == 1

    def test_sum():
        assert 1 + 1 == 2
    ```
    * FunktionenNamen und TestDateien sollte mit **test** beginnen
    * man kann im Terminal starten mit `pytest` - findet selbst nur Datei, die mit **test** beginnen, `pytest datei.py` 
* Probleme beim Testen: 
    1. man braucht eigentlich Server auf dem die APP läuft
    2. Objekte der Model erstellen

#### e2e
* es gibt viele Bibs, die für zum Testen von Views gedacht sind. 
* wird getestet:
    1. Views -> e2e
    2. 

+ Jeder Test sollte isoliert sein d.h. unabhängig von anderen sein. Dazu werden *before* und *after* ausgeführt
* Bsp mit 
```py test_app.py
from app import app

class TestViews:
    
    # eigentlich before
    def setup(self):
        print("before each")
        app.testing = True
        self.client = app.test_client()

    def teardown(self):
        print("after each")

    def test_home():
        response = self.client.get('/')
        assert response.status_code == 200

```