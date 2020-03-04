### 1 - Was ist Angular
#### 1 - Was zeichnet ein WebFramework aus
* JS-Framework von Google (Open Source) um module-basierte Web-App entwickeln
* Derivate von Angualar für iOS und Android (NativeScript; ionic)
* Angular-Features:
    1. Client-Server-Komunikaiton = mit Backend zu reden
    2. Datenbindung = in View Daten aus DB presentieren
    3. Animationen
    4. Routing für Singe-Page-Applicatione = mit einer BASE-HTML unterschiedliche virtuelle Views erstellen
#### 2 - Komponentenbasierte Entwicklung
* Komponente = HTML-Knoten
* Logik, HTML-Vorlage und Style trennen
* Komponente in Komponente möglich (Kind-Komponente) bzw. 
#### 3 - Trennung Logik und View
* Komponente =
    1. Logik = TS-Klasse
    ```ts
    export class UserComp{
        name = "Kirill"
        changeName(){
            this.name = "Peter"
        }
    }
    ```
    2. View = HTML-Vorlage
    ```html
    <h1>{{name}}</h1>
    <button (click)="changeName()">Ändern</button>
    ```
    3. View-Style = CSS
    ```css
    h1 {
        color: gray
    }
    ```
#### 4 - Modulare Arbeitsweise
* Anguler-Module ~ Container: Komponenten, Direktiven, Pipes, Service
* Komponten kann nur in einem Modul vorhanden sein
* Module können aber andere Module importieren bzw. Komponenten aus Modulen importieren
### 2 - Kernfunktionen des Angular-Frameworks
#### 1 - Decorators
+ = Funtionen
* werden vor Klassen, Methoden gesetzt
* erweitern eigentliche Klassen, Methoden bzw. nur Metadaten
* Dekoratrofunktionalitäten
    1. speichert Metainformationen
    2. Funktion, Klasse manipulieren/erweitern
* Decorator-Typen:
    1. für Klassen
    2. für Eigenschaften
    3. für Methoden
    4. für Parameter
#### 2 - Vorlagen
* HTML-Schnipsel = Definition einer Kopmponten; = View
* zwei Möglichkeiten Vorlage zu definieren
    1. als Zeichenktett
    2. als Datei
#### 3 - Bindungen
* Bidnung
    1. mit Ausdrucksinterpolatione:
        * `<h1>{{ name }}</h1>`
        * `<h1>{{ getName() }}</h1>`
    2. als Eigenschaft = []
        * `<img [src]="imgPath">`src soll Wert von imgPath-var bekommen
#### 4 - Direktiven
* Direktiven werden in Vorlagen benutzt
* als Attribute ausgezeichnet
* zwei Typen der Direktiven
    1. strukturellen Direktiven = manipulieren DOM
        * `<img *ngif="showImg">` - if-Direktive (stukturelle Direktive)=> img-DOM-Knoten wird angezeigt nur wenn showImg==True ist
        * `<li *ngFor="let label of labels">` - ngFor benutzt Element (hier also `<li>`) als Vorlage, iteriert über label und erstellt so of `<li>`
    2. Attribut-Direktiven = Aussehen/Verhalten eines Elements manipulieren
        * `<input matIput>`
        * `<textarea matAutosizeMinRows="2">`
        * `<input [ngClass]="inputClass">` - hier Bindung `[]` + Direktive
* Syntax: beginnt mit `*`
#### 5 - Pipes
* wie in Linux 
* Transformation der Ausgabe auszuführen
Syntax: `AUSDRUCK | PIPE_NAME<: PARAMETER>` - überwiegend in Templates benutzt
```ts
<h1>{{ name | uppercase }} //Pipe ohne Parameter
<h1>{{ createdAt | date: 'long' | uppercase }} //Pipes können verkettet werden
``` 
#### 6 - Services
* Services = View-unabhängige Logik = eigentlich JS-Klasse - ist Singelton (wird über Dependency Injection realisiert)
#### 7 - Dependency Injection
* ist eigentlich Entwurfs-Muster
+ in Anguler = Services,Werte, Funktionen injizieren zur Laufzeit
* innherhalb des Continers/Injector bereitgestellt. Bereitstellung durch Anhängen in provide-Liste (provider-Liste erfolgt über Metainfo (Decoratoren)). Metadaten kann man für Module oder Kompontent nalegen
* Dependency Injection:
    * es gibt Rootinjektor anwendungsweit
    * wenn man ein Modul anlegt, kann man über `@NgModule({providers: [ServiceA]})`-Decorator Metadaten hinterlegen => wird im Rootinjektor dieser Provider registiert. Und jedes Mal, wenn ServiceA benötigt wird wird er von Rootinjektor angefragt (also Singelton; ABER Singelton pro Injektor)
#### 8 - Routing
* Routing-Modul implementieren bzw. importieren
* = Basis einer Single-Page-Application = bestimmt, welche Komp. bei welchem Pfad angezeigt wird (virutelle Pfade)

* App-Komponente = Root-Komp.
    * hat Knoten => je nachdem welche URL wird in diesen Knoten andre Komp. reingestellt
#### 9 - Formulare
* zuerst Form-Modul importieren
* zwei Strategien:
    1. Vorlagen-getrieben, wobei in der Vorlage Direktiven benutzt werden
    2. Raktiv = welches Model, Validatioren usw. und leitet diese Info ins Template
* Model des Formular + Validierung 
* Validierung: zwei Wege
    * anhand der CSS-Klassen
    * über Kontroller
#### 10 - Animationen
* dafür eigens Angular-Modul
* diese Modul stellt eine Schnittstelle zu **Web Animations API** des Browser dar. Wenn Browser Web Animations API nicht unterstützen => Polyfills nutzen
* Angular-Animation hat immer ein Zustand (mittels CSS-Styles)
#### 11 - Compiler
* 
#### 12 - JIT
* Compiler kann als JIT - Just in Time arbeiten. Wird von Browser compiliert.
* JIT wird überwiegend in Dev genutzt
Ablauf:
* Server: Vorlagen,Styles,Logk --(parse)-->Browser:View Code (AST) --(eval JS)-->Browser:View-Klassen --new-->Laufenden Anwendung
* Nachteile:
    1. **eval**
    2. Sicherheit
    3. Compiler-Zeit
#### 13 - AOT
* Compiler kann als Out of Time arbeiten. 
* Compilierung bevor Code auf dem Server landet.
* Vorlagen,Styles,Logik --(parse)-->View-Code(AST) --gener-->View-Code(TS) --gener-->View-Code(JS) (Das wird dann auf den Server gesschoben)
    * auf dem Server nur --new-->
    * Vorteil: Compiler muss nicht zum Client benutzen
* inzwischen wird auch in Dev verwendet

### 3 - Die Entwicklungsumgebung für Angular-Projekte
#### 1 - in Angular-Projekten verwendete Technologien
* muss:
    1. Angular
    2. node.js
    3. TS
    4. git
    5. webpack
* weitere Tools:
    * SASS - programmierbare CSS = Preprozessor
    * Karma - Unit-Tests von jest ausführen
    * Jasmine - 
    * Protraktor - E2E-Tests
#### 2 - nodeJS
* = JS-Laufzeit-Umgebung
* JS-Code ausführen
    * Bsp: mit Elektron Betriebssystem-Anwendugnen erstellen
* in Dev benutzt um
    1. Entwickeln + Testen = VM-Server, Packetierung, Compilierung
    2. Veröffentlichen der Packages
#### 3 - TS
* ES2015-basierte-ProgrammiernSprache (ES6)
* unterstützt: Klassen, Vererbung, Typisierung,Interface, Enum usw.
* TS kann den Code auf ES5 herunterkompilieren
#### 4 - git
+ Gedanke des Autors: Commit = Zustand
#### 5 - SASS
* = Erweiterungssprache für CSS
* = Preprozessor für CSS
* Man Kann:
    1. Variablen = z.B CSS-Werte verwenden, 
    2. Funktionen = Mixins 
    3. Erweiterungen = sowas wie Vererbung
    4. Module = CSS in einander schachteln
* Seite zum Üben: **sass.js.org**
* Bsp:
```css
@import "_variables"; /* $size: blue */
@import "_demo"; 

.selector {
    margin: $size /* Variable benutezen */

    .nested { /* Verschachtelung => .selector .nested */
        margin: $size / 2
    }
}
```
#### 6 - webpack
* TS-Dateien zu Packages zu machen
* Früher hat man mit `link` - viele .js importiert
* WebPack - statische Inhalte verpacken => wird zu JS-Package. => optimierter Ladeprozess
* Doku: webpack.js.com
#### 7 - Jasmine
* Unit-Tests durchführen:
    1. verhaltensorientiert Tests
#### 8 - Karma
* Test-runner
* JS-Unittests steuern = wie protokoliert, wie durchgeführt werden soll
* von Angular => optimiert für Angular
* kann in CI integriert werden
#### 9 - Protractor
* für E2E-Test basiert auf Selenium
* Klicks und Eingabe simulieren

### 4 - Polyfills und Vendors
#### 1 - Was sind Polyfills
* JS-Datien.
* überprüfen, ob Browser bestimmte Funktionen unterstützt, und entsprechende Workarounds ausführt -> kann eventuell aber nicht alle Funktionen workarounden
#### 2 - core-js
* ist Polyfill -> ES6 für alte Browser zu simulieren
* ist Bib auf github
#### 3 - web-animations
* Angular-Animation braucht **Web Animations API** braucht
* simuliert diese API
#### 4 - Zone.js
* nicht so ganze verstanden habe, wozu
* ABER ist wichtiger Teil von Angular
* manipuliert auf Low-Level den Browser
* ist auch ein wichtiger Tool für Projekte ohne Angular
#### 5 - RxJS
* = ReactiveX - für asynchrone Prozesse
* RxJS ist ReactiveX für JS-Welt
* sollte man sich anschauen -> ist mächtiges Framework

### 5 - Angular-Module im Überblick
#### 1 - core
* `@angular/core` - Kern-Funktionen von Angular
    1. Komponenten und Direktiven implementiert
    2. Pipes implementiert
    4. Dependency Injection implementiert
#### 2 - common
* `@angular/common` - 
    1. `BrowserModule` - ist Ableitung von CommonModule
    2. `CommonModule`
        1. Direktiven (`ngIf`)
        2. verschiedne Pipes (`date`)
#### 3 - compiler
* für JIT = erzeugt zur Laufzeit im Browser Code und verschmilzt Logik- und Darstellungsschicht
* compiler wird von `platform-browser-dynamic` - angeschmießen.
    
#### 4 - platform-browser und dynamic
* `@angular/platform-browser`
* braucht jede Angular-Anwendung
* steuert Browse und DOM-Elemente zum Rendern <- wird dann APP übergeben
* ist von JIT oder AOT abhängig
    * `platform-browser` - AOT
    * `platform-browser-dynamic` - JIT 
#### 5 - platform-webworker und dynamic
* alternative zu **platform-webworker**
* **platform-browser** läuft als Single-Thread (Rendering und anderer JS-Code)
* **platform-webworker** startet mehrere Worker, die mit Arbeit gefühtert werden
* ist von JIT oder AOT abhängig
    * `platform-webworker` - AOT
    * `platform-webworker-dynamic` - JIT 
#### 6 - platform-server
* = Angular-Universal
* ermöglicht Universal-Angular-Anwendungen zu erstellen
* ermöglicht, dass Angular auf Node.js läuft, compiliert alles da. ~ läuft als Server-Anwendung
    * kleinere Ladezeiten
    * Kürzere Startup-Zeit
    * Perfekt für Bots
#### 7 - http
* für Server-Client-Kommunikation
* `@angular/http` - Import über HttpModule
* stellt Service bereit, um XHR-Request zu unterstützen 
#### 8 - forms
* `@angular/forms`
* Zweie Form-Module: `FormsModule`-Vorlagen-getrieben `ReactiveFormsModule`-Reaktiv
#### 9 - router
man braucht für Single-Page-Application `RouterModule`
* = Konfiguration (welcher Pfad, welcher Comp) und Steuern von Routen
#### 10 - animate
* `@angular/animate` -> `BrowserAnimationModule`
* = Brücke zu Web-Animation-API