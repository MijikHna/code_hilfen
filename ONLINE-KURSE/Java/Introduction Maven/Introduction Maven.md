### 0 - Introduction
#### 1 - Building Java the Maven way
* Apache Maven - Apps Builden
    + kann App Bilden, Dep Management, Dokumentation, Unit Testing und Reporting
#### 2 - What you need to know
* Maven-Config ist in XML
* Installation:
    1. Java Installation
    2. Apache installieren eventuell mit Packet Manager
        * `M2_HOME` - Apache verwendet oft diese Env-Variable
* hier Intellij wird verwendet 
### 1 - Maven Basics
#### 1 - Introduction to Apache Maven
* Apache - Software Project Management + Comprehension (Verständnis) Tool 
    * Management durch Project Object Model (POM-Datei)
* Entwickelt um SW zu bilden
* Maven Ziele:
    1. Easy Build
    2. Uniform Build System (POM-Datei) (ist dann System unabhängig)
    3. Dokumentation zum Bilden
        * Dependency List
        * Test Exec Reports
        * Change Logs
        * Java Docs
* 
#### 2 - The Java project structure
+ Java Project Structure ist eine Struktor von Maven für Java-Projekte
* Separiert Code from Resourcen
* Separiert Runtime Code von Tests
* Struktur:
    * **root**-dir
        * **src**-dir
            * **main**-dir - Code
                * **java**-dir für Java-Code
                * **resources**-dir für Resourcen
            * **test**-test - Code
                * **java**-dir für Java-Code
                * **resources**-dir für Resourcen
            * eventuell weiter dirs, die von Maven-Plugins erstellt werden
        * **pom.xml**
#### 3 - The POM file
* POM - Project Object Model 
    * hat Infos über das Project:
        * Info zu Project = Project Information - Top
        * Dependencies
        * Build Details
        * Reporting Details
1. Project Information - Top Level Details des Projects
    * groupId - Gruppe zu der App gehört (Organisation Unit in Maven Repo). Oft korrespondiert zu Root-Package des Projects
    * artifactId - (auch projectId) - Eigentlicher Name des Projects
    * Version z.B. Snapshot oder Release
    * Properties
    * Dependencies
    * Build - Plugins die Project bilden
    * Report - wie Reports gemaht werden
    * Repository - Maven-Repos für Artifacts
    * Plugins - welche Plugins benutzt werden
    * Profiles - mehrere Profile, überschreiben Defaults
#### 4 - POM properties
* wer welche Issues gelöst hat
* vermeiden Dublikatinen
* Items in Sync halten vor allem Versionen
```xml
<properties>
    <jackson.version>2.9.8</jackson.version>
    <slf4j.version>1.7.25</slf4j.version>
    <junit.version>5.2.0</junit.version>
    <java.version>11</java.version>
    <surefire.version>3.0.0-M3</surefire.version>
</properties>
```
* Properties-Section einfügen. Die Versionen und Programme wurden aus dependencies-Section herausgelesen
* dann kann man jetzt in den Dependencies die *hart*-geschriebenen Versionen mit denen aus den Properties ersetzen Bsp: *jackson*
```xml
<dependencies>
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-core</artifactId>
        <version>${jackson.version}</version>
    </dependency>
    <!-- ... -->
<dependencies>
```
* somit kann man dann die Versionen leichter updaten, indem man nur die Version an einer Stelle ändert

#### 5 - Dependencies
* in `<scope>lala</scope>` kann man Scopes festlegen
* groupId = Name der Dependency
* aritfactId = die Dependency referenzieren 
#### 6 - Build
* in `<build>` wird mit `<plugins>` gearbeitet.
* Bsp:
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.8.0</version>
            <configuration>
                <target>${java.version}</target>
                <source>${java.version}</source>
            </configuration>
        </plugin>
        <!-- ..weitere Plugins + deren Configs.. -->
    </plugins>
</build>
```
+ in `<configuration>` sagt man dem Maven-Compiler welche Jave-Version benutz werden soll
* Plugins auswählen + dren Navigation: Bsp: Compiler-Plugin
    * https://maven.apache.org/plugins/index.html
    * *compiler* auswählen
    * links auf *Usage* klicken - hier stehen auch ein paar Bsp
    * links auf *Compile Using -source and -target javac Option* klicken => Template 
* Maven-Build executen = maven-command
    * in den Project navigieren
    * `mvn clean package` - *clean* ist Optional, löscht alte Sachen löschen. package erstellt .jar int target-Ordner

#### 7 - Reporting
* Doku erstellen + Doku des Bilds
```xml
    <reporting>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-report-plugin</artifactId>
                <version>${surefire.version}</version>
            </plugin>
        </plugins>
    </reporting>
```
* Repost erstellen: 
    * ins Project-Ornder gehen, wo das richtige .pom liegt
    * `mvn clean package site` - site erstellt Doku
    * in `target/site` und `index.html` öffnen 
#### 8 - Reactors and parents
* Dependencies auf höhren Ebene kontrollieren -> Dependencie-Hierarchie
* Parent Pom:
    * Dependencies und Plugins die alle Subprojekte 
    * Properties + Repos für alle alle Subprojekte z.B Versionen für Plugins für Unterprojekte
* Reactors:
    * Bildet auf dem Konzept vom parent-POM
    * um zusammenhängende Subprojekte zu bilden über parent-pom 
* Struktur:
    * Root -> pom.xml: hat Liste von Untermodulen + gleiche Dependencies und Plugins; packaging sollte **pom** sein
        * module -> pom.xml zeigt auf Parent-web
* <- z.B. zum bilden der Shared Libs
* in Root-Ordner: `mvn clean package` - 
#### 9 - Understanding archetypes
* = ist Project Template/Struktur. Wird eigentlich erstellt, wenn man Project startet
* benutzt wenn:
    * für Package-Strukturen

### 2 - Build
#### 1 - Introducion to the build lifecycle
* Drei Default-Lifecycles: -> besteht aus Phasen
    * Default - Main Lifecycle für Bilden und Deployen
    * Clean - um Project bzw. /target zu cleanen
    * Site - Seiten-Dokumenation erstellt.
* Phasen (Default-Phasen) = Step/Stage in Lifecycle
    * Default Lifecycel -> Phasen: validate -> compile -> test -> package -> verify -> install -> deploy
    * Phasen müssen in Reihenfolge ausgeführt werden
    * Phasen selbst haben Goals
* Goals - einzelnge Task in Phasen
    * Goals sind an Phase in Lifecycle gebunden
    * Goals kann man aber auch einzeln triggern z.B 
        * `mvn depenendency:analyze` - Plugin **dependency** hat Goal **analyze** = zeigt Status der Dependencies
        * Nüztlich wenn man nicht alle Phasen durchlafen will
#### 2 - Leverage build plugins
* Biuld Plugins - Plugins für Build-Phasen in Lifecycles
* maven.apache.org/plugins/index.html
* Drei Arten von Build Plugins
    1. core - 
        * Kompileren (benutzt jvm)
        * Installation - zum Packagen, Artefakt-erstellung + Installieren in Maven-Repo
        * Deployment - Artekfakt zu Remote-Repo schieben
        * Validation
    2. packaging - Byte-Code in Struktur bringen, damit es funktionert 
        * jar - Jar produzieren
        * war - für WebApps z.B für TomCat
        * ear - Enterprise
        * shade 
    3. tools - sonstige
        * release - Tagen usw.
        * signing - Jars signen
        * depencency - build-Tool zum bilden + analysieren der Dependency-Trees 
#### 3 - Core plugins
* compiler-Plugin - Kompiliert Source-Code
    * `mvn compile`
    * `mvn test-compile` - Test ausführen
    * sollten in Parent-POM sein
* deploy-Plugin - zur master-Repo den Code/Build schieben
    * `deploy:deploy` - eigenen Code zu deployen z.B. zu Production-Server
    * `deploy:deploy-file` - fremden Code bei sich deployen 
* resources - Resourcen z.B JS, CSS usw. mit in jar packen
* surefile - JUnit-Test machen + Doku zu den Test erstellen
* failesafe - für Integration-Tests durch Lifecycle
* maven.apache.org/plugins -> SEHR GUTE DOKU
    * Usage-Reiter
    * Example-Reiters
#### 4 - Tools plugins
* sind Konfigrationsschwer
* dependency:
* enforcer: - damit alle den gleichen Stand haben z.B alle haben gleiche Versionen usw. -> bestimtme Sachen forcen oder Plugins bannen
* jarsigner: JAR signieren (man sollte derzeit Production-JARs immer signen)
* release: Project bilden + releasen (versionieren + tagen + für nächsten Scrum vorbereiten)
#### 5 - Packaging plugins
* ear
* jar
* war

### 3 - Depnedencies
#### 1 - Scope
* Dependency Scope - wie alles packaged wird:
* Scopes:
    * Compile Scope:
        * ist Default
        * diese Dependency wird kompiliert
    * Provided Scope - meist für Enterpice
        * ähnlich wie Scope
        * nicht transitive = nicht im finalen Projekt
    * Runtime Scope
        + wenn man mehrere Implementierungen von API hat
        * nur zum Ausführen (nicht für Kompileren)
    * Test Scope:
        * reduziert Artifakt Menge
        * nur bei Test und Execution
        * nicht transitive 
    * System Scope:
        * Pfade auf dem Rechenr
    * Import - nur für POM Files 
#### 2 - Transitive dependencies
* = Dependenceis von Dependencies
* Reduziert die Menge von Dependencie-Deklarationen, da vom Parent-POM vererbt
* Regeln:
    * die näherste Version zum Projekt gewinnt
    * Scopes sind hier wichtig
    * Lokale Dependencie Definitionen gewinnen immer
* Tricks:
    + richtige Scopes
    * Versionen in Parent-POM 
#### 3 - Dependency management
* Bsp: Versionen also `<properties>`-Teil aus Kind in Parent kopieren und `<dependencyManagement>` in Parent anglegen, `<dependencies>` in Kind in `<dependencyManagement>` kopieren (nicht ausschneiden), `<scope>` und `<version>` in Kind in `<dependencies>` löschen => version und scope wird von Parent genommen
* <- das gleiche kann man auch mit plugins machen
* `dependency:analazy` - checken, ob Dependencies OK sind
#### 4 - Dependency goals
* `mvn dependency:analazy`
    * Warning:
        * `undeclared dependencies found` - ist Dependency, die nicht definiert wurde, die vererbt wurde (d.h. könnte z.B Probleme verursachen)
        * `unused dependencies`
* `mvn dependency:resolve` - Liste von deklarierten Dependencies
* `mvn dependency:tree` - zeigt von wo die .jar in den Klassen kommen
#### 5 - Uber JARs
* = Shaded jar

### 4 - Reporting
#### 1 - Maven sites
#### 2 - Site look and feel
#### 3 - Common reporting plugins

