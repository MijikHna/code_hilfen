### 0 - Introduction
#### 1 - Use JPA for inheritance and querying
* wird weiter an Trakzilla gearbeitet
    * = Spring-Based APP
#### 2 - Development env setup
* Java >= JDK 8
* Browser
* IDE
* Postman
#### 3 - Project application inroduction
* Trakzilla-APP-Architektur:
    1. Domain
    2. Service
    3. Data Access
        * DB: H2-DB = 3 Domain-Entities
            * Application
            * Ticket
            * Release
#### 4 - Proejct application in action
* 

### 1 - Inheritance Mapping Strategie
#### 1 - Entity inheritance strategie overview
* 4 Inheritance(Vererbung) Strategien in JPA:
    1. Mapped Superclass
    2. Single Table
    3. Joined Table
    4. Table per class
* in Trakzilla-APP Inheritance:
    * Ticket:
        * Bug
        * Enhancement
* in DB gibt es keine Vererbung
* damit man JPA-Vererbung machen kann => muss Klasse `@Entity` sein
#### 2 - Mapped superclass Strategie
* Entities können erben von:
    1. von Transient-Klass
    2. von Abstract Class
    3. von Mapped Superclass
* Bsp: Mapped Superclass:
    * Ticket -> wird nicht in DB erstellt = also wird nicht von EntityManger vewaltet: mit `@MappedSupperclass` annotieren + keien `@Entity`-Annotation
        * Bug -> wird in DB erstellt
        * Enhancement -> wird in DB estellt 
* Pros:
    * einfach
    * nur Kinder sind Entities
* Conras:
    + Eltern ist keine Entity
* nicht ganz verstanden: ABER Aufbau der Relationships wird dann etwas kompliziert
#### 3 - Mapped superclass: Demo

#### 4 - Single Table
* wenn man auch Eltern als Entity haben will
    * und Kinder werden in der Eltern-Entity d.h in DB in der Elterntabelle gespeichert = eine Tabelle für Eltern und Kind
* ist Default Vererbungs-Strategie, wenn man selbst nichts spezifiziert
* bei Eltern folgende Annotationen einfügen:
```java
@Entity
@Inheritance(strategie = InheritanceType.SINGLE_TABE)
public class Lala{

}
```
* damit JPA zwichen Kind und Eltern-Obj untescheiden kann wird in DB Zeile: `DTYPE` erstellt, wo Typ des Obj in DB gespeichert wird. Den Namen `DTYPE` kann man ändern mit `@DiscriminatorColumn` ändern in Eltern-Klasse
* Pros:
    + nur eine Tabelle für ähnliche Typen => polymorhpe Queries leichter
* Cotnras:
    * man kann nicht mehr `NOT NULL`- Constraints benutzen => kann eventuell DATA-Integrity-Issues verursachen, da wenn man jetzt eine Eltern-Enity erstellt, wird sie Kind-Attribute zu `NULL` setzen
#### 5 - Table per class
* also alles ist eine Entity:

* Annotationen für Eltern, Kind braucht keine besondere Annotationen:
```java
@Entity
@Inheritance(strategy=InheritanceType.TABLE_PER_CLASS)
public class Ticket {}
```

* erlaubt Assoziationen und Polymorphe Queries .d.h. alle Subclassen werden auch return (im Background wird UNION-Statement benutzt)
* Pros:
    * Polymorphe Queries
* Contas:
    + Polymophe Queries fügen DB-Komplexität hinzu => Performance-Issues
#### 6 - Joined table
* Kinder-DB haben keine Eltern Kinder d.h. ganze Kind eintrag wird auf zwei Tabelle verteilt:
    + Kind-Tabelle hat den gleichen PrimaryKey wie das Eltern-Tabelle= ForeignKey bei Eltern-Tabelle
* Pros:
    + erlaubt NOT-NUL-Contraints bei Kindern
* Contras: 
    + komplexe Queries => Performance
* wenn man direkt in DB SQL-Queries macht => muss man Tabellen Joinen
### 2 - Java Persistence Query Language (JPQL)
#### 1 - What is JPQL
* JPQL = Java Persistence Query Language = Query schreiben
* z.B Queries die nicht nach PrimaryKey suchen oder Listen abragen
+ JPQL ist SQL-Like
    * z.B Queries nach den Relationships machen
* SQL return Tabelle
* JPQL return Entity oder Collection of Entities
* Tipp: SQL-Logging bei Development aktivieren, damit man generierte SQL-Queries sehen kann.
#### 2 - Create simple queries with JPQL syntax
* Syntax hat zwei Teile:
    1. `select`-Part = definiet Format der Query (hier kann man auch `delete` oder `update` benutzen)
    2. `from`-Part = definiert Enitity/Entities, die geliefert werden könne
    3. Optional:
        1. `where`-Part
        2. `order` By-Part
        3. `group` By-Part
        4. `having`-Part
* man kan auch SQL-Funktionen auf `select` anwenden: 
    1. Funktioen: `avg`, `count` `max` usw
    2. Operatioen: `equal`, `less than`, `between` usw.
    3. Numbers: `sqrt`, `size`
    4. Strings: `length`, `concat`, `dates`
* Bsp:
    1. `select t from Ticket t order by t.title`
* Bsp aus dem Code.
```java
public List<Ticket> getAllTicket(){
    String query = "select t form Ticket order by t.title"
    return (List<Ticket>) entityManger.createQuery(query).getResult();
}
```
#### 3 - Create complex queries with setParameter
* = `createQuery()` + `getResultList()` + `setParameter()` diskutieren. Sind alles Methode der Klasse `Query`
    * `createQuery()` - Dynamische Queries erstellen, die Direkt in App-Business-Logik erstellet werden. Eigentlich erstellt ein Query-Obj um JPA-Query-Statement auszuführen
    * `getResult()` - return UNTYPED List => deswegen muss man Konvertieren
    * `setParameter()` - NamedParam and Query binden
* Bsp (aus ApplicationDAO.java):
```java 
String jpql = "from Application as app where app.name = ? and app.owner = ?"
int count = em.createQuery(jpqp).setParameter(0, name).setParameter(1, owner).getResultList().size();
```
* Pros:
    * leicht Queries wenn man nicht nach PrimaryKey fragen will
* Contras:
    * hohe Kosten da JPQL muss noch SQL übersetzt werden
#### 4 - Create compile-time named queries
* = fest definierte Queries (sind dann unveränderlich)
* werden in Entity-Klasse definiert mit `@NamedQuery`; können gruppiert werden mit `@NamedQueries`
* `@NamedQuery`: hat zwei Parameter
    1. Name der Query (gute Praxis: den Namen mit dem EntityNamen/Klasse präfixen)
    2. JPQL-Statement/Query
    3. Bsp:
    `@NamedQuery(name="Bug.findSevereBugs", query="select t form Ticket t where t t.severity = 1")`
* usefull, wenn man Quries organisiren will
* Result bekommen, genauso wie bei JPQL_Queries also `em.createNameQuery("Bug.findSeverBugs").getResultList();`
* Bsp:
```java EntityKlasse.java
@Entity
@NamedQuery(name="Bug.findSeverBugs", query="select t form Ticket where t.severity = 1")
public class Bug extends Ticket{
    ....
}
```
```java BugDAO.java
getServerBugs(){
    return (List<Bug>) entityManger.createNamedQuery("Bug.findSeverBugs").getResultList();
}
```
* Pros
    * bessere Code-Organisation, da Queries vom Java-Code getrennt werden
    * da statisch werden zu SQL beim Start der App. übersetzt
* Contra:
    * nicht veränderbar at Run-time
#### 5 - Create native queries
* = SQL direkt schreiben
* returnen aber auch Entities
* können wie dynaische Queries erstellt werden:
```java
public List<Enhancement> getTicketsWithApps(){
    String jpql = "select t.id t.description, t.status a.app_anme " + "from APPLICATIONS a, TICKET t " + "where a.application_id = t.application_id";
    return (List<Enhancement>) em.createNativeQuery(jpql).getResultList();
}
```
* Contras:
    * Java-Code wird abhänig von DB-Tabellen d.h. wenn man in DB etwas umbennent, kann es sein das die Query nicht mehr funktionieren wird
#### 6 - Create stored procedures
* Stored Procedures = Logik direkt in DB speichert
* vor JPA 2.1 keine Unterstüztung => Native Queries benutzen um Stored Procedures aufzurufen
+ eigentlich Views erstelen
* zwei Wege:
    1. Dynamic Stored Procedure 
    2. Declarative name strored Procedure
        * werden in der Entity-Klasse definiert mit:
        ```java
        @NamedStoredProcedureQuert(
            name = 'findByRelease',
            procedure = "FIND_TICKET_BY_RELEASE",
            resultClasses = {
                Ticket.class
            },
            parameters = {
                @StoredProcedureParameter{
                    name = "p_id",
                    type = "Integer.class",
                    mode = ParameterMode.IN)
                }
            }
        )
        ```
        * da ja wie View ist muss man zuerst in DB speichern, sonst wird JPA-Exception geschehen
        * für `mode = ParameterMode.XX`
            1. `IN` - input Parameter
            2. `OUT`- Outout Paramter
            3. `INOUT` - in und output Paramter
            4. `REF_CURSOR` - für DB-Cursor
        * DB muss stored Procedure unterstüzten => Doku der DB dazu lesen. 
            * dann Testen `call FIND_TICKET_BY_RELEASE(1)`
        * dann aufrufen: `em.createNamedStoredProcedureQuery("findByRelease").setParameter("p_id": pId);`
* Pros:
    + komplexe SQL-Queries in DB speichern und dann diese aus dem Code aufrufen
#### 7 - Query using streams
* Stream API:
    * `getResultStream()` - um durch Result-Set zu navigieren
    + => `getResultStream()` anstatt von `getReusltList()` aufrufen
    + Steams gut bei großen Listen von Results:
        * früher durch die Results gepaged => Fehleranfällig    
* Schritte:
    1. in pow.xml:
        * bei Spring-dependency einfügen:
        ```xml
        <dependency>
            <groupId>javax.presistence</groupId>
            <artifactId>javax.persistence-api</aritfactId>
            <version>2.2.</version>
        </depencency>
    2. `em.createQuery(query).getResultStream();`
        * jetzt kann man weiter Operation am Result ausführen
        * => einfach `.` am Ende eingeben und von Intellicense Vorschläge machen lassen z.B em.`createQuery(query).getResultStream().collect(Collectors.toList())` - 


### 3 - Criteria API
#### 1 - What is the Criteria API?
* = mit Java API Queries ertellen
* also man kann Anfragen mit JPQL oder Criteria API machen
    * JPQL sind String => können nicht von Java-Compiler überprüft werden
    + Criteria API = Queries für Entities von Java = werden in Java geschrieben + sind Type-Safe:
        * Code-Complitaion
        * Complier-Überprüfung
        + Portable
        * gut um dynamische Queries zu erstellen
#### 2 - Create queries with Criteria API
* Vergleich JPQL vs Criteria Query
    1. JPQL
    ```java
    String jpql = "select t from Ticket t"
    ```
    * `select`
    * `from`
    * `where`
    + `like`
    * `order by`
    * `group by`
    2. Crietria Query
    ```java
    CriteriaBuilder cb = em.getCriteriaBuilder();
    CriteriaQuery<Ticket> cq = cb.createQuery(Ticket.class); // Diese Query wird mit weitern Java-Statements erweitert 
    Root<Ticket> ticket = cq.from(Ticket.class); //from setzen
    cq.select(ticket); //select setzen
    TypedQuery<Ticket> q = em.createQuery(cq); //Query zum Senden voberetien
    List<Ticket> allTickets = q.getResultList();
    ```
    * `select()`
    * `from()`
    * `where()`
    * `like()`
    * `orderBy()`
    * `groupBy()`
+ 
#### 3 - Query relations using joins
* Tabellen Joinen:
    * `Join<X,Y>join(String attrName, JoinType jt)`
        * JoinType:
            * `JoinType.INNER` - ist default, wenn man nichts angibt.
            + `JoinType.LEFT`
* Bsp:
```java
CriteriaBuilder cb = em.getCriteriaBuilder();
CriteriaQuery<Ticket> cq = cb.createQuery(Ticket.class); // Diese Query wird mit weitern Java-Statements erweitert 
Root<Ticket> ticket = cq.from(Ticket.class); //from setzen
cq.select(ticket); //select setzen

Join<Ticket, Release> releases = ticket.join("release"); //Join Release an der Klasse Ticket = wird nur Tickets mit Realeasen ausgeben

TypedQuery<Ticket> q = em.createQuery(cq); //Query zum Senden voberetien
List<Ticket> allTickets = q.getResultList();
```
#### 4 - Restrict criteria query result
* = `WHERE`, `Conditional Methoden`
1. Where:
    * `CriteriaQuery<T> where(Expresoin<Boolean> restriction);`
2. CriteriaBuilder hat Methoden für Exression für Arithmetic, String, Date, Time, Case
    1. Codnidtion Methoden:
        1. equal
        2. NotEqual
        3. gt/ge/lt/le/between/like
    2. Compound Predicate Methoden:
        1. and
        2. or
        3. not
```java
CriteriaBuilder cb = em.getCriteriaBuilder();
CriteriaQuery<Ticket> cq = cb.createQuery(Ticket.class); // Diese Query wird mit weitern Java-Statements erweitert 
Root<Ticket> ticket = cq.from(Ticket.class); //from setzen
cq.select(ticket).where(cb.equal(ticket.get("status"), "CLOSED")); //select setzen !!!!!! WHERE-Clausel

Join<Ticket, Release> releases = ticket.join("release"); //Join Release an der Klasse Ticket = wird nur Tickets mit Realeasen ausgeben

TypedQuery<Ticket> q = em.createQuery(cq); //Query zum Senden voberetien
List<Ticket> allTickets = q.getResultList();
```
### 4 - Persistence Providers
#### 1 - Overview of persistence provider comparison
* Provider = liefet Implementierung von JPA
    + man muss auch verstehen welche SQL-Anfragen bei JPQL gelaufen werden
* Provider können auch eigene Erweiterungen von JPA implementieren (non-standard Funktionalitäten) => deswegen oft schwer von einem auf den anderen Provider zu switchen.
#### 2 - Persistence provider comparison
* Hibernate ist Default für Spring-Boot-Framework
* EclipseLink
+ OpenJPA
#### 3 - Change providers
* wenn man Standard-Funktionen benutzt eigentlich kann man Provider ändern, ohne Code zu ändern
* oft einfach in pow.xml die Dependency ersetzen bzw. Depenency excluden, wenn JPA Teil einer Abhängigkeit ist.
* Hier im Bsp von Hibernate auf EclipseLink umsteigen, musste man .java-Datei mit Einstellungen für EclipseLink erstellen = CustomConfiguration, erweitert `JpaBaseConfiguraion` => folgende Methoden muss man überschreiben:
    1. `createJpaVendorAdaper()` = welcher Provider soll benutzt werden
    2. `getVendorProperties()` = Provider-speziele Eigenschaften setzen.