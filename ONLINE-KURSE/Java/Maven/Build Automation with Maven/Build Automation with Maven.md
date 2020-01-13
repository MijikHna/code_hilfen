### 2 - Understand Maven
#### 1 - POM
* Project Object Model
* Dieses Model besteht aus:
    * Project Lifecycle
    * Dependency Management
    * Logic zum Ausführen von bestimmten Prozesse in bestimmten Lifecycle-Phasen
* nimmt an, dass Projekte nach bestimmten Muster aufgebauet/verwaltet werden
    * Project Model hat:
        * Project Beschreibung `<description>`
        * einzigartige "Koordinaten" `<groupId>` + `<arifactId>` + `<version>`
        * Projekt Eigenschaften
        * Projekt Lizenzen
        * Projekt Version
        * Autor
        * Dependencis
* POM kann
    * Dependency Management
    * auf Remote Repos zugreifen
    * Build Logic wiederbenutzen
    * Tool-Integration (NetBeans, Intelij)
    * Artefacts durchsuchen
#### 2 - Maven lifecycle
* Maven LifeCycle:
    1. Projekt erstellen
    2. Maven ausführen
    3. Artifacts (Ergebnis des Buildes) in lokale Repo installieren 
    4. App ausführen
* Maven LifeCycle
    1. Validate - chechen, dass Projekt ok ist
    2. Compile
    3. Testen
    4. Package 
    5. Integration-Tests - Packages in Environments deploy, woe diese Tests gemacht werden
    6. Verify - checht Packages
    7. Install - Package ins lokale Repo installieren
    8. Deploy - Pacakge ins remote Repo installieren
* Maven Plugins können zu bestimmten dieser 8 Phasen hinzugefügt werden
    * haben Goal(s) für einzelne Phasen 
* `mvn install` -> Goals:
    * verschiedene Plugins haben ihre besimmte Goals ausgeführt (kann man unter `[INFO]` ansehen)
#### 3 - Maven Repository
* zwei Repos:
    1. Maven Remote Repo (search.maven.org)
    2. lokales Maven Repo ~/.m2
#### 4 - Maven dependency management
* für Code reuse
* ähnlich zu API
* `<scope>` - sagt in welchem Teil des LifeCycle dieser Plugin benutzt wird, also wenn man Dependencies definiert

### 3 - POM
#### 1 - POM categories and configuration
* hat alle Infos zu Projekt
* mindestens groupgID, ArtifactID und Version müssen sein

### 4 - Maven Plugins
#### 1 - Core plugins
* Maven Plugins
    * ist eine Colection von Goals
    * Goal ist "Unit of Work" in Maven
* Core-Plugins:
    * JAR-Plugins
    * Compile plugins
    * Surefire Plugins - zum Testen und Doku
    * Custom Plugins 
* Liste aller Plugins: maven.apache.org
* Bsp: Syntax: `mvn pluginName:pluginGoal`
    * `mvn compile:compile`
#### 2 - Packaging tools (plugins)
#### 3 - Reporting (plugins)
* `mvn javadoc:javadoc` - Doku für Projekt erstellen
    * wird in `/target/site/apidocs` abgelegt. -> index.html aufrufen
#### 4 - Tools (plugins)
* **archetype** - Templates bei Projekt erstellung
    * sollte dann über Console benutzen
    * `mvn help:describe -Dplugin-archetype` - Info über plugin **archetype** bekommen
### 5 - Create a Project with Maven
#### 1 - Create a sample program
* `mvn archetype:generate -DgroupId=la.lalal -DartifactId-name -DarchetypeArtifactId-maven-archetype-quickstart -DinteraciveMode=false` => `-DarchetypeArtifactId-maven-archetype-quickstart` - Templatename
* `mvn help:effective-pom` - ganze .pom-Datei
    * ersten Zeilen = Project-POM
    * weitere Zeilen = Super-POM
* `mvn install` - ist Phase in Lifecycle => wird ein paar Plugins anschmeißen. Es wird auch .jar (Artifact) ins lokale Repo installiert
* `java -cp target/sample-1.0-SNAPSHOT.jar org.lala.MainKlassenName` = `-cp` - Clathpath; das ganze führt das Java-Programm
### 6 - Test with Maven
#### 1 - Write unit tests
* in .pom muss Dependency für *junit* stehen
* `mvn test` - Tests ausführen
    * hier nicht ganz verstanden, woher mvn weiß, was Tests sind
#### 2 - Add dependencies
* Dependency kann intern oder extern sein
Bsp:
```xml
<dependencies>
    <dependency>
        <groupId>lala</groupId>
        <artifactId>lala</arifactId>
        <version>1.0.0<verion>
        <scope>compile</scope>
    </dependency>
</dependencies>
```
* `mvn install` => dabei werden die Dependencies ins lokale Repo installieren
#### 3 - Add test resources
* Resource = Datei
* Bsp: Resource = Datei, die Werte für Tests hat
    * Datei ins /src/test/resources legen (eventuell selbst erstellen)
    * im Code (Test-Code) die Datei öffnen und Werte lesen  
#### 4 - Packaging your app
+ Info zum Packagen (wie gepackt werden z.B .jar, war, ear (Default ist .jar)) steht in .pom 
`<packaging>jar</packaging>` - wie das Modul/Project gepackaged werden soll
* `mvn package` - .jar erstellen
### FAZIT:
* `<dependency>` - für Imports
* `<plugins>` - Maven-Plugins (sind dann auch Java-Programme)