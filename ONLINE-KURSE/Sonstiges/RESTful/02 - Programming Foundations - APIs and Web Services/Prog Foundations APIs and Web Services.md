### 1 - Understanding Web Services
#### 1 - Web services overview
* Web Service = erlaubt verschiednen Systemen miteinander über Internet zu kommunizieren.
* Client sendet Message zu Server, Server kann diese Message verstehen => z.B Message in XML
* SOAP vs REST
    * SOAP => sendet Messages in XML
    * REST => benutzt HTTP um Ressourcen anzusprechen
#### 2 - Advantages of web services
* Vorteile vom Benutzen Web Services:
    * Reusability
    * Language Transparency = Client und Server können in verschiednen Sprachen geschrieben werden. verstehen sich dennoch, da Messages in XML oder JSON
    * Usability 
    * Deployability
#### 3 - Condiderations of Web services
* Überlegen wann Web Service verwenden:
    * Latency = Time zwischen Request <-> Response
    * Partial Failure = wenn bestimmte Kommonente des Webs ausfällt
        * Bsp: Wenn bestimmte verschiedene Server verschiedene Teile der Transaktionen ausführen und einer z.B down ist.
#### 4 - Secure web services
* Public-Private Keys
* API-Token
* AuthN/AuthZ
    * AuthN - Wer du bist
    * AuthZ - Rechte des Users
    * AuthZ kommt nach AuthN
    * Bsp für AuthN/AuthZ
        1. Basic Authentication
            * username + password mit DB vergleichen -> bei Fehler 401
        2. API Key Authentication
#### 5 - Web services, APIs, and mircoservices
* API - Mechanismus um Daten zu teielen und zu kommunizieren. Evolution von Web Services sind aber dynamisch
* Web Service
* Alle Web Services sind APIs. nicht alle APIs sind WEb Services, haben viel Overhead
* Web Services bnutzen oft SOAP-Protokol.
* Microservices = viele kleine Komponenten die miteinader arbeiten.

### 2 - Using RESTful APIs and HATEOAS
#### 1 - Rest Overview
* Set of Guidelines um APIs zu designen
* 4 Prinzipien:
    1. Daten und Funktionalitäten sind Ressourcen -> über URI aufrufbar
    2. Ressourcen werden mit vorgegeber Anzahl an Operationen manipuliert (GET, POST, PUT, DELETE)
    3. Ressource kann in verschiedenen Formaten sein (XML; HTML, PlainText, JSON)
    4. Stateless - Server ist Stateless
#### 2 - Benefits of REST
* REST gut für Mobile Geräte, da SOAP viel Overhead sendet.
    * Payload = Daten die von Server/Client zu Client/Server
* RESTful beginnt klein, wächste dann mit der Zeit (=weiter Funktionalitäten)
* RESTful kann verschiedene Formate benutzen (SOAP nur XML)
* 
#### 3 - HATEOS overview
* RESTful API sollte genug Info an Client senden, dass er mit Server kommunizieren. SOAP - benutzt fixen Konstrakt (Protokoll ?)
* RESTful muss HATEOS implementieren
* = Ressourcen sind über Links erreichbar
#### 4 - Consume a RESTful API
* Bsp: public RESTful benutzen (github: https://github.com/15Dkatz/official_joke_api - ist in Swing)
* im Bsp wird die joke-API in eine APP (Mobile App) integriert
    * es wird zu URL navigiert, dann JSON-Antwort in die APP geparst.
#### 5 - Consume a RESTful API via Postman
* Postman ist Tool um API zu testen
#### 6 - Create a RESTful API
* Bsp in Java mit Spring-Data-Rest-Bib
#### 7 - Document an API
* Swagger - Tool zu Dokumentation der API <- ist Bundle von Open Source Tools, die auf OpenAPI Spezifikation aufbauen
* Swagger Tools:
    * Swagger Editor
    * Swagger UI - erstellt Dokumentation für API
        * man kann mit API kommunizieren, obwohl API noch nicht geschrieben wurde
        * zu Projekt hinzufügen mit Maven-dependency
    * Swagger Codegen

### 3 - Using SOAP-Based Web Services
#### 1 - SOAP overview
* SOAP  - Simple Object Access Protocol ist mehr sicher
* benutzt XML
* SOAP ist ACID-Complaint (Atomicity Consistency Isolation Durability (sowas wie Transaktion in DB))
* WSDL-Dokument - Web Service Desctiption Language - sagt, welche Anfragen an den Server möglich sind / er ausführen kann (beinhaltet mögliche Datentypen + Operationen). Ist Web-Standard von W3C. 
* definiert Regeln für Messagestruktur und Sicherheit
* SOAP Message - hat Struktur oft als HTML:
    1. Envelop (XML-Envelop)
    2. Header (optional z.B Security-Tokens)
    3. Body
    4. Fault (optional) - Fehler die beim Sende der Message passieren können 
#### 2 - History and future of SOAP
* SOAP wird für Enterprise-level Web Services benutz, die viel Sicherheit erfordern z.B PayPal-API
#### 3 - Consume SOAP web service
1. Bsp: www.dataaccess.com/webservicesserver/numberconverions.wso
2. www.dataaccess.com/webservicesserver/numberconverions.wso?WSDL - wsdl-Dokument ansehen
3. Java-Client erstellen:
    1. `wsimport -keep https://www.dataaccess.com/webservicesserver/numberconverions.wso?WSDL` - es werden Java-Classes erstellt in ./webservicesserver, die benutzt werden um den Service zu benutzen
    2. dann nur Java-Client-Main erstellen, der Anfragen macht.
#### 4 - Consume a SOAP web service via SoapUI
* SoapUI - Tool für SOAP wie POSTMan für REST. Kann man einfach downloaden
* Projects erstellen -> Funtional-Tests, Load-Tests usw. erstellen.
+ erstellt SOAP-Anfragen in richtigem XML-Format
+ braucht WSDL-Dokument
#### 5 - Create a web service
* JAX-RX-Lib benutzen
    * mit `@WebService(...)` App zu SOAP machen
    * wie alles in JAX-RS ist alles annotiert
* man muss den Code noch mal anschauen.
* wenn man App startet, kann man WSDL anschauen (wird) automatisch von der SOAP-App erstellt
* man kann die Anfragen mit SoapUI machen

### 4 - Developing APIs using GraphQL
* ist eigentlich weitere alternative zu REST und SOAP
#### 1 - GraphQL overview
* GraphGL - Query-Sprache
* Syntax, die beschreibt, wie Daten angefragt werden sollen. 
#### 2 - The structure of GraphQL queries
* GraphQL lässt Client spezifizieren, welche Daten es braucht, kann Daten von mehreren Sourcen aggregieren
+ erstellt Query-Dockument:
    + String, der an den Server gesendet werden soll, um Daten zu requesten
    + ist nur read-only,
* man kann GraphQL-Anfragen als JSON senden, aber meistens wird RAW-GraphQL-Format benutzt
* GraphQL benutzt Type System, dass aus drei Teilen besteht
    1. Schema - Set von Typn
    2. Queries - Felder der gelieferten Objekte spezifizieren
    3. Resolvers - GraphQL-Operationen zu Daten umwandeln
* jede Query wird ein spezifisches Objekt erhalten, wobei in der Query, kann man die wirklich benötigten Objekte-Felder spezifizieren
* es gibt zwei Sites-Queries:
    1. Mutation - modifiziert Server-Side-Daten
    2. Subscription - Notification, wenn Daten auf dem Server sich verändert haben
#### 3 - Consume a GraphQL API
* Bsp: Yelp-GraphQL-API: *www.yelp.com/developer/graphql* - deren UI um GraphQL-Anfragen zu machen. Man muss sich für yelp-Developer-Programm registrieren
* Request - Response eigentlich auch in JSON-Format
#### 4 - Create a API with GraphQL
* man kann GraphQL auch mit node.js benutzen = GraphQL-Server und GraphQL-Client
    1. Server:
        1. GraphQL-Server = Express.js als GraphQL-API-Server
        2. GraphQL.js mit npm installieren  
        3. Struktur:
            1. Schema: GraphQL definiert Typen, die die Daten beschreiben (GraphQL-Schma-Language), die von GraphQL-API angefragt werden können.
            2. Resolver-Funktion
        * <- man muss eventuall den Code noch Mal anschauen
    2. Client: hier ist dieses yelp-Dev-GraphQL-UI