# Learning MongoDB

## 0 - Introduction

### 1 - Installation on Windows

* Installieren
* Pfad von Mongo-DB zu PATH aufnehmen
* in cmd:
  * `md \data` - Ordner für Daten erstellen
  * `md \data\db` - sowas wie .conf für MongoDB
  * `mongod` - Mongo-Deamon starten
* zweite cmd öffnen:
  * `mongo` - mongo-Shell öffnen
  * `db.users.insert({"name":"Kirill Haha"})` - Eintrag in MongoDB

### 2 - Installation on MacOS

1. man kann auch per homebrew installieren
2. .tar herunterladen
    * entpacken
    * /bin zu PFAD aufnehmen oder alles in /usr/local/bin entpacken

* `mkdir -p /data/db` + eventuell Berechtigunen ändern
* `mongod`
* `mongo`
* `db.users.insert({"name":"Kirill Haha"})` - Eintrag in MongoDB

### 3 - Environment setup

* Node.js installieren
  * Libs installieren:
  * `npm install` <- in Exercise Files ausführen
  * `httpie` installieren, dafür python3 und pip3 installieren
  * `pip3 install httpie`

## 1 - Understanding MongoDB

### 1 - Why Mongo

* Nachteile der rel DB:
  * DB-Design kann komplex werden
  * wenn Schema geändert wird, muss man auch Code ändern
* NoSQL (Document-DB):
  * sehr nach am Code-Object
  * Entwickelt für Developers
  * eine Tabelle -> ein Eintrag = ein Object = ein JSON-Eintrag

    ```js
    db.users.insert({"first_name":"John", "last_name":"Smith", "address":"123 Mayberry Place", "phone":"555-555"});

    db.users.find(); //alle Einträge
    db.users.find({"first_name":"John"}) //nach John suchen
    db.users.find({address: {$exists: true}})
     ```

* JSON-Format
* JavaScript shell commands
* Excellent drivers für viele Sprachen
* um umfangreichere Daten zu verwalten

### 2 - Document-oriented data

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
  * `db.users.find({"phone": {"type":"fax","number":"555-555"}}, {"phone":1})` - bei *phone* nach *type* *fax* und *number* suchen und nur *phone* ausgeben/returnen
    * db.users.find({},{"phone":1});

### 3 - Embed vs. reference

* Mongo kann Hierarchy der Daten bis 100 haben => aber wird langsam

* Embeded DAta
    1. einfacher arbeiten
    2. weniger Code
    3. einfacher zu querien und indexen

* Collections References
    1. mehr Operationen
    2. Referencen um Daten zu holen

* DB und Tabellen sind eigentlich json-Dateien => diese Datei anordnen als

* Bsp: Wiki-DB
  1. Tabellen-Felder:
      1. Pages
      2. Authors
      3. Tags
      4. Comments
* Lösung Embedded:
  1. Tabelle:

    ```json
    {
        "Type": "blog",
        "Title": "My blog post",
        "Author": "Kirsten Hunter",
        "Tags": ["great", "awesome" ],
        "Commetns": ["i love this post" ]
    }
    ```

  2. Queries:

    ```ts
    db.pages.find({"Author": "Kirsten"})
    db.pages.find({"Tags": "greate"})
    db.pages.insert({
        "Type": "blog",
        "Title": "My blog post",
        "Author": "Kirsten Hunter",
        "Tags": ["great", "awesome" ],
        "Commetns": ["i love this post" ]  
    })
    ```

  3. wenn man z.B weitere Daten für bestimmte Felds ändern möchte z.B

    ```json
    {
        "Type": "blog",
        "Title": "My blog post",
        "Author": {
            "name": "Kirsten Hunter",
            "twitter": "@lala"
        }
        "Tags": ["great", "awesome" ],
        "Commetns": [{
            "content": "i love this post",
            "user": "Fred Flint"
        }]
    }
    ```

  4. => man

    ```ts
    db.user.find({"Comments.user": "Fred Flint})
    //Ausgabe
    {
        "_id": ObjectID("8850adf"),
        "Type": "blog",
        "Title": "My blog post",
        "Author": {
            "name": "Kirsten Hunter",
            "twitter": "@alal"
        },
        "Tags": ["great", "awesome"],
        "Comments": [{
            "user": "Fred Flint",
            "content": "I Love this post"
        }]
    }
    ```

  * Lösung: References d.h z.B Comments speichern Referenzen auf Comments-Dokument
    1. Query-Bsp: Comments mit bestimmten User finden ("name")

    ```ts
    db.comments.find({
        "name": "Fred Flint",
        "page_id": true
    })

    var pageIds = comments.map(function(c){
        return c.post_id; 
    })

    db.pages.find({_id: {$in: pageIds}}, {title: true});
    ```

### 4 - Performance

* Mongo - Features:
    1. Indexing = Index für Tabellen aufbauen
        1. 64 Indizes pro Collection
        2. Single Field - Index  - einfach zu setten und ist schnell = Index für Feld setzen
        3. Compound Index = Index gegen mehrere Felder z.B man hat DB mit Autos. Man kann Index für Hersteller-Feld erstellen
        4. Unique - gegen Dublikate z.B User-eMail
    2. Sharding (auch Partitioning) = Daten auf mehrere Machine verteilen => jeder Rechner sucht in seinen Dokumenten/Objekten => Daten skalieren. Ist komplex zu konfigurieren
    3. Replications - gegen Failover.

## 2 - Explore the System

### 1 - Explore the Mongo shell

* `mongod`  - Server starten
* `mongo` - Mongo-Shell öffnen
  * `db` - verbundene db anzeigen
  * `use lala-db` - zu `lala-db` switchen, wenn nicht existiert, wird trotzdem verbunden. DB wird erstellt, sobald man erstes Obj erstellt
  * `db.cars.insert({"make": "Subaru"})` - in DB `lala-db` Tabelle `cars` erstellen und ersten Eintrag machen
  * `show dbs` - Tabellen- anzeigen
  * `show collections` - Tabellen anzeigen
  * `print("test")` - man kann JS-Befehle in Mongo-CLI benutzen
  * `var arr=["one", "two", "three"]` - man kann Variablen setzen
  * `for (i=0; i<10000; i++){ db.nubmers.insert("number": i)}` - 10000 Einträge in Tabelle numbers machen - HIER Mongo-Befehle + JS-Befehle
  * `db.numbers.count` - alle Einträge in Tabelle/Collection anzeigen
  * `db.numbers.find({"number": 1})`
  * `db.numbers.find({"number": 1}).explain()` - was Query gemacht hat
  * `db.numbers.find({"number": 1}).explain(executionStats)`
  * `db.numbers.createIndex({number:1})` - Index erstellen für **numbers**
  * `db.numbers.find({"number": 1}).explain(executionStats)`

### 2 - Import the data into the database

* Daten, die in json, csv sind importierbar
* `mongoimport --help`
  * namespace options
    * `-c` - Collection/TabellenNamen vergeben
    * input options
      * `-f FileNAME`

* Bsp json-Datei
  * `mongoimport --db learning_monog --collection tours --jsonArray --file tours.json`
  * `mongo`
  * `use learning_mongo`
  * `show collections`
  * `db.tours.count()`
  * `db.tours.find("tourTags": "hiking")`

### 3 - Mongo shell operations

* CRUD-Operationen
  1. `user lala-base`
  2. `db.lala.find({"lala": "lala"})`
  3. `db.lala.insert({"tournam": "The Wines", "toulenght": 3, "tourDesc": "lalal", "tourPrice": 500, "tourTag": ["wine", "Santa Cruz"]})`
  4. `db.lala.update({"touname": "Then Wines"}, {$set: {"tourRegion": "Cenral Coast"}})` Feld updaten `update(query, set)`
  5. `db.lala.update({"touname": "Then Wines"}, {$addToSet: {"tourTags": "Central Coast"}})` - Feld hinzufügen
  6. `db.lala.remove({"touname": "Then Wines"})`
  7. `db.lala.drop()`

### 4 - Simple indexing

* `db.tours.createIndex({tourPackage:1})` Index für Feld tourPackage erstellen, ohne `"` bei Index erstellen
* `db.tours.find({"tourPacakge": "Taste of California"}).explain(executionStats)` - ist schneller mit dem Index.
* `db.tours.find({"tourPrice": {$lte: 500}, "tourLenght: {$lte: 3}})` - mit `<` abfragen
* `db.tours.createIndex({tourPrice: 1, tourLenght: 1})` - Index für mehrere Felder erstellen
* man kan bis 64 Indexes pro Collection erstellen

## 3 - Build an Application in Node

### 1 - Node MongoDB setup

* Bsp mit MongoDB-Driver

```js index.js
var MongoClient = require('mongodb').MongoClient;

var url = 'mongodb://localhost:27017/learning_mongo';

MongoClient.connect(url, function(err, db) {
    console.log("Connected to server")

    db.close();
})
```

* `node index.js` = Ausführen

```js index.js
var MongoClient = require('mongodb').MongoClient;

var findDocuments = function(db, callback){
    var collection = db.collection('tours');

    collection.find().toArray(function(err, docs){
        console.log(docs);
        callback;
    });
}

var findDocuments2 = function(db, callback){
    var collection = db.collection('tours');

    collection.find({"tourPackage": "Snowboard Cali"}).toArray(function(err, docs){
        console.log(docs);
        callback;
    });
}

var url = 'mongodb://localhost:27017/learning_mongo';

MongoClient.connect(url, function(err, db) {
    console.log("Connected to server");

    findDocuments2(db, function(){});

    findDocuments(db, function(){
        db.close();
    });

    find
})
```

### 2 - Add APIs for read request in Hapi

* Node und HAPI-Framework für RESTful-APIs

```js
var MongoClient = require('mongodb').MongoClient,
    assert = require('assert'),
    Hapi = require('hapi');

var url = 'mongodb://localhost:27017/learning_mongo'

var server = new Hapi.Server();
server.connection({
    port:8080
})

// die HTTP-Routen
server.route( [
    // Get tour list
    {
        method: 'GET', // HTTP-Methode
        path: '/api/tours', //URL-Pfad
        config: {json: {space: 2}}, // json-Formatierung für response = Tabs für Json-Darstellung
        handler: function(request, reply) { // Handler = was soll gemacht werden, wenn diese URL angefergt wird

            collection.find().toArray(function(error, tours){
                reply(tours) //Array anzeigen in Browser bzw. Terminal (wenn curl), hier im Bsp: http http://localhost:8080/api/tours
            })

            // GET mit :id als Query-Params (http://localhost:8080/api/tours?tourPackage=Backpack Cal)
            var findObject = {};
            for (var key in request.query) {
                findObject[key] = request.query[key]
            }
            collection.find(findObject).toArray(function(error, tours) {
                assert.equal(null,error);
                reply(tours);
            })
        }
    },
    // Get a single tour
    {
        method: 'GET',
        path: '/api/tours/{name}',
        config: {json: {space: 2}},
        handler: function(request, reply) {
            collection.findOne({"tourName":request.params.name}, function(error, tour) {
               assert.equal(null,error);
               reply(tour);
            })
        }
    },
    // Home page
    {
        method: 'GET',
        path: '/',
        handler: function(request, reply) {
            reply( "Hello world from Hapi/Mongo example.")
        }
    }
])

// hier ist eigentlich die main()
MongoClient.connect(url, function(err, db) {
    assert.equal(null,err);
    console.log("connected correctly to server");
    collection = db.collection('tours');
    server.start(function(err) {
        console.log('Hapi is listening to http://localhost:8080')
    })
})
```

### 3 - Add APIs for write requests in Hapi

## 4 - Build an Application in Node

### 1 - Unique indexes
* 

### 2 - Tune Mongo queries

### 3 - Text indexes

### 4 - Model your schema

### 5 - Aggreation

### 6 - Replication and sharding
