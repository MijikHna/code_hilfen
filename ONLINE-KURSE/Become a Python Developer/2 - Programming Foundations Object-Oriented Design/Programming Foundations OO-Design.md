### 1 - Object-Oriented Fundamentals:
#### 1 - Object-oriented thinking:
1. Finktionaler/Prozeduraler vs OO Programmierung ← jeder hat seine Vor-/Nachteile ← sind Sprachenparadigmen
#### 2 - Objects:
1. Objekt-Definition vs. Objekt-Instanz
2. Objekte werden durch Identität, Attribute, und Verhalten beschrieben
#### 3 - Classes:
1. =Vorlage = aus drei Teilen (Name, Attribute, Verhalten)
2. Methoden = Funktionen einer Klasse
3. Existierende Klassen meiste Sprachen:
    1. Strings, Datum, Collections, I/O-Klassen, Netzwerk-Klassen usw. => von denen erben. ← heißen irgendwie Standard Library
#### 4 - Abstraction:
1. ~ Vorlage
#### 5 - Encapsulation:
1. Element/Instanz des Objekt hat alle Attribute und Methoden (eventuell muss etwas geschützt werden) + Zugang nur über Objekt-Methoden möglich => bei Änderungen mehr Aufwand nur in bestimmten Methoden, die auf geänderte Attribute zugreifen sollen
#### 6 - Inheritance:
1. Vererbung = Wiederverwendbarkeit + bessere Wartbarkeit
2. Es gibt Mehrfachvererbung (C++, Python) und Einfachvererbung (Java)
#### 7 - Polymorphism:
1. = mehrere Formen haben
2. Polymorphismus hat mehrere Formen:
    1. dynamisch = ein Interface wird von mehreren Objekt-Instanzen benutzt = Interface ist gleich die Methoden werden aber überschrieben.
    2. Methoden Überladung = andere Parameter (+ Rückgabe) der Methode
#### 8 - Analysis, design and programming:
#### 9 - OO Analysis/Design/Programmierung
1. Analysis = Problem verstehen
2. Design = Algorithmus/Lösung ausdenken
3. Programmierung = Implementierung
4. Eventuell Analysis + Design = ein Ganzes = führt zu Klassendiagramm
#### 10 - Unified modeling language (UML):
1. Graphische Beschreibung der Klassen (Name der Klasse, Attribute, Methoden)
2. ← es gibt verschiedene Diagrammtypen (meistens Klassdiagramm und Use Case Diagramm)
3. Lesetipp zu UML = UML Distilled von Martin Flower
### 2 - Requirements:
#### 1 - Defining requirements:
1. Was/Warum soll das das Produkt muss machen, was sind die Funktionen/Features
2. Anfoderungen: Gesetzliche, Leistung, Sicherheit, Support
3. Anforderungen → für HW- und SW-Projekte
4. Anforderungen:
    1. muss machen ← hat nichts mit OOP zu tun => logische Anforderungen = reiner Text
    2. sollte sein (Zugänglich, Userfreundlich usw.) ← non funktionale Anforderungen 
#### 2 - FURPS+ requirements:
1. Functionality (Kern), Usability (Userfreundlichkeit), Reliability (Sicherheit usw.), Performance, Supportability (Testbarkeit, Erweiterbarkeit, Konfigurierbarkeit)
#### 3 - Challenge: Jukebox requirements
#### 4 - Solution: Jukebox requirements
### 3 - Use cases and User Stories:
#### 1 - Use cases:
1. wie das Programm vom User bedient wird. ← reiner Text, in einfachen Sätzen
2. Braucht:
    1. Title = Was wird gemacht
    2. Akteur = wer macht am Programm was ← kann auch anderes externes System sein
    3. Sznario = welche Schritte werden gemacht
    4. Erweiterungen = was passiert, wenn etwas schief läuft (z.B falsche Eingaben)
3. Lesetipp: Writing Effective Use Cases von Alistair Cockburn
#### 2 - Identifying the actors:
1. welche Benutzergruppen mit welchen Zielen,
    1. Primäre vs. Sekundäre Akreure
2. welche externe Gruppen mit welchen Zielen,
3. welche externe Programme mit welchen Zielen
#### 3 - Identifying the scenarios:
1. Ziele der einzelnen Akteure definieren ← sollten kurz sein, keine Fachsprache, basierend auf den Zielen
#### 4 - Diagramming use cases:
1. zeigt Abhängigkeiten zwischen Akteuren und Szenarien
2. = Akteuren(meistens rechts) pfeilen Szenarien an (braucht aber keine Pfeilenden); Szenarien sind System; kein User (z.B externes System => << ACTOR >> …, … (auf linken Seite) 
#### 5 - User stories:
1. Alternative zu Use Case Diagramm ← in zwei/drei Sätzen; Form: As a ( type of user), I want (goal) so that (reason), reason ist optional ← keine Fachsprache benutzen
2. User Strories != Use Cases
3. Lesetipp: User Stories Applied for Agile Software Development von Mike Cohn
#### 6 - Challenge: Jukebox use cases:
#### 7 - Solution: Jukebox use cases:
1. ← Alles im Allem bei jedem Schritt muss man eventuell zurückgehen und Veränderungen machen, da neue Anforderungen entdeckt werden; ← Kapitel 3 = Analyse.
### 4 - Domain Modeling:
#### 1 - Identifying the objects:
1. = Konzeptuelles Modell daraus entwerfen = welche Klassen benötigt werden und deren Beziehungen.
2. Aus Use Cases alle Nomen nehmen und schauen, ob sie ein Objekt werden können oder eventuell Attribute des Objekts.  
#### 2 - Identifying class relationships:
1. = alle Objekte nehmen und schauen, ob Beziehung zwischen denen bestehen => 1)erst Mal nur Pfeile zueinander machen, 2) Verben an den Pfeilen schreiben (~ uses), 3) Menge-Beziehungen schreiben: 1; 1..* usw. ↔ UML
#### 3 - Identifying class responsibilities:
1. nach Verben schauen um nach Verantwortlichkeiten zu suchen = wessen Verantwortlichkeit es ist diesen Verb auszuführen. !! Verb darf nur vom „richtigen“ Objekt ausgeführt werden. ← eventuell andere bieten (initialisieren) anderen Objekte bestimmte Aufgaben auszuführen.
#### 4 - CRC cards:
1. Class, Responsibility, Colaboration = Tabelle aus zwei Spalten: Responsibility | Collaboraters + Titel = Klassname
#### 5 - Challenge: Jukebox conceptual model:
#### 6 - Solution: Jukebox conceptual model:
1. Fazit: CRC = alternative zu 1)-3) (UML)
### 5 - Class Diagrams:
#### 1 - Creating class diagrams: Attributes:
        1. man kann auch Initialwerte in Klassendiagramme schreiben: ...=“Wert“
#### 2 - Creating class diagrams: Behaviors:
1. vor Attributen/Methoden:
    1. + = public
    2. - = private
2. zuerst das Klassendiagramm überlegen, dann Programmieren
#### 3 - Converting class diagrams into code:
1. zu Python:
    1. hat eigentlich keine private vs. public Varaiblen => alles ist public. Programmieren ist selbst verantwortlich, dass er nichts falschen damit macht.
        1. ABER: man macht _ vor der Variablen, so weiß man, dass die Variable eigentlich private ist
#### 4 - Instantiating classes:
1. in Python gibt es kein new XXX() => einfach: obj1 = XXX()
2. Konstruktor ist in Klassendiagramm als normale Methode eintragen.
#### 5 - Class with multiple constructors:
1. Konstruktor !!! → wenn Objekte ein anderes Objekt hat => dieser Konstruktor muss Unterobjekt erstellen.
#### 6 - Static attributes and methods:
1. static in Klassendiagramm - 
2. static = wird von allen Klassenobjekten benutzt. ~ ist globale Variable innerhalb der Klasse(objekte)
3. Python hat kein stataic-Keyword => alles was außerhalb von „def __init__()“ bzw. außerhalb einer Funktion definiert ist, ist static Variable.  Zugriff über nicht über Objektnamen, sondern über Klassennamen.
4. ??? Python static Klassenmethoden
#### 7 - Challenge: Jukebox class diagrams:
#### 8 - Solution: Jukebox class diagrams:
### 6 - Inheritance and Composition:
#### 1 - Identifying inheritance situations:
#### 2 - Using inheritance: (Ableitung)
1. Python: Oberklasse(Unterklasse):
2. Methoden überschreiben in Oberklasse → siehe Dokumentation der Klasse (manchmal werden Keywörter benutzt
3. Methode der Unterklasse aufrufen: super().funktName()
#### 3 - Abstract and concrete classes:
1. Wenn von Oberklasse keine Objekte erstellt werden sollen:
    1. Muss mindestens eine abstrakte Methode haben. (kann Mix aus abstrakten Funktionen haben)
    2. 
2. in Klassendiagrammen den Klassennamen Italics machen
#### 4 - Interfaces:
1. hat nur Definition der Funktionen ( im Vergleich zu abstrakten Klassen, hat gar keinen Code innerhalb der Funktionen. Die Klassen, die Interface bekommen, müssen den Code dafür haben):
    1. Interface = präsentieren Möglichkeiten der Klasse (XXX kannYYY)
    2. Abstrakte Klasse = präsentiert den Typ der Klasse (XXX ix YYY)
#### 5 - Aggregation: 
1. 1(XXX hat /benutzt (mehrere) YYY). - ein Objekt hat (mehrere) andere Objekte
2. in Klassendiagramm mit Pfeil von → zu + mit den Indizien der Menge.
3. Die einzelnen Objekte können aber auch unabhängig von einander existieren
#### 6 - Composition:
1. spezifische hat/benutzt – Beziehung. 
2. Wenn die Owner-Klasse gelöscht wird => wird auch geowned Objekt gelöscht.
3. Klassendiagramm ist wie bie Aggreagtion:
#### 7 - Challenge: Jukebox class relationships:
1. Inheritance-, Interface- Aggregation- und Composition- Pfeile in Klassendiagramm sehen am der Spitze alle anders aus. 
#### 8 - Solution: Jukebox class relationships:
1. mit Ableitung nicht übertreiben, da man sonst einfach mehr Klassen erstellt als nötig
### 7 - Software Development:
#### 1 - OOP support in different languages:
1. Python und C++ haben Merhfachvererbung
2. Python dynamisch Typisiert, C++ statisch Typisiert
3. in C++ und Python Interfaces sind komplett abstrakte Klassen 
#### 2 - General developmet principles:
1. = SOLID: (Single responsibility principle, Open/closed principle, Liskov substitution principle, Interface segregation principle, Dependency inversion principle)
    1. SRP  -Single Responsible Principles => keine Gott-Objekte, die alles machen, stattdessen jede Klasse macht ihre Aufgaben
    2. DRY – Don‘t Repeat Yourself => copy-paste minimal halten, da sonst bei Fehler überall diesen Fehler suchen und ersetzen
    3. YAGNI – You Ain‘t Gonna Need It => 
#### 3 - Es gibt Tools, die den Code analysieren, sind konfigurierbar
#### 4 - Software testing:
#### 5 - Design patterns:
1. = wieder-benutzbare Form der Lösung/des Algorithmus zu einem Problem. Definieren Code-Architekturen, beste Practises zum Lösen der üblicher Probleme. 
2. = Muster um den Code besser zu strukturieren
3. Musterarten:
    1. Factory Method Pattern = benutzen „Werk“-Methoden, um Objekte zu erstellen
    2. Memento Pattern – gibt die Möglichkeit das Objekt zum vorherigem Status zu restoren
4. Buch Tipp: Design Patterns: Elements of Reusable Object-Oriented Software von Erich Gramma, Richard Helm …
    1. die Basis Pattern aus dem Buch:
        1. Creational Patterns = zum Objekte instantieren 
            1. Abstract Factory
            2. Builder
            3. Factory Method
            4. Protopye
            5. Singeton
        2. Structural Patterns = wie man die Klassen designt (Vererbung usw.)
            1. Adapter
            2. Bridge
            3. Composite
            4. Decorator
            5. Facade
            6. Flyweight
            7. Proxy
        3. Behavioral Patterns:
            1. Chain of responsibility 
            2. Command
            3. Interpreter
            4. Interator
            5. Mediator
            6. Memento
            7. Observer
            8. State
            9. Strategy
            10. Template
            11. method
            12. Visitor
5. Tipp Buch 2: Head First Design Patterns: A Brain-Friendly Guide von Eric Freeman, Bert Bates …
6. man kann auch auf lynda.com Design Patterns lernen