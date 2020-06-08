#### Development:
1. JDK 8 oder höher
2. IDE + Maven => Inteliji
3. Web Browser
4. Postman

### 1 - Understanding Java Persistence API (JPA)
#### 1 - What is persistence
* App ist eigenlicht über bzw. zugreifen auf Data -> DB
* Persistence = Beständig = Info/Daten, die auch bestehen, wenn App die diese angelegt hat nicht mehr läuft. Also man persist/lässt fortbestehen, um später die Daten retrieven/abrufen , processen, tranformieren und analysieren.
* Storage Optionen:
    * DB
    * NoSQL = JSON
    * Files
* JPA = DB auf Java-Objekte Mappen
#### 2 - Object relational mapping (ORM)
* ORM = Object relational mapping 
* ORM = OOP-Obj zu DB-Rows mappen, Kommunikation dafür um es zu realisieren, diese Kommunikation übernimmt JPA
#### 3 - JPA overview
* Hibernate = Instanz-Provider für JPA
* es gibt mehrere JPA-Spezifikationen
* Annoation = JPA-Metadaten um Mapping zu realisieren
* JPA ist Abstraction-Level auf JDBC (Java DB connectivity)
* eigentlch ist JPA eine Colletion von Interface => müssen selbst implementiert werden = Instance-Provider. Momentan gibt es 4 JPA-Implementationen:
    1. EclipseLink
    2. Hibernate
    3. OpenJPA
    4. Data Nucleus
* Mapping ist via Persistence Metadata definiert. JPA benutzt diese Metadatan um DB-Operationen auszuführen
#### 4 - JPA configuration and entities
* Zwei Wege JPA Metadaten zu definieren:
    1. Annotations:
        * `@Entity` - Objects, die in DB leben und zu DB-Tabelle gemappt werden können + `@Table(name="TabelleName")`
        * `@Id` -> `@Id`
        * `@Table`
        * `@Column` -> `@Column(name="ZeilenName", nullable = false)
        * `@Generated Value` -> `@GeneratedValue(strategy = GenerationType.Auto)`
    2. in persistence.xml als XML
* man kann auch beide kombinieren
* XML-Metadaten überschreiben Annotationen
+ EntityManager kann dann über Metadatan die Entities zu Objects mappen. EntitiyManager macht dann create, delete, update usw.
* EntityManager handelt meisten SQL-Operationen ohne zusätzlichen Code zu schreiben
+ JPQL = Java Persistence Query Language = SQL-Anfragen mit OOP-Sprache. ist Layer auf SQL => Sprachen sind ähnlich:
    * SQL `select * fromt TabName where lala < 60`
    * JPQL `select t from TabName t where t.lala < 60` 
* Also Vorteil von JPA:
    1. kein JDBC-Code
    2. kein SQL-Code
#### 5 - Benefits of JPA over pure JDBC
* JDBC = Low Level API
    1. DB-Verbindung
    2. SQL-Code an DB senden
#### 6 - Looking at the course project
* Project: Trackzilla = App zum Bugtracking. Spring-based App
    1. Domain
    2. Service
    3. DB
* => wahrscheinlich ExersiceFiles herunterladen
* ist RESTful-App
#### 7 - Review course project tools
* localhost:8080/console - DB-Console wie z.B phpadmin (als DB wurde H2 benutzt)
    * Driver Class: org.h2.Driver
    * JDBC URL: jdbc:m2:mem:bugtracker
    * User name: sa
    * Password: leer
### 2 - Managing Entities with EntityManager
#### 1 - EntityManager
* JPA Configuration:
    * in persistence.xml gemacht
        1. Caching
        2. welcher Operationen erlaubt
        3. Data Sources
        4. usw.
        5. Driver usw.
* EnitityManager = perfomt CRUD (crate, read, update, delete)-Operatioen auf DB
* JPA Concept:
    1. `Persistence` erstellt einen oder mehrere `EntityManagerFactory`
    2. einer `EntityManagerFactory` wird von einer `Persistence Unit` konifiguriert
    3. `EntityManagerFactory` erstellt dann einen oder mehrere `EntityManager`
    4. ein `EntityManager` managet einen `Persistence Context`
* `Entities` werden von `EntityManager` gemanaged.
    * solange es keinen `EntityManager` für `Entity` gibt => ist diese `Entity` = Play Old Java Object (POJO) und ist in `Detached State`
    * wenn `EnityManager` die `Entity` verwaltet => in `Managed State`
* zum Code:
    1. mit `@PersistenceContext` EntityManager in DAO-App (Data Access Object) injecten von EntityManagerFactory d.h. sichergehen, dass es nur einen EM gibt = Transactional/Shared Entity Manager
    ```java
    public class AppDAO implements IApplicationDAO{
        @PersistenceContext
        private EntityManager entityManager;
    }
    ```
* Doku zu EntityManager API schauen
#### 2 - Creating object
* Aufbaue der App:
    1. Controller empfängt HTTP-GET/POST (in diesem Fall POST) und ruft Service-Methode auf
    2. Service -> hat Attribute ApplicationDIA, die dann CRUD-Sachen macht
    3. ApplicationDAO hat dann EntityManager
#### 3 - Persisting Objects
* Code zum erstellen des Obj.
```java
public void addApplication(Application application){
    entityManger.persist(application); 
}
```
* bevor `persist()` war es nur ein Obj, danach es wird zu Managed Entity d.h. wird permanent in DB geschrieben.
* 2 Wege zu testen
    1. Unit-Tests
    2. mit POSTMAN
#### 4 - Reading objects
* = mit EntityManager Entity finden, die schon persist to DB ist
* => Find Methode: `<T> T find(Class<T> enttityClass, Object primaryKey)`
    * man kann auch statt nach primaryKey nach etwas andrem Suchen
* Bsp: `service/ApplicationDAO.java
```java
getApplicationById(int ApplicationId){
    return enntityManager.find(Application.class, applicationId)
}
```
* Unit-Test laufen `findApplication()`
* mit POSTMAN GET-Anfrage ausführen
* APP in Browser ausprobieren
#### 5 - Updating objects
* Update passiert, wenn man Object in Java-APP ändert
* es gibt keine update-Methode in EntityManager
* Bsp: ApplicationDAO.java
```java
updateApplication(Application app){
    //Schritt 1 - Entity finden
    Application app = getApplicationById(app.getId());
    //Schritt 2 - Attribute ändern
    app.setName("lala");
    // weitere Änderungen
    entityManager.flush(); 
}
```
* `entitiyManager.flush()` - synchronisiert Obj (persistents Context = Set der managed Entities) in DB und im Programm
#### 6 - Deleting objects
* Schritte zum Deleten:
    1. remove-Methoden: `void remove(Object entity)`
        * Exceptions: 
            1. `IllegalArgumentException`
            2. `TransactonRequiredException`
* Bsp: ApplicationDAO.java
```java
deleteApplication(int appID){
    entityManger.remove(getApplicationById(appID));
}
```
* es wird aus DB gelöscht + aus managed Entities ausgetragen

### 3 - Transaction Managemet
#### 1 - Entity life cycle
* Entity Lifecycle = sind Entity-Events:
    1. Persisting
    2. Loading
    3. Updating
    4. Removing
* Unterschied zu normalem Java-Obj: wird nicht zusätzlich zu GarbageCollector auch vom EntityManager verwaltet
* Entity States:
    1. Managed = unter Kontorlle von EntityManager
        1. wenn mit Obj mit `new` erstellt = Regular Java Obj. = in Transient- (new-)State
        2. wenn persistened oder von DB geladen = in Managed-State
        3. in Removing State = wenn `remove()` aufgerufen wurde = wird **zur Deletion** markiert
        4. Final State = = Detachted State -> wenn Obj.removed oder flushed oder committe wurde -> dann wird GC das Java-Obj zerstören
    2. Detached = final LifeCycle-State
* 
#### 2 - Managing transactions overview
* Java Transaction API + `@Transactional`
* Transaction (`em.getTransation()`) = mehrere Operationen als Unit ausführen => alle werden ausgeführt oder durchfallen:
* Schritte:
    1. `EntityTransaction emTransaction = em.getTransaction()`
    2. `emTransaction.begin()`
    3. Objekte erstellen, verändern usw.
    4. `em.flush()`
    5. `emTransaction.commit()`
* Java Transaktion API erlaubt:
    1. Transaktionen starten
    2. Transaktionen commiten
    3. Transaktionen rollbacken
* einfach `@Transactional` an Klasse oder Methode anhängen
#### 3 - Managing transaction demo
* Bsp: Java Transaction API
```java TicketDAO.java
@Transactional
class TicketDAO{

    addTicket(Ticket ticket){
        em.persist(Ticket)
    }
}
```
* mit `@Transational` es wird Logic für die Klasse für Tranactional nach + vor der Klasse eingefügt
#### 4 - Advanced mapping using annotations
* man kann Default-Mapping = Annotationen anpassen
+ `@Entity public/protected ... {}` - Klasse als JPA-Entity definieren. + muss `@Id`-Attiribute haben
* Mapping Java-Obj zu DB - Default-Strategien:
    1. über Configuration by Exception
    2. Convention over configuration
* Default Strategie benutzt Persistence Provider
* Default Mapping Rules:
    1. Entity-Name = Table name
    2. Id = Primary Key
    3. Attributes = Columns
        * String -> varchar(255)
        * Long -> BIGINT
        * Boolean -> SMALLINT
* Customization => durch @Annotationen
* ab Java 8 werden auch `Date` und `Time` - Typen richtig gemappt => man muss nicht eigene Converter schreiben (hier im Bsp wurde `LocalDate`)
* mit `@Transient` = Attribut vom Mapping ausschließen

### 4 - Relationship Mapping in JPA
#### 1 - Relationships
* = OOP-Relationschips
* JPA wird auch über Annotatioen realisiert
* Bsp:
```java Ticket.java
class Ticket {
    //private Integer appId;
    @ManyToOne
    @Join(name="applicaton_id")
    private Application app; 

    //weitere Anpassungen z.B Constructor korrigieren + getter/setter
}
```
#### 2 - Mapping strategies overview
* = `@JoinColumn` und `@JoinTable`
* 
#### 3 - Mapping associations overview
#### 4 - Cascading events