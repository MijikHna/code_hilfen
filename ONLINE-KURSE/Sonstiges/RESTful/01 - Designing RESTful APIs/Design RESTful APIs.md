### 0 - Introduction
* Bsp: API zum Buch kaufen
* Medium ist HTTP

### 1 - Who needs your API
####  Why good API design is important
* API Desing:
    * Welche Funktionen
    * wie diese Funktionen anbieten
    * Testen
    * eventuel oberen drei wiederholen
* API -> Anbieten = API bietet Schnittstelle an
#### Three approaches to adding an API
* drei Annährungen API dem Projekt hinzuzufügen
    1. Bolt-On Strategie = API dem System hinzufügen (Brute-Force, schnell). Fehler des System gehen weiter.
    2. Greenfield Strategy = noch kein System (API first - am einfachsten API zu entwickeln) 
    3.   Facade Strategie (etwas zwischen 1. und 2.) = bestimmte Teile des System anpassen.
#### Tips for modeling APIs
* 3 Regel:
    1. Tools doesn't matter 
    2. festen + dokumentierten Prozess haben
    3. alles dokumentieren auch Annahmen, Fehler, Task die später kommen könnten
#### Identifying participants
* Prozess verstehen
    1. Identify Participants
    2. Identify Activities
    3. Into Steps
    4. API Definitions
    5. Your API
* Identify Participants:
    1. Leute, die API nutzen werden = Entities, die API nutzen werden (nicht alle müssen Menschen sein)
    2. Wer/Was is in den Prozess involviert:
        1. Wer initialisiert den Prozess
        2. Wer wartet, bis Action passiert
    * <- diese aufschreiben, ob internal/external
    * Bsp: Kaffe bestellen
        1. Käufer
        2. Barista
        3. Kassierer
        4. Payment Prozess (Bar, Karte)
        5. andere Käufer
        * <- schreiben, was enzelner genau macht (welche Aktionen)
#### Identifying activities and break them into steps
* = Step 2
* Bsp: Aktivität Kaffe bestellen
    1. Käufer bestellt beim Kassierer
    2. Kasierer gibt Bestellung weiter an Barista
    3. Barista queuet die Bestellung zu andren Bestellungen
    4. Kassier sagt dem Käufer den Preis
    5. Käufer bezahlt oder sagt Bestellung ab (hier muss man dann zweigleisig weiter gehen)
    6. Barista macht den Kaffe und gibt es dem Käufer

### 2 - What does your API look like
#### Createing and grouping API methods
* Bsp: Buch bestellen
* Schritt 3
* Grenzen auswählen
    1. Wer sind die Participants:
        1. Custommer
        2. ~~System Admin~~
        3. ~~Developer~~
        4. Verkäufer
        5. Customer Support
    2. Aktivitäten:
        1. Käufer sucht nach dem Buch = View Items
        2. Käufer added das Buch zum Einkaufswagen = Add Item to cart 
        3. ~~Käufer added oder removen weitere Bücher~~ - da momentan API nur für einen Buch = Add more Items
        4. Käufer meldet sich ab = check out
        5. Verkäufer versenden das Buch = fulfill the ship order
        6. Wenn das Buch nicht vorrätig ist, Customer Support informiert den Käufer = review order/cansel order
        * <- da erste Entwurf kann/wird Fehler haben

#### Mapping activities to verbs and actions
* API Definitionen machen
* Schritt 4
* Ressourcen = Nomen aus Schritt 3
* Also
    1. Item
    2. Item, Cart
    3. Cart, Order
    4. Order

    * Cart -> Design Dession machen. Cart = Collection of Items oder eigene Ressource/Object (hier Collection of Items)
    * Weitere eventuelle Ressourcen
        * Custommer
    Weiere Aktions
        * Check Out Method

#### Validating your API
* API Definition (Schritt 4)
* Verben (GET,PUT=Update, DELETE,POST=create/update)
* Verben von HTTP zu unsren Verben mappen
    1. list items = GET items
    2. view item = GET item
    3. Create cart = POST cart
    4. Add item to cart = PUT cart
    5. check out = POST cart
    6. create order = von checkout erledigt
    7. view order = GET order
    8. cancel order = POST order
* Customer Ressource:
    1. customer registration - noch nicht festgelegt z.B mit Productowder klären
    2. view customer = GET customer
* Diese Ressourcen haben Beziehungen
    1. Independent
    2. Dependent = Ressource kann nur existieren, wenn eine andere Ressource schon existiert
    3. Associative = independent oder dependent, dass aber weitere Info braucht
* <- auf Buch bestellen angewendet:
    1. item independent
    2. cart dependent von items
    3. order dependent von cart und customer
    * <- Dependenciemap (wie in DB (aber nicht einfach Schema von DB nehmen))
    
### 3 - How does you API work
* Validate API:
    * Pseudo Code schreiben, der die API nutzt
    * Microframeworks nutzen
        * hapi.js für node.js, sinatra für Ruby, slim oder silex für PHP
        * schauen, ob incomping Requests akzepiert werden
        + VERB und Urls damit validieren
        * Static HTTP Responses returnen
    + Also:
        + list the end points
        + list the parameters
        + list the response codes
        + show the reponse paylouds
    * <- dabei wird sozusagen Dokumentation erstellt

#### Overview of HTTP
#### HTTP Overview
* HTTP = Protokol
* XML = Markup Sprache
* JSON = Notation
* REST = nichts von den oberen. REST = Vereinbarung von Prinzipien und Constraints (Beschränkungen)
SOAP vs REST
* SOAP: feste Prozesse, detalierte Szenarien, komplexes Error-Handling
* REST: wenige Requirements, basierend auf den Needs der Partien, basierend auf Patterns
* HTTP-Request/Response = Header + Payload
#### HTTP headers and resonse codes
* `curl -I https://..` - nur Header anzeigen 
* API-Clienten verstehen diese Headers
* man sollte keine eigene Response-Codes erstellen. Standard-Codes sind schon gut.
#### REST APIs: The six constraints
* REST ist kein Standard. er bunutzt aber Standards
* 6 Constraints:
* man kann auf diese 6 Constraints vezichten, da als beste practice etabliert
    1. Client-Server Arch
    2. Stateless Arch => z.B Authentication-Daten bei jedem Request senden
        + da HTTP Stateless ist
        * Stabilität, Reliabilität, Flexibilität
    3. Cacheable = ob Request-Response-Paar kann gecacht werden
        * Message sollte enthalten, ob sie Cacheable ist und wie lange => Bandbreite sparen
            * => gleiche Anfragen => gleiche Anfrage
    4. Layerd System
        * man sollte nicht annehmen, dass Client nicht direkt mit Server reden, es können also andere Layers dazwischen liegen
    5. Code on Demand (optional aber powerfull)
        * API kann weiterentwickelt werden, ohne Client zu verändern
    6. Uniform Interfaces
        * URI
        * = Ressource addressieren
        * sind self-descriptive
        * HATEOAS - sowas wie Links
            * Ressourcen bei Links angesprochen werden
### 4 - Common Desing Challenges 
#### Authentication and authorizatin
* Authenticatoin = Wer du bist
* Authorization = war ist erlaubt mir zu tun
    * gruppe
    + Context
    + usw
Bsp: für AuthN/AuthZ
* API Keys für Authentication <- Nachteil: kann abgefangen werden
* eigneen AuthN/AuthZ Protokol schreiben
* OAuth 2.0 = AuthN/AuthZ - Protokol:
    * oft in API benutzt
    * man sollte fertige OAuth2.0-Prokolle benutzen
        + Couse Tip: Web Security OAuth und OpenID Connect
#### Versioning best practices
* Versionierung in URL vs Header
* Accept Header = Content Negotiation
    1. z.B auswählen ob XML oder JSON
    2. Media Type auswählen
    3. Version der Mediy Types auswählen
    * Bsp Versioning in Header mit curl: `curl -I https://... -H "Accept: application/vnd.github.v3+json"`
* Bsp Verioning in URL: `curl -X POST "https://../2010-04-01/Accounts/../`  - 2010-04-01 ist die Version
#### Choosing media types and processing content
#### Hypermedia approaches
#### Advanced HTTP headers: Content negotiation and caching
#### Documentation approaches
#### SDK design considerations