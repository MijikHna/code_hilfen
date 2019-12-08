### 2 - Requests and Responses
#### 1 - The requests/response pair
* User Engines - Browser
#### 2 - Anatomy of a URL
* URL = Protocol+URN
    * URN - wo die Resource
        * Host - Domain
        * Port (Invisible) <- aus Protocol abgeleitet
        * Resource/Source
        * URL query nach *?* z.B User-ID zu tracken
#### 3 - HTTP methods
* Methode = Verb
    1. GET - Resource bekomen;  (eventuell Authoritaion-Header (Username + Password) +Cookie mit Authentikationtoken) Success: OK (200) oder Failure (40X)
    2. POST - neue Resource erstellen; braucht Authorisation-Header; Success: Created(201) oder Failure (40X)
    3. DELETE - Deletes Resource; braucht Resource-ID; Server kann die Resource als Deleted markieren oder tatsächlich löschen Success: OK (200) oder Failure (40X)
    Diese Drei werden meistens benutzt
    4. PUT - Update Resource; braucht Authorisation Header + Resource-ID der Resource + neue Content; Success: OK (200) oder Failure (40X)
    5. PATCH - Modifiy Resource + wie; braucht Authrisation + Resource-ID; Success: OK (200) oder Failure (40X)
    6. HEAD - nur HEAD des Response leifern
    7. OPTIONS - liefert Methoden, mit denen man mit dem Server kommunizieren kann
    8. TRACE - erstellt Loopbak für die requested Message
* jedes Verb hat eigenes Request/Response-Pair
#### 4 - HTTP status messages
1. 1XX - Information (Status des Servers)
    * 
2. 2XX - Success
    * 200 - OK
    * 201 - Created
    * 204 - NO Content
3. 3XX - Redirection
    * 301 - Moved permanently
    * 302/303 - Found at this other URI
    * 307 - Temporary redirect
    * 308 - Permanently
4. 4XX - Client Error
    * 400 - Bad request
    * 401 - Unathorized
    * 403 - Forbidden
    * 404 - Not found
    * 405 - Method not Allowed 
5. 5XX - Server Error
    * 500 - Internal server error - 
    * 502 - Bad gateway - Server ist Gateway oder Proxy und hat NO Response vom richtigem Server mit dem Service bekommen.
    * 503 - Service unavailable - Server overloaded usw
### 3 - HTTP headers
#### 1 - What are HTTP headers
* Headers haben Informationen über den State des Browsers. Senden diese Info mit Request/Response
* Info zwischen Server und Client austauschen
+ Bsp Info in Header:
    * `Authorization: Basic afjpwerdj` - hat Username und Password, Base64 encoded
* Cookie-Sets um States z.B welcher Film gerade geschaute wird, Server sendet an Client Cookie mit dieser Info. Client sendet dann diese Cookie zurück, um zum alten State zurückzugehen. 
* Server kann Cache-Header senden, dann wird Inhalt gecached (wie lange, wann expired usw.) `Cache-Control: max-age=x`
* HTTP2 hat weitere Teile im Headers
#### 2 - How to see HTTP headers
* mit Entwicklertools anschauen
* Bsp: https://mor10.com
* ganzes Web ist großes RESTful API => Rest Client benutzen um damit zu kommunizieren
    * Rest Client -> Postman, Erweiterung in vscode
        * GET/HEAD https://mor10.com/gutenberg-and-the-future-of-wordpress-conditions-for-success/
#### 3 - Anatomy of a request header
* Header kann z.B beim POST zusätzliche Daten haben: Formular-Inhalte, Upload-Daten usw.
#### 4 - Ananoty of a response header
* 
#### 5 - Coookie
* Sessions werden auch im Cookies gesetzt
* Bsp:
    1. Login Formular
    2. Cookie, das unique token oder string hat, wird als Resonse gesendet und speichert diesen String in eigenen DB
    3. nächster Request an den Server hat dann den Cookie im Request-Header. 
#### 6 - Caching
* Cached files werden vom Server nicht überschrieben
+ im *Cache-Control-Header* stehen Cache-Optionen. werden sowohl im Request als im Response benutzt
* Cache-busting - Technik gegen Cachen, Jeder Datei hat unique Name