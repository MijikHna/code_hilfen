### 0 - Introduction
* JAX-RS ist Annotation-Driven
* JAX-RS ist als Maven-Packet paketiert
* exirsice files: start -> end
### 1 - JAX-RS 2.0
#### 1 - JAX-RS 2.0 introduction
* JAX-RS = Implementation von REST in java
* ist Annotations Driven:
    * @Path - Root resource Annotation
    * @POST/@GET - HTTP request Methoden
    * @QueryParam, @PathParam - Query und Path Variablen ansprechen
    * @Consumes/@Produces - Content Type Annotationen
    * es gibt Mehr Annotation
#### 2 - REST introduction
* URL + Http-verb + Http-body = REST
* => man kan CRUDs auf HTTP-Verben mappen
    * Create -> POST
    * Read -> GET
    * Update -> PUT
    * Delete -> DELETE
* HATEOAS -> beim Antwort auch weitere verfügbare/erlaubte Links mitgeben

#### 3 - Headline features of JAX-RS 2.0
* JAX-RS kann man mit Provider erweitern. Provider = Klasse die JAX-RS-Interface(-s) implementiert. 3 Typen
    1. Entity - zum Mappen 
    2. Context - 
    3. Exception mapping providers

### 2 - Introduction to Bookshop Application
#### 1 - Bookshop application demo
* Bsp App - Bookshop:
    1. Server App - aus drei pacakges
        * domain - Entitys
        * infrastracture - Repositorys für Buch und Autor
        * rest - Ressourcesn
    2. Client App - besteht aus drei packeten
        * domain - domain-Object die auch auf dem Server vorhanden sind, zum mappen
        * beans - für Views für Beans
        * restclient
* Fazit:
    * hier wird komplette Web-Anwendung in REST implementiert
#### 2 - Deployment demo
* Das ganze Project ist Maven Project
    * Benutzte Plugins:
        * *cargo* (codehaut-cargo)
* in Terminal zu Maven-Datei gehen = **pow.xml** und ausführen `maven clean package cargo:run` <- man muss für beide für client und server machen = Server und Client Appications werden deployed
* Postman zum Testen der API benutzt - muss man auf dem Rechner installieren

### 3 - Create a REST Resource
#### 1 - Define the REST contract
* zwei Ressourcen: book, author
* Application routed: /rest-sever
* Application path at /api
* => REST API /rest-server/api => localhost:xxxx/rest-server/api
    * Book Ressource => /books => rest-server/api/books
        * REST-Methoden
            * POST /books => URI um Buch zu erstellen
            * POST /books/:isbn => dem Buch isbn hinzfügen
            * GET /books
            * GET/books/:isbn
            * PUT /books/:isbn
            * DELETE /books/:isbn
            * GET /books/:isbn/authors
    
    * Author- Ressource /authors => => rest-server/api/authors
        * GET /authors 

#### 2 - Inheritance or XML configuration
* URI: localhost:xxxx/rest-server/api/books
    * localhost:xxx - Domain
    * /rest-server - Context Root
    * /api - Base URI
    * /books - Ressoursename
* man kann *base URI* auf zwei Arten configurieren
    1. Inheritance
        * Subclasse erstellen die inherits von java.ws.rs.Application und die @ApplicationPath("/api") - Annotation hat
        ```java
        @ApplicationPath("/api")
        public class RESTConfig extends Applicaton {
            //...
        }
        ```
    2. web.xml - XML-Configuration
        + URL-Pattern für servlet Mapping definieren in web.xml
        ```xml
        <servlet-mapping>
            <servlet-name>
                javax.ws.rs.core.Application
            </servlet-name>
            </url-pattern>/api/*</url-pattern>
        </servlet-mapping>
* mögliche URLs:
    * /api
        * /books
            * @GET/
            * @GET/{isbn}
            * @POST/
        * /authors
            * @GET/
            * @GET/id/{id}
            * @POST/
* man muss Klassen impementieren, die Ressourcen und die Methoden repräsentieren
* man muss mindestens **Root resource**-Klasse definieren, die auf die Ressource und CRUD implementiert
* man sollte getrennte **Root ressource**-Klasse für selbständige Ressource erstllen
    * Book - Ressource
    ```java
    @Path("/books")
    public class BookRessource{
        //
    }
    ```
    * Author - Ressource
    ```java
    @Path("/authors")
    public class AuthorRessource{
        //
    }
    ```
    * <- hier fehlen noch REST-Methoden
#### 3 - Define the API root
```java
@Application("/api")
public class RESTconfig() extends Application(){

}
```
* package rest erstellen
```java
@Stateless //Stateless Klasse
@Path("/books")
public class BookRessource{

}
```
```java
@Stateless //Stateless Klasse
@Path("/authors")
public class AuthorRessource{

}
```
#### 4 - Create the resource  entity
* Ressource Entity kann sein POJOs oder JPA
* JAXB XML binding - Bib um XML zu seralizieren
    * `@XmlRootElement`
```java
@XmlRootElement
public class Book{
    public string id;
    public List<Authors> authors;
}
```
* package für Entities erstellen *domain*
```java
@XmlRootElement
public class Book implements Serializable{
    private String id;
    private tring title
    private List<Authors> authors;
    private String descriotion;
    private Float price;
    private Stirng imageFileName;
    private String link;
    private Date published; 

    //getter + setter generieren
    //equals + hashCode generieren
    //Konstruktor generieren - man muss auch Konstruktor ohne params erstellen, sonst failed Serialization
```
* das gleiche für Author
```java
@XmlRootElement
public class Book implements Serializable{
    private String id;
    private tring firstName
    private String lastName;
    private Stirng blogUrL;

    //getter + setter generieren
    //equals + hashCode generieren
    //Konstruktor generieren - man muss auch Konstruktor ohne params erstellen, sonst failed Serialization
```
#### 5 - Create the resource methods
* die Methoden mit @GET/@POST/usw annotieren, die bei dem Method ausgeführt werden sollen
```java
@Path("/books")
public class BookRessource{

    @GET
    public Response getAllBooks(){}
}
```
* für Books:
```java
@Path("/books")
public class BookRessource{
    
    private BookRepository bookRepository //<-ist diese map

    @GET
    public Response getAllBooks(){
        //hier werden Books in Map gespeichert => aus dieser Map die die Books holen
        List<Book> books = bookRepository.getAll();
        GenericEntity<List<Book>> bookWrapper = new GenericEntity<List<Book>> (books){};
        //Response bilden => wird HTTP-Seite
        return Response.ok(bookWrapper).build(); //ok = 200
        //return Response.status(Response.Status.OK) usw <- weitere Möglicher Responses liefern
    }

    @POST
    public Reponse saveBook(final Book book){
        Book persistedBook = bookRepository.saveBook(book);
        return Response.ok(persistedBook).build();
    }
    //man muss noch HTTP-accept und Content-Type definierern damit alles funktioniert
}
```
* <- Rückgabetyp ist **Respons** spezielle Wrapper-Object
#### 6 - Path parameters
* Path-Variablen abrufen = z.B ID die mit URI mitgegeben werden
* mit `@Path("/{id}")` und `@PathParam("id")`
```java 
@GET
@Path("/{id}")
public Response getAllBooks(@PathParam("id") String id)
```
* <- dabei können Konfikte erstellen mit ähnlichen URIs
* => RegEx benutzen um richtige Funktion aufzufen
    * `@Path("id: \\d{9}[\\d|X]$")`
#### 7 - Add path parameters
* weiter in **BookResource**
```java
@GET
@Path("{isbn: \\d{9}[\\d|X]$}")
publc Response getBookByIsbn(final @PathParam("isbn") Stirng isbn){
    Optional<Book> book bookRepository.getByISBN(isbn);
    if (book.isPresent(){
        return Response.ok(book.get().build());
    })
    return Response.noContent().build();
}
```
* wetiere Parameter-Annoationen
    * @QueryParam - QueryParameer aus URI extrahieren
    * @CookieParam - Cookie wert extrahieren
    * @FormParam - Form Daten extrahieren
    * @HeaderParam - HTTP header Werte extrahieren
    * @MatrixParm - Matrix Daten aus URI extrahieren
#### 8 - @Consumes and @Produces
* Methoden können Content erstellen oder konsumieren => @Consumes und @Produces
    * erstellen z.B JSON oder XML => mit diesen Annotationen Media-Typ festlegen 
        * `@Consumes(MediaType.APPLICATION_JSON)` => in HTTP-header: Content-type:application/json
        * `@Produces(MediaType.APPLICATIN_JSON)` => in HTTP-header: Accept: application/json
#### 9 - Add the media types
* weiter in **BookResource**
```java 

@GET
@Produces(MediaType.APPLICATION_JSON)
public Response getAllBooks(){
    List<Book> books = bookRepository.getAll();
    GenericEntity<List<Book>> bookWrapper = new GenericEntity<List<Book>> (books){};
    return Response.ok(bookWrapper).build()
}

@POST
@Produces(MediaType.APPLICATION_JSON)
@Consume(MediaType.APPLICATIN_JSON)
public Response saveBook(fianl ){
    Book persistedBook = bookRepository.saveBook(book);
    return Response.status(Response.Statsu.OK).entity(persistedBook).build();
}

@GET
@Produces(MediaType.APPLICATIN_JSON)
@Path("{isbn: \\d{9}[\\d|X]$}")
publc Response getBookByIsbn(final @PathParam("isbn") Stirng isbn){
    Optional<Book> book bookRepository.getByISBN(isbn);
    if (book.isPresent(){
        return Response.ok(book.get().build());
    })
    return Response.noContent().build();
}
```
* testen
    *  da Maven verwendet => in ./rest-sever gehen
    * `maven clean package cargo:run`
* <- es wird über Maven Glasfish-Server installiert
* und mit Postman testen
#### 10 - Challenge/Solution: Add resource methods

### 4 - Response and HATEOAS
#### 1 - The HTTP response
* REST sollte die richtigen Response-Codes senden
    1. per Default senden lassen
    2. per Configuration senden lassen
* Response-Code ist wrappen in diesem Response-Objekt
* wenn man ohne Response sendet => JAX-RS entscheidet selbst welchen Code er setzt.
* wenn Response ist NULL => 204, sonst 200
#### 2 - Build a response
* für komplexe API sollte man *ResponseBuilder* benutzen. Response-Klasse benutzt *ResponseBuilder* wenn es diese Funktionen `.ok()`, `status()` aufruft.
    * Bsp für Response Codes:
        * `Response.status(204).build();` oder `Response.noContent().build();`
        * `Response.status(202).build();` oder `Response.accepted().build();`
        * `Response.ok(book).build();` - setzt auf 200 und Body zu book
        * `Response.accepted(book).build();`
* Bsp: Alles selbst setzen: 
    * `Response.status(Response.Status.OK).language(Locale.CHINESE).type(MediaType.APPLICATION_XML).header("Custom_Header, "Value").build();`
* eventuell muss man Response selbst setzen, da Response Probleme mit Gerenischen Typen als Body hat (dafür bietes JAX-RS Klasse `GeneriyEntity`)
* eventuell muss man die Cookies zu Response hinzufügen (javax.ws.rs.core.NewCookie)
#### 3 - How to handle errors
* 4 Möglichkeiten auf Exceptions zu reagieren
    1. vom Java alles machen lassen -> von von servlet Layer behandelt => 500 Server Error
    2. Excepitions catchen -> try-catch (doppelter Code)
    3. Wrap Exseptions in WEb-App und es mit JAX-RS behandeln -> mit WebApplicationException-Klasse behandeln. Eigentlich auch try-catch, aber im Catch wird `throw new` gemacht und `WebApplicationException(...)` aufgerufen (doppelter Code)
    4. Manager Exception mit Exception Manager -> Exception Manager implementieren
#### 4 - Implements an exception manager
```java
@Provider //
public class ISBNExceptionNotFoundManager implements ExceptionManager<ISBNNotFoundException>{
    @Override
    public Response toResponse(ISBNNotFoundException exception){
        return Response.status(Response.Satutus.NO_CONTENT).build();
    }
}
```java
@GET
@Produces(MediaType.APPLICATIN_JSON)
@Path("{isbn: \\d{9}[\\d|X]$}")
publc Response getBookByIsbn(final @PathParam("isbn") Stirng isbn){
    Optional<Book> book bookRepository.getByISBN(isbn);
    if (book.isPresent(){
        return Response.ok(book.get().build());
    })
    //return Response.noContent().build();
    throw new ISBNExceptionFoundException();
}
```
* code in BookRessource ändern, sodass es diese Exception wirft
#### 5 - Work with HATEOAS
* 2 Möglichkeiten zu implementieren
* HATEOAS = Navigieren mit URIs
    * d.h. Response liefert Liste mit URIs die weitere Operationen erlauben
* Bsp json
```json
"links": [
    {
        "rel": "delete", //Relationship = kleine Bescheibung 
        "href": "http://../../",
        "type": "DELETE"
    }
]
```
* mögliche Relationships:
    * next, privious für Navigation
    * self für Aktion auf aktuelle Ressource
    * ressourceName = all
* Client sollte diese Links verstehen und verarbeiten können
#### 6 - HATEOS and JAX-RS
* 1 Möglichkeit -> Links zu Ressourcen in JSON
```java
public abstract class Hypermedia {
    private List<LinkRessource> links = new ArrayList<>();
    //getters + setters
}

public class LinkResource{
    private String rel;
    private String type;
    private URI uri;
    //getters + setters
}


Link delete = Link.fromUri(uriInfo.getBaseUriBuilder.path(getClass()).path(getClass(), "deleteBook").build(book.get().getId())).rel("delete")
book.get().addLink(new LinkRessource(delete))
```
* 2 Möglichkeit -> in HTTP-Header
```java
@Context
private UriInfo uriInfo;
Link delete = Link.fromUri(uriInfo.getBaseUriBuilder.path(getClass()).path(getClass(), "deleteBook").build(book.get().getId())).rel("delete").type("DELETE").build(); //Link erstellen

Response rep = target.request(MediaType.APPLICATION_JSON).get();
Set<Link> links = rep.getLinks(); //links dem Header hinzufügen
```
#### 7 - HATEOAS to the resource
* in domain 
```java
@XMLRootElement
public class LinkRessource{
    private String rel;
    private String type;
    private URI uri;

    //getter + setter
    //Konstruktor
    public LinkRessource(Link link){
        this.rel = link.getRel();
        this.type = link.getType();
        this.uri = link.getUri();
    }

    public LinkRessource(){}
}

public class Hypermedia(){
    private List<LinkRessource> links = new ArrayList();

    public void addLink(LinkRessource linkRessource){
        this.links.add(linkRessource);
    }
    // auch getLinks(), setLinks, deleteLinks()
}

//alle Entititys (Book, Author) sollen extend Hypermedia

//BookRessource dann

@Content
private UriInfo uriInfo;

@GET
@Produces(MediaType.APPLICATIN_JSON)
@Path("{isbn: \\d{9}[\\d|X]$}")
publc Response getBookByIsbn(final @PathParam("isbn") Stirng isbn){
    Optional<Book> book bookRepository.getByISBN(isbn);
    if (book.isPresent(){
        //links erstellen
        Link self = Link.fromUri(uriInfo.getBaseUriBilder()
            .path(getClass())
            .path(getClass(), "getBookByIsbn") //getBooByIsbn = Funktionsname
            .build(book.get().getId()))
                .rel("self")
                .type("GET")
                .build();
        Link delete = Link.fromUri(uriInfo.getBaseUriBilder()
            .path(getClass())
            .path(getClass(), "deleteBook") //getBooByIsbn = Funktionsname
            .build(book.get().getId()))
                .rel("delete")
                .type("DELETE")
                .build();
        LinkRessource selfLink = new LinkRessource(self);
        LinkRessource deleteLink = new LinkRessource(delete);
        book.get().addLink(selfLink);
        book.get().addLink(deleteLink);

        return Response.ok(book.get()).links(self, delete).build());
    })
    //return Response.noContent().build();
    throw new ISBNExceptionFoundException();
}
```
#### 8 - Challenge/Solution: Add exception handlers

### 5 - Bean Validation API
#### 1 - Bean Validation introduction
#### 2 - Work with Bean Validation
#### 3 - Manage validation failures
#### 4 - Implement validation failure management
#### 5 - Challenge/Solution: Add validation annotations

### 6 - Create a REST Client
#### 1 - Make a request
* JAX-RS bietet REST-Client an
    * dabei kann jedes REST-API konsumieren
    * => nur richtige URI erstellen bzw. HTTP-Request 
```java
Client client = ClientBuilder = ClientBuilder.newClient();
client.target("http://...").request(MediaType.APPLICATION_JSON).get();

client.close();
```
* ResponseKlass hat ein paar Methode zum Lesen von Ressourcen
    * `readEntity(Class<T>)` - liest Resource, die in Response eingepackt ist
    * <- oder JsoObject-Bib benutzen
#### 2 - Implement a client
```java
public class BookServiceImpl{
    //das ganze Client-Ding ist über Eigenschaften und init() realisiert
    //Client client = ClientBuilder = ClientBuilder.newClient();
    //client.target("http://...").request(MediaType.APPLICATION_JSON).get();
    //client.close();

    public List<Book> getBooks(){
        WebTarget target = client.target(BOOKS_ENDPOINT);
        Response response = target.target(MediaType.APPLICATION_JSON).get();

        //aus Response Books holen
        cacheBooks = response.readEntity(new GenericType<ArraylList<Book>>(){});
        return Collections.unmodifiableList(cacheBooks);

    }
}

```
#### 3 - Process the response with JSONP
#### 4 - Use JSONP
#### 5 - HATEOAS and the frontend
#### 6 - Implements HATEOAS
