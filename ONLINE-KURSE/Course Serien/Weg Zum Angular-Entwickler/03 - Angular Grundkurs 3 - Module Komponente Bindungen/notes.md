### 1 - Projektdateien zum Training
#### 1 - mit den Projektdateien arbeiten
* github.com/netTrek/LinkedIn_Angular_Grundlagen
* zum Branch wechseln
* `npm install`
* `ng serve`
#### 2 - mit Updates und neuen Versionen umgehen
* `ng --version` - im Projekt und global ausführen
* auf update.angular.io gehen und anschauen, wie man globalen und Pojekt Angular updatet.

### 2 - Grundlagen zu Modulen
#### 1 - Was sind Module
* Angular ist Modular aufgebautet
* = Funktionalitäten kapseln
* Module ~ Container
    * Komponente, Direktive, Pipes, Service
    * imports, exports
* => Wiederverwendung in andreren Projekten
* 
#### 2 - Wie funktioneren Module
+ ModulA:
    * KomponenteA
    * KomponenteB
    * => Komponenten können innerhalb des Modul mit einander reden/benutzen
    * export von KomponenteA
* ModulB:
    * KopmonenteC
    * import von KomponentA
#### 3 - Angular-Module kennenlernen
* Überblick der Angular-Module:
    1. BrowserModule (Events, DOM-Rendering) -> importiet CommonModule per Defautl
    2. CommonModule (Direktiven, Pipes) - häufige Funktionen in Form von ng-Direktiven, Pipes, Sprachabhängige Module
    3. HttpModule(XHR) - HTTP-Requests/Response (hat auch Tests)
    4. FormsModule + ReactiveFormsModule
    5. RouterModule (Komponenten-Router) - Single-Page-App


### 3 - Module erstellen und verwenden
#### 1 - Modul anlegen
* Modul-Klasse (ts)
    + `export class ModuleName`
    * Klasse muss keinen Code beinhalten, ist nur Container => stattdessen Metainfo einfügen:
        * `@NgModule ({ meta }) export class ModuleClasse` - ModulKlasse decorieren. Wichtige meta-Datan:
            * `imports` = welche Module dieses nutzt
            * `declarations` - List mit enthaltenen Komponenten, Direktiven, Pipes
            * `providers` - Services, die mit diesem Moduel bei der App registrierte werden
            + `exports` - welche Elements aus `declaratons` exportiert werden sollen (außer Service)
            * `bootstrap` - Liste von Kompontenten/Element mit den Angular-App starten soll (meistens nur eine Komponente)
#### 2 - Start der Anwendung
* startet mit `main.ts`
    * wird entweder `platformBrowser()` oder `platformBrowserDynamic()` aufgefurfen (JIT oder AOT)
        * ruft `bootstrapModule(AppModule)` auf - startet Angular-App (muss als Param AppModul haben)
            * `AppModule` muss Attribute `boostrap: [AppComponente]` haben. `bootstrap` definiert eigentlich wie der Tag heißt, der Angular-Sachen ausführen soll
                * hat Verweis auf `index.html` -> `<app-rot>`
#### 3 - Anwendungs-Modul
* `ng serve`
* `AppModule` hat als import `BrowserModule` = um mit dem Browser zu reden
* `bootstrap` sagt, welche von den `declarations` soll gestartet werden
* `AppComponent` - hat `selector: in.root` 
#### 4 - Neue Module anlegen
1. Manuell anlegen:
    1. Ordne anlegen `lala`
    2. Datei `lala/lalaModule.ts` erzeugen:
    ```ts
    import {NgModule}

    @NgModule [{
        imports: [
            CommonModule //Direktiven, Pipes
        ]
    }]
    export class LalaModule{}
    ```
    3. NG-CLI: `ng g module MODULNAME`
    
#### 5 - Modul mit Komponenten importieren
* in `lala` Kompoente erstellen:
    1. `ng g component lala/COMPNAME`
    2. dann noch in `MODULNAME` die `COMPNAME` exportieren
    3. in `app.module.ts` `MODULENAME`importieren
### 4 - Grundlagen zu Komponenten
#### 1 - Was ist eine Komponente
* Komponente = HTML-Knoten:
    1. Logik = .js-Code
    2. HTML = HTML-Vorlage
    3. CSS-Style
    4. kann dann Kind-Komponenten verwenden
#### 2 - Wie funktioniert Komponenten
* Logik: = TS-Klasse
```ts
export class UserComponent {
    name = "Lala";
    chgName (){
        this.name = "Lala2"
    }
}
```
* HTML-Vorlage = View
```html
<h1>{{ name }}</h1>
<button (click)="chgName()">Ändern</button>
```
* CSS-Style
* am Ende macht Angular daraus eine Datei = Komponente
#### 3 - Komponentenbasierte Entwicklung
* Komponente = ein UI-Element
* Root: index.html
    * App-Komp: Vorlage
        * Kind-Komp: Vorlage
        * Kind-Komp: Vorlage
            * Kind-Komp: Vorlage
            * Kind-Komp: Vorlage
### 5 - Komponenten erstellen und answenden
#### 1 - Wie erstellt man Komponenten
* Basis der Komponente ist Logik = TS-Klasse
* Klasse mit Metadaten versehen `@Component({Meta-Data})`-Decorator
#### 2 - Komponenten anlegen und deklarieren
* Bsp: User-Komponente erstellen
* Kopmonente = Ordner:
    1. Order erstellen `user-list` (Kebab-Style-Namen)
    2. in diesem Order `user-list.component.ts` erstellen
    ```ts
    @Component({
        selector: 'in-user-list', //in das Präfix in festgelegt wurde
        template: '', //hier HTML-Vorlage
    })
    export class UserListComponent(){
        
        constructor(){
            console.log("Hello User-List")
        }
    }
    ```
    3. in `user.module.ts` bei `declartion` und `exrpots` `UserListComponent` eintragen 
    4. in `app.component.html` noch eintragen `<in-user-list></in-user-list>`
#### 3 - Komponenten-Vorlagen
```ts
    @Component({
        selector: 'in-user-list', //in das Präfix in festgelegt wurde
        templateUrl: './user-list.component.html', 
    })
    export class UserListComponent(){
        
        constructor(){
            console.log("Hello User-List")
        }
    }
    ```
#### 4 - Komponenten-Styles
#### 5 - Styles für Host
#### 6 - Encapsulation-Modi
#### 7 - Komponenten über CLI anlegen
#### 8 - Komponenten verschachteln

### 6 - Lebenszyklen von Komponenten
#### 1 - Was sind Lebenszyklen
#### 2 - Konstruktor und OnInit
#### 3 - AfterViewInit
#### 4 - DoCheck and AfterViewChecked
#### 5 - OnDestroy

### 7 - Grundlagen zu Bindungen
#### 1 - Was sind Bindungnen
#### 2 - Ausdrücke interpolieren
#### 3 - Eigeschaften binden
#### 4 - Attribute binden
#### 5 - Styles binden
#### 6 - Styles mit Einheit binden
#### 7 - Style-Klassen binden
#### 8 - Style-Klassen konditional binden
#### 9 - Style-Klassen konditional binden
#### 10 - Ereignisse binden
#### 11 - Ereignisinformationen transponieren

### 8 - Dekoratoren binden
#### 1 - HostListener
#### 2 - HostListener-Optionen
#### 3 - HostBinding

### 9 - Daten austauschen
#### 1 - Eltern-Kind-Kommunikation
#### 2 - Input-Decorator
#### 3 - Input-Eigenschaften binden
#### 4 - OnChanges
#### 5 - Output-Decorator
#### 6 - Benutzerdefinierte Ereignisse
#### 7 - User-List-Komponente
