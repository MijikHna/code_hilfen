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
#### 3 - Embed vs. refernce?
* DB und Tabellen sind eigentlich json-Dateien => diese Datei anordnen als
    1. Embedded Data = eine große Datei
        1. einfacher
        2. weniger Code-operationen
        3. einfacher anzufragen und zu indexen
    2.  Reference Data = getrennte Dateien
        1. mehr Operationen zum Einfügen und Accessen
        2. 
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
        2. Queries.
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
#### 4 - Performance
* Mongo - Features:
    1. Indexing = Index für Tabellen aufbauen
        1. 64 Indizes pro Collection
        2. Single Field - Index  - einfach zu setten und ist schnell
        3. Compound Index = Index gegen mehrere Felder
        4. Unique - gegen Dublikate
    2. Sharding = Daten auf mehrere Machine verteilen => jeder Rechner sucht in seinen Dokumenten/Objekten
    3. Replications - automatic Failover

### 2 - Explore the System
#### 1 - Explore the Mongo shell
* `mongod`  - Server starten
* `mongo` - Mongo-Shell öffnen
    * `db` - verbundene db anzeigen
    * `use lala-db` - zu `lala-db` switchen, wenn nicht existiert, wird troztdem verbudnen. DB wird erstellt, sobald man erstes Obj erstellt
    * `db.cars.insert({"make": "Subaru"})` - in DB `lala-db` Tabelle `cars` erstellen und ersten Eintrag machen
    * `show dbs`
    * `show collections` - Tabellen anzeigen
    * `print("test")` - man kann JS-Befehle nutzen
    * `var arr=["one", "two", "three"]` - man kann Variablen setzen
    * `for (i=0; i<10000; i++){ db.nubmers.insert("nummber": i)}` - 10000 Eintraäge in Tabelle numbers machen
    * `db.numbers.count` - alle Einträge in Tabelle/Collection anzeigen
    * `db.numbers.find({"number": 1})`
    * `db.numbers.find({"number": 1}).explain()` - wie Query zusammengestzt wrde
    * `db.numbers.find({"number": 1}).explain(executionStats)`
    * ``db.numbers.createIndex({number:1})` - Index erstellen für **numbers**
    * `db.numbers.find({"number": 1}).explain(executionStats)`

#### 2 - Import the data into the database
* Daten, die in json, csv sind infügen
* `mongoimport --help`
    * namespace
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
#### 3 - Mongo shell operations
#### 4 - Simple indexing

### 3 - Build an Application in Node
#### 1 - Unique indexes
#### 2 - Tune Mongo queries
#### 3 - Text indexes
#### 4 - Model your schema
#### 5 - Aggreation
#### 6 - Replication and sharding
