### Introduction:
* Seite ist ein Template, das dann Request an REST-API sendet. RESt-API sendet JSON, die Seite interpretiert diese und zeigt an.

### 1 - REST API: Representaion State Transfer Application Programming Interface
* Client sendet Requst (mit ID) mit Format, REST such nach diesen Daten, formatiert entsprechend und gibt sie zurück.
* Client sendet Veränderung, REST verändert und sendet Veränderung + Status der Änderung
#### 1 - The RESTful librarian
* REST - Reprentational State Transfer. 
#### 2 - What is a REST API?
* Web Application:
    * jede Seite repräsentiert Current State of View.
    * Beim ersten Besuch der Seite wird erstmal alles Heruntergeladen. Die App sendet, dann URI mit dem Nächsten State und mit empfangenen Daten, wird next State of View gebildet (Requests: Modify, Replace, Delete)
    * REST sendet Data Objects und nicht ganze Seite. App updatet die Daten und nicht die ganze Seite
* REST API ~ Sprache für REST
#### 3 - Sidebar: URL vs. URI?
* URI - Universal Resource Identifier - identifieziert abstrakte oder physische Resouce
* URL - Universal Resource Locator - Teil von URI + beschreibt, wie man die Resource erreicht (http://, ftp://)
* URN - ist Teil von URI, kann auch URN sein
#### 4 - The six constraints of REST
* Sechs Teile von REST:
    1. Client-Server Architecture
        * 
    2. Statelessness
        * Client Context (state) wird nicht auf dem Server gespeichert. Client speichert selbst eigenen State
    3. Cacheability
        * alle REST-Responses müssen als cacheable oder uncacheable markiert werden 
    4. Layered System
        * 
    5. Code on demand
        * 
    6. Uniform interface
        1. Resource identification in request - URI-Request spezifieziert welche Resource und in welchem Format
        2. Resource manipulation through representations - Client kann die Resource modifizieren oder löschen (Client sagt, was auf dem Server gespeichert werden soll)
        3. Self-descriptive messages - jede Representation soll eigenen Data Format beschreiben
        4. Hypermedia as the engine of application state - Client sollte alle verügbaren Resourcen und Methoden durch Hyperlinks bekommen (REST Service beschreibt alle möglichen Resourcen in jedem Response)
#### 5 - How REST relates to HTTP
* REST API ist durch Web erreichbar mit HIlfe des HTTP-Protokols, muss aber nicht unbedingt HTTP sein, (z.B FTP usw.). RESTful API = über HTTP
#### 6 - Who or what interacts with REST APIs?
* meisten REST API haben Limits, wer, wieviel was machen kann.
#### 7 - Tools to see REST API in action
* https://reqres.in/ - Live RESTful-API Server
    * https://reqres.in/api/users - GET
    * Rest Client in vscode installieren: Rest Client von Huachao Mao

### 2 - Request
#### 1 - Anatomy of a REST request
* Rest Request hat zwei Teile:
    1. Methode: GET/POST/PUT/PATCH/DELETE/OPTIONS/HEAD
    2. URI: https://restfull.dev/posts/5
* Bsp: Liste von most recent Posts auf einer WordPress seite -> `GET https://site.com/wp-json/wp/v2/posts`. Man kann auch Request Metadaten in Header mit angeben z.B:
    * `HOST: appsite.tv`
    * `Content-Type: application/json`
    * `Authrization: Basic adfafeurha`
    * `Cache-Control: no-cache`
* Bsp: POST-Request mit Update bzw. New Entry
```
POST /wp-json/v2/posts HTTP/1.1
HOST: appsite.dev
Authorization: Basic Morten pass
Content-Type: application/json
Cache-Control: no-cache
#Daten 
{
"titel": "Tralala",
"content": "Tralala",
"author": 10,
}
```
* im Code wird JS für die Request verwendet:
```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://site.com/wp-json/wp/v2/posts", true)
xhr.onload = function(){
    console.log(xhr.responseText)
}
xhr.send()
```
ODER Ajax:
```javascript
$.ajax({
    url: "https://site.com/wp-json/wp/v2/posts",
    type: "POST",
    data: {
        title: "Tralala",
        content: "Tralala",
        author: "10,
    }
    success: function(response){
        console.log(response);
    }
});
```

#### 2 - Discovery
* welche Resources und Methoden in der REST-API verfügbar sind (REST API untersuchen)
* GET und OPTIONS benutzen
* OPTIONS:
    * liefert im Header z.B `Access-Control-Allow-Methods: GET,HEAD,PUT,PATCH,POST,DELETE`
    * `OPTIONS http://restful.dev/wp-json/wp/v2/posts` - liefert JSON in dem steht, welche Methoden auf welche Resource angewendet werden
* ABER besser Doku lesen
#### 3 - Resource
* ist Mapping zu einem Set der Einheit (z.B rotes Buch im Regal Nr. 4). Kann auch eine Collection sein (alle roten Bücher) - in Web z.B bookcase/books/red/cubby
* Representation - current oder intended State der Resource (Kopie der Resource, die für bestimmte *Mashinen* angepasst wird z.B json, cml)
#### 4 - Methods (Verbs)
* GET - 200 oder 404
* POST, PUT, PATCH - Daten an den Server senden
    * POST - auch in non-Rest Szenarien benutzt, z.B Form-Input senden. Oft neue Resource erstellen z.B etwas Adden. 201 - Created oder 401,409,404
    * PUT - Daten updaten, braucht ID der Resource + neuen Content. Eventuell Resource wird erstellt, falls nicht vorhanden. 200 oder 401, 404, 405. Replaced Content
    * PATCH - Daten updaten + wie die Daten ersettzt werden d.h. damit kann nicht ganzer Eintrag/Resource ersetzt werden, sondern nur ein bestimmter Teil
* DELETE - Daten/Resource löschen. 200 oder 401, 404
* OPTIONS - gibt Beschreibung der möglichen Kommunikation für die Resource
* HEAD - 200 oder 404

### 3 - Response
#### 1 - Response header
#### 2 - HTTP status messages
* Gruppen:
    * 1xx - Information. Client informieren z.B. ich bearbeite deinen Request
    * 2xx - Success. 
    * 3xx - Redirection 
    * 4xx - Client Error
    * 5xx - Server error
* Wenn man eigene Redirections implementieren soll in der eigenen RESTful API, dann muss man selbe entscheiden welche 3xx man benutzt
#### 3 - REST and Authorization/Authentication
* Antwort von REST hängt vom Authorisationlevel ab. Meisten RESTfuls haben leveled access d.h. User können limitierte GET/HEAD/OPTIONS Requests machen. Manche User können POST und wenige können PUT,PATCH,DELETE. 
### 4 - Request/Response Pairs
#### 1 - Request/response pairs
#### 2 - GET
* Bsp:
```
GET http://restful.dev/x/y/posts
Authorization: Basic username myPassword

GET http://restful.dev/x/y/posts?per_page=1
Authorization: Basic username myPassword
```
#### 3 - POST
* Bsp: 
```
POST http://restful.dev/x/y/posts
Authorization: Basic username myPassword
Content-Type: application/json

{
    "title": "Tralal",
    "content": "Tralala",
    "satatus": "publish", # sonst wird automatisch zu DRAFT
    "author": 1 # sonst wird Author der Inhaber der Seite
}

GET http://restful.dev/x/y/posts
Authorization: Basic username myPassword
Content-Type: application/json
```
#### 4 - PUT/PATCH
* Bsp:
```
POST http://restful.dev/x/y/posts/15
Authorization: Basic username myPassword
Content-Type: application/json

{
    "title": "Tralala"
}
```
#### 5 - DELETE
* Bsp:
```
DELETE http://restful.dev/x/y/posts/15
Authorization: Basic username myPassword
```
* oft wird nicht deleted, sondern status z.B auf *trash* gesetzt
```
* um endgültig zu delete zuerst mit OPTION alle Methoden und deren Optionen anzeigen
DELETE http://restful.dev/x/y/posts/15?force=true
Authorization: Basic username myPassword
```