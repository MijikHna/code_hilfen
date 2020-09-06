### 1 - Unit Tests - Ein Überblick
* Es geht hier um (Unit-)Testing des Frontendes
#### 1 - Was ist Unit Testing
+ Test-Framework benutzen (hier jasmine)

#### 2 - Arten der Testautomation
* Modultests (Unit-Tests) -> Integrationstest -> UI-Tests
    1. UI-Tests: 
        1. führen Schritte des echten Benutzers aus
        2. schwer zu warten
        3. nur häufige Funktionen, Kernfunktionen, die häufig Fehler produziert haben.
    2. Integrationstest
        1. ob Kompoenten korrekt zusammenarbeiten
        2. parallel zu Entwicklung der und Unittest schreiben
    3. Modultests/Unittests
        1. eine Komponetne des Systems
        2. Abhängigkeiten durch Mocks ersetzt 
        3. sehr schnell
        4. eigentlich immer bei Veränderung des Codes.

#### 3 - Tests, Test Frameworks und Tests Runner
* `SystemUnderTest` <- wird von UnitTest gestestet. `Unit Tests` werden mit `Test Frameworks` geschrieben. Diese werden dann von `Test Runner` ausgeführt (meisten Test Framework kommen mit Test Runner)
* Test Framework:
    1. Jasmine
    2. Mocha
    3. Jest
### 2 - Motivation für Unit Tests
#### 1 - Auswirkung von Unit Tests
* kosten Zeit und Geld
* muss wie Prod-Code gewartet werden
#### 2 - Gründe gegen Unit Tests
* Contras:
    * keine Vorkenntnisse
    * Code funktioniert => keine Test nötig. ABER was passiert bei Änderungen/Erweiterungen/Refactoring
    * Zeitaufwändig
    * Schwierig bei bestehendem Code d.h. Abhängigkeiten nicht richtig isoliert => eventuell Redesign machen, damit man Unit Tests machen kann.
    * Unit Testing ist langwieilig => zuerst Unit Tests schreiben, dann Code schreiben.
#### 3 - Gründe für Unit Tests
* Pros:
    * Fehler frühzeitig aufdecken => Zeit sparen + noch weniger Abhängigkeiten. Code-Wissen noch aktuell.
    * Risiko bei Refactoring/Redesign mindern.
    * Debugging-Aufwände verringern
    * Unit-Tests dokumentieren den Code => da Unit-Tests auch Änderung des Prod-Codes angepasst werden. Zeigt auch wie man den Prod-Code benutzen kann.
    * Verbessern auch Architektur: da Komponenten getrennt getestet werden => lose Kopplung-Architektur benötigt => leichter zu erweitern und pflegen. => Unit-Tests zwingen saubere Architektur umzusetzen.
    * Basis für Qalitätsmetriken.
### 3 - Das Testing Framework Jasmine
#### 1 - Überblick über das Jasmine Testing Framework
* github.com/jasmin/jasmin => MIT-Lizens => auch für kommerziele Projekte erlaubt
    * Doku: jasmine.github.io
* Jasmine folgt einem BDD (Behaviur Driven Desing)
    * = Test beziehen auf "WAS" nicht auf "WIE" geschrieben wurde.
* open source Test-Framework für JS, dass BDD Syntax folgt. Für Client- und Server-seitigen Code benutztbar
#### 2 - Installation des Jasmine Testing Frameworks
* Jasmine über github.com -> Release:
    * xxx-standalone herunterladen/entpacken
        * in /lib sind Jasmine-Executables und Bibs
        + in /src => zwei Beispiele zum Testen
            + in /SpecRunner.html = Ausgaben der Tests werden hier gespeichert für Beispiele.
        * jasemine.js = eigentliche Definitionen
        * boot.js.
        + /spec = hier landen die Test-Quellendateien
        * Test werden über das öffnen von SpecRunner.html ausgeführt
* Standard-Test-Aufbau: AAA = Arrange Act Assert - Syntax. Jasmine hat andere Syntax:
* Jasmine Bestandteile:
    * Suite = Test-Suite `describe("Name der Suite", fucntion () {});`
        * Spec = beschreibt Funktionlität des Code: `it('Spec Beschreibung', function () {});
            * Expectation <-> Matcher `expect(xxx.call().toBeTruthy());` - `toBeTruthy()` ist Matcher
        * Spec 
#### 3 - Specs, Expectatoins, Matchers
* Standard-Test-Aufbau: AAA = Arrange Act Assert - Syntax. Jasmine hat andere Syntax:
* Jasmine Bestandteile:
    * Suite = Test-Suite `describe("Name der Suite", fucntion () {});`
        * Spec = beschreibt Funktionlität des Code: `it('Spec Beschreibung', function () {});
            * Expectation <-> Matcher `expect(xxx.call().toBeTruthy());` - `toBeTruthy()` ist Matcher
        * Spec 
* Jasmine Syntax unterscheidet sich leicht von der AAA-Syntax stattdessen BDD-Syntax (Suites, Spec, Expectation, Matchers)
#### 4 - Jasmine-Tests auf der Kommandozeile ausgeben
#### 5 - Karma konfigurieren
#### 6 - Erstes Bsp: Bestehendes JS-code über Tests absichern
#### 7 - Eingebaute Matcher
#### 8 - Eigene Matcher
#### 9 - Setup und Teardown
#### 10 - Tests mit xdescribe und xit überspringen
#### 11 - Asynchone Tests

### 4 - TDD - Test Driven Dev
#### 1 - Klassische Vorgehensweise vs. TDD
#### 2 - Bestehenden Code via TDD erweitern
#### 3 - Neuen Code per TDD entwickeln

### 5 - weitere Themen
#### 1 - Praxistipps zum Einstieg in Unit Testing