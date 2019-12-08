### 0 - Introduction
#### 1 - Installation on Windows
* Installieren
* Pfad von Mongo-DB zu PATH aufnehmen
* in cmd:
    * `md \data` - Ordner für Daten erstellen
    * `md \data\db` - sowas wie .conf für MongoDB
    * `mongod` - Mongo-Deamon starten
* zweite cmd öffnen:
    * `mongo` - mongo-Shell öffnen
    * `db.users.insert({"name":"Kirill Haha"})` - Eintrag in MongoDB
#### 2 - Installation on MacOS
1. man kann auch per homebrew installieren
2. .tar herunterladen
    * entpacken
    * /bin zu PFAD aufnehmen oder alles in /usr/local/bin entpacken
* `mkdir -p /data/db` + eventuell Berechtigunen ändern
* `mongod`
* `mongo`
* `db.users.insert({"name":"Kirill Haha"})` - Eintrag in MongoDB
#### 3 - Environment setup
* Node.js installieren
    * Libs installieren:
    * `npm install` <- in Exercise Files ausführen
    * `httpie` installieren, dafür python3 und pip3 installieren
    * `pip3 install httpie`
### 1 - Understanding MongoDB
* Nachteile der rel DB:
    * DB-Design kann komplex werden
    * wenn Schema geändert wird, muss man auch Code ändern
* NoSQL (Document-DB):
    * sehr nach am Code-Object
    * Entwickelt für Developers
    * eine Tabelle -> ein Eintrag = ein Object = ein JSON-Eintrag
    ```nosql
    db.users.insert({"first_name":"John", "last_name":"Smith", "address":"123 Mayberry Place", "phone":"555-555"});

    db.users.find(); //alle Einträge
    db.users.find({"first_name":"John"}) //nach John suchen
    db.users.find({address: {$exists: true}})
    ```
* JSON-Format
* JavaScript shell commands
* Excellent drivers für viele Sprachen
* um umfangreichere Daten zu verwalten
#### 2 - Document-oriented data
* Document in MongoDB ist JSON-Objects
* werden in BSON-Format (binary JSON) gespeichert
* flexibles Indexing
* da JSON kann leicht im Code adaptiert werden
* MongoDB-Object hat `"_id"` -> man kann hier beliebigen String benutzen => sollte aber Unique sein
* remove: `db.users.remove({first_name:"John"})`
* update:
    * `db.users.update({first_name: "John"}, {"first_name":"John", "last_name":"Martin", ...})` - ganze Objekt updaten, wenn man alte Felder weglässt, werden diese Felder gelöscht, da NoSQL
    * `db.users.update({first_name: "John"}, {$set: {"last_name": "Smith"}})` - nur Teil des Objekts updaten
* Embedding = Nested Arrays:
    * Objekt im Objekt:
    * 
    ```json
    {
    "_id": ObjectID(".."),
    "first_name": "John",
    "last_name": "Smith",
    "phone": [
            "555-555",
            "444-444"
        ]

    }
    ```
    * `db.users.find({phone:"555-555"})` - Sucht auch in Unterobjekten
* zu `find`
    * `db.users.find({"phone": {"type":"fax","number":"555-555"}}, {"phone":1})` - bei *phone* nach *type* * fax* und *number* suchen und nur *phone* ausgeben/returnen
    * db.users.find({},{"phone":1});
#### 3 - Embed or refernce?
#### 4 - Performance

### 2 - Explore the System
#### 1 - Explore the Mongo shell
#### 2 - Import the data into the database
#### 3 - Mongo shell operations
#### 4 - Simple indexing

### 3 - Build an Application in Node
#### 1 - Unique indexes
#### 2 - Tune Mongo queries
#### 3 - Text indexes
#### 4 - Model your schema
#### 5 - Aggreation
#### 6 - Replication and sharding
