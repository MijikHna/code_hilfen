### 0 - Introduction

### 1 - Introduction to Modularity
#### 1 - Introduction 
* Java 9 ist mehr über Programming Design
* JPMS (Project Jigsaw) - Java Platform Module System = modular JDK, modular source code, modular runtime images, Enapsulation der meisen internal APIs, Module System, Jlink und Java linker
* Vorteil:
    * man muss über Module am Anfang nachdenken
    * neue Konzepte, Syntax und Tools
* java Platform ist jetzt selbst modular
#### 2 - What is modularity
* Struktur in Projekt, kleinere Teile die in einander zum größeren Teil eingefügt werden
* Anzeihen für nicht Modularität:
    * Änderungen sind schwierig
    * Lange Build- und Deploy-Zeiten
    * verbraucht mehr HW-Ressourcen
* Module können einzeln oder zusammen mit andren Modulen arbeiten
#### 3 - Real-world modularity
#### 4 - Other paths to modularity
Microservices vs OSGi
1. Microservices:   
    * Archtektur Still
    * kleine, lose Komponenten
    * nicht nur Java
    * viel Ähnlichkeiten zu JMPS, wird aber anstelle von JPMS benutzt
        * Microservices - Architektur Still, JMPS - auf Klass- und Prozess-Level; mehr KLass und Package-Design
        * Microservices - schnlle Builds; Adjustement später; Disposale (Wegwerf) SW, JMPS - SW Design deliberate (durchdenken)
        * Microservices - kleine Komponenten; leichte Protokolle; guter Error Handling;
        * Microservices auf Archtiktur Level, JPMS auf Language Level (Java)
2. OSGi ähnlicher zu JSPM
    + eigene Syntax durch Bundles und Jar-Manifests
    * Services and Service Discovery
    * Runtime
    * App Server Platform
JPMS und OSGi bauen nciht auf einadner auf => Wettbewerber
### 2 - Java Modularity through the Ages
#### 1 - Modularity form Java to 1 to 8
* durch Klassen, Jar, Packages
* JPMS erweitert Modularity
* 5 Pillars (Säule) von JSMP 
    1. Encapsulation
    2. Interoperability (Kompatibilität)
    3. Composability
    4. Autonomy
    5. Exteautndability
#### 2 - Gaps in Modularity from Java 1 to 8
* Schwächen:
    1. Class Accessibility - nur pubic,private,protected und pacakges
    2. Classpath Hell- Jar-s zu Classpath aufnehmen => Probleme bei gleichn .jars aber unterschiedlichen Versionen
    3. Controlling the System Footprint - JDK.jar ist aber groß => wird nicht alle benutzt
#### 3 - New modularity artifacts
* JPRS brint neue Artifacts
* module.info.java 
    1. Module Encapsulation -> darin werden die die Accessebilities definiert
    2. Module Dependencies zwieshcen Packages und Modulen
    3. Module Integrity - Integrität und Garantien während der verschiedenen Phasen
* Module (module-info.java) - Package von Packages
* module-info.java
    + kann nur Module-Syntax-Code/Syntax enthalten
    * normaler Java-Class
    * verfügbar während der runtime
    * wird in dem Root-Level des Moduls deklariert
    * erstellt Namespace für Modul => muss eindeutig sein
    * Module geben die Pacakge-Hierarchie
#### 4 - New modularity syntax
* 
#### 5 - Modularity syntax considerations

### 3 - Building Modular Applications with Java
#### 1 - Designing a modular structure
#### 2 - Implementing the modular structure
#### 3 - Transitive dependencies
#### 4 - Qualified dependencies
#### 5 - Service dependencies
#### 6 - Service dependencies demo
#### 7 - Optional dependencies
#### 8 - Runtime dependencies
#### 9 - Challenge/Solution: Implement modularity

### 4 - Tools and Strategies
#### 1 - Build tools
#### 2 - JAR file versioning
#### 3 - Dependencies checking tools
#### 4 - Module packaging tools
#### 5 - Custom image building tools
#### 6 - Backward compatibility with classes
#### 7 - Backward compatibility with JARs
#### 8 - Tips and throughts
#### 9 - Challenge/Solution: Modules and legacy code