# Module Kopmonente Bindungen

## 1 - Projektdateien zum Training

### 1 - mit den Projektdateien arbeiten

* <https://github.com/netTrek/LinkedIn_Angular_Grundlagen> - ist in Branches organisiert
* zum Branch wechseln
* `npm install`
* `ng serve`

### 2 - mit Updates und neuen Versionen umgehen

* `ng --version` - im Projekt und global ausführen
* auf update.angular.io gehen und anschauen, wie man globalen und Pojekt Angular updatet.

## 2 - Grundlagen zu Modulen

### 1 - Was sind Module

* Angular ist Modular aufgebautet
* = Funktionalitäten kapseln
* Module ~ Container
  * Komponente, Direktive, Pipes, Service
  * imports, exports
* => Wiederverwendung in andreren Projekten

### 2 - Wie funktioneren Module

* ModulA:
  * KomponenteA
  * KomponenteB
  * => Komponenten können innerhalb des Modul mit einander reden/benutzen
  * export von KomponenteA
* ModulB:
  * KopmonenteC
  * import von KomponentA

### 3 - Angular-Module kennenlernen

* Überblick der Angular-Module:
    1. BrowserModule (Events, DOM-Rendering) -> importiet CommonModule per Defautl
    2. CommonModule (Direktiven, Pipes) - häufige Funktionen in Form von ng-Direktiven, Pipes, Sprachabhängige Module
    3. HttpModule(XHR) - HTTP-Requests/Response (hat auch Tests)
    4. FormsModule + ReactiveFormsModule
    5. RouterModule (Komponenten-Router) - Single-Page-App

## 3 - Module erstellen und verwenden

### 1 - Modul anlegen

* Modul-Klasse (ts)
  *`export class ModuleName`
  * Klasse muss keinen Code beinhalten, ist nur Container => stattdessen Metainfo einfügen:
    * `@NgModule ({ meta }) export class ModuleClasse` - ModulKlasse decorieren. Wichtige meta-Datan:
      * `imports` = welche Module dieses nutzt
      * `declarations` - List mit enthaltenen Komponenten, Direktiven, Pipes
      * `providers` - Services, die mit diesem Moduel bei der App registrierte werden
      * `exports` - welche Elements aus `declaratons` exportiert werden sollen (außer Service)
        * `bootstrap` - Liste von Kompontenten/Element mit den Angular-App starten soll (meistens nur eine Komponente)

### 2 - Start der Anwendung

* startet mit `main.ts`
  * wird entweder `platformBrowser()` oder `platformBrowserDynamic()` aufgefurfen (JIT oder AOT)
    * ruft `bootstrapModule(AppModule)` auf - startet Angular-App (muss als Param AppModul haben)
      * `AppModule` muss Attribute `boostrap: [AppComponente]` haben. `bootstrap` definiert eigentlich wie der Tag heißt, der Angular-Sachen ausführen soll
        * hat Verweis auf `index.html` -> `<app-rot>`

### 3 - Anwendungs-Modul

* `ng serve`
* `AppModule` hat als import `BrowserModule` = um mit dem Browser zu reden
* `bootstrap` sagt, welche von den `declarations` soll gestartet werden
* `AppComponent` - hat `selector: in.root` 

### 4 - Neue Module anlegen

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

### 5 - Modul mit Komponenten importieren

* in `lala` Kompoente erstellen:
  1. `ng g component lala/COMPNAME`
  2. dann noch in `MODULNAME` die `COMPNAME` exportieren
  3. in `app.module.ts` `MODULENAME`importieren

## 4 - Grundlagen zu Komponenten

### 1 - Was ist eine Komponente

* Komponente = HTML-Knoten:
  1. Logik = .js-Code
  2. HTML = HTML-Vorlage
  3. CSS-Style
  4. kann dann Kind-Komponenten verwenden

### 2 - Wie funktioniert Komponenten

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

### 3 - Komponentenbasierte Entwicklung

* Komponente = ein UI-Element
* Root: index.html
  * App-Komp: Vorlage
    * Kind-Komp: Vorlage
    * Kind-Komp: Vorlage
      * Kind-Komp: Vorlage
      * Kind-Komp: Vorlage

## 5 - Komponenten erstellen und answenden

### 1 - Wie erstellt man Komponenten

* Basis der Komponente ist Logik = TS-Klasse
* Klasse mit Metadaten versehen `@Component({Meta-Data})`-Decorator

### 2 - Komponenten anlegen und deklarieren

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

### 3 - Komponenten-Vorlagen

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

### 4 - Komponenten-Styles

* Component CSS zuweisen

```ts
@Component({
    selector: 'in-user-list', //in das Präfix in festgelegt wurde
    templateUrl: './user-list.component.html',
    styles: [
        h1: {
            text-decoration: underline;
        }
        ul{
            list-style: none;
        }
    ]
})
export class UserListComponent(){
}
```

* besser direkt mit CSS-Datei: `comp-name.component.scss`
* SCSS kann man nutzen, da in `.angular.cli.json` steht: `default: {..., "styleExt": "scss", ...}`
  * => mits SASS Preprozessor arbeiten

```ts
...
 styles: [ './user-list.component.scss' ]
```

### 5 - Styles für Host

* globalen Style für ganze Componente
* oft wird HTML der Componente in div mit ID gepackt
* zwei bessere Lösungen
  1. in globalen SCSS-Datei Style für den Knoten (`selector:`) setzen
  
  ```css
  selector-name {
      display:block;
      background-color: #f1f1f1;
  }
  ```

  2. in Component SCSS alles machen + statt Component-Namen `:host` benutzen
  
  ```css
  :host {
      display:block;
      background-color: #f1f1f1;
  }
   ```

### 6 - Encapsulation-Modi

* = wie macht Anguler so, dass CSS der Component nur bei dieser Componente angewendet werden
  * dabei wird z.B aus `h1` `h1[_ngcontent-XY]` in am Ende produzierten CSS. auch die HTML Tag werden mit `ngXXX-XY` ergänzt.
* man kann auch diesen Enkapsulation Modus ändern:

```ts
@Component({
    selector: 'in-user-list', //in das Präfix in festgelegt wurde
    templateUrl: './user-list.component.html',
    styles: [ './user-list.component.scss' ],
    encapsulation: ViewEncapsulation.None
})
export class UserListComponent(){
}
```

1. `encapsulation: ViewEncapsulation.None` - keine Enkapsulation => eine `ngXXX-YZ`
2. `encapsulation: ViewEncapsulation.Native` - CSS-Info in Shadow-DOM gespeichert (vergleichbar wie WebComponentenen arbeiten) (man kann Schadow DOM nicht sehen (nur bei Developer Tools mit entsprechender Einstellungen)). ! Nicht alle Browser unterstützen Shadow DOM
3. `encapsulation: ViewEncapsulation.Emulated` - Standard

### 7 - Komponenten über CLI anlegen

* `ng generate component ordner/compName` dabei werden `.scss`, `.html`, `.ts` Datei erstellt + wird in Modul in dem die neue Componente bei `declarations: [..., compName]` eingetragen erstellt wird eingetragen
  * da es in `declarations:` eingetragen ist => kann man die Componenten in `declarations:` als Kinds-Componenten nutzen. ! Aber nicht zyklische Abhängigkeiten erstellen.

### 8 - Komponenten verschachteln

* deklarierten Componenten innerhalb des Modul + importierten Componenten kann man verschachteln.
* geschieht mittels `selector`- Namen
* Bsp:

## 6 - Lebenszyklen von Komponenten

### 1 - Was sind Lebenszyklen

* Phasen der Componenten:
  1. constructor
  2. ngOnChanges - wenn Componente Änderungen erfährt. Änderungen durch Bindungen realisiert z.B `<userList[data]="userList">` - `data` ist benutzerdefinierte Eigenschaft, Wert von `data` ändert sich gemäß dem gebundenen Wert `userList`. `ngOnChanges`-Methode = empfängt Info, was sich geändert hat.
  3. ngOnInit - Methode `ngOnInit` einbauen, wird nur ein Mal ausgeführt
  4. ngDoCheck - diese Phase mit `ngDoCheck` abfangen. = überpfüft, ob bestimmte Werte abhängig von Ereignis passiert ist, damit Rerendering machen kann.
    1. ngAfterContentInit (nur wenn Kinds-Componenten hat)
    2. ngAfterContentChecked (nur wenn Kinds-Componenten hat)
    3. ngAfterViewInit (nur wenn Kinds-Componenten hat)
    4. ngAfterViewChecked (nur wenn Kinds-Componenten hat)
  5. ngOnDestroy - wenn Componente nicht mehr angezeigt werden soll, Angular zerstört dann alle Abhängikeiten

* man kann mit entsprechenden Methoden in diese Phasen eingreifen.

### 2 - Konstruktor und OnInit

1. Constructor => in `constructor()` eigenes Zeugs in dieser Phase realiseren
2. ngOnInit: die Klasse/Componente muss `OnInit` implementieren:

```ts
import {OnInit} from '@angular/core'
@Component({
    selector: 'in-user-list', //in das Präfix in festgelegt wurde
    templateUrl: './user-list.component.html',
    styles: [ './user-list.component.scss' ],
    encapsulation: ViewEncapsulation.None
})
export class UserListComponent() implements OnInit{
    constructor(){
        console.log("Consturcor");
    }

    ngOnInit(): void {
        console.log("OnInit Phase");
    }
}
```

### 3 - AfterViewInit

* mit Browser Plugin `Augury` Aufbau der Angular-Anwendung ansehen
* eigentlich checken ob `ngOnInit` der Kinder der Componten fertig sind. Wird eignetlich nach `ngOnInit` von Kindern aufgerufen
* muss `AfterViewInit` implementieren

```ts
import {OnInit, AfterViewInit} from '@angular/core'
@Component({
    selector: 'in-user-list', //in das Präfix in festgelegt wurde
    templateUrl: './user-list.component.html',
    styles: [ './user-list.component.scss' ],
    encapsulation: ViewEncapsulation.None
})
export class UserListComponent() implements OnInit, AfterViewInit{
    constructor(){
        console.log("Consturcor");
    }

    ngOnInit(): void {
        console.log("OnInit Phase");
    }
    ngAfterViewInit(): void {
        console.log('AfterViewInit von Parent'); 
    }
}
```

#### 4 - DoCheck and AfterViewChecked

* kontrollieren ob was geändert hat und rerendern.

```ts
import {OnInit, AfterViewInit, DoCheck} from '@angular/core'
@Component({
    selector: 'in-user-list', //in das Präfix in festgelegt wurde
    templateUrl: './user-list.component.html',
    styles: [ './user-list.component.scss' ],
    encapsulation: ViewEncapsulation.None
})
export class UserListComponent() implements OnInit, AfterViewInit, DoCheck, AfterViewCheck{
    constructor(){
        console.log("Consturcor");
    }

    ngOnInit(): void {
        console.log("OnInit Phase");
    }
    ngAfterViewInit(): void {
        console.log('AfterViewInit von Parent'); 
    }

    ngDoCheck(): void {
        console.log('DoCheck ausgeführt');
    }

    ngAfterViewCheck(): void { //wird nach dem DoCheck der Kinder ausgeführt d.h. etwas machen, wenn alle Kinder aktualisiert wurden.
        console.log('AfterViewCheck');
    }
}
```

* mit Augury kann man DoCheck erzwingen. z.B wenn man die Klassen Attr. in Augury ändert

### 5 - OnDestroy

* in .html `<in-comp-name *ngIf="showCompInfo"></in-comp-name>`. Die Componente wird nur dan eingebunden, wenn Attr. `showCompInfo = true` ist.

```ts
import {OnDestroy} from '@angular/core'
@Component({
    selector: 'in-user-list', //in das Präfix in festgelegt wurde
    templateUrl: './user-list.component.html',
    styles: [ './user-list.component.scss' ],
    encapsulation: ViewEncapsulation.None
})
export class UserListComponent() implements OnDestroy{
    constructor(){
        console.log("Consturcor");
    }

    ngOnDestroy(): void {
        console.log("Destroy Phase");
    }
}
```

## 7 - Grundlagen zu Bindungen
### 1 - Was sind Bindungnen

* `{{xxx}}` - Ausdrucksinterpolation. geht auch Methode zu binden: `{{getName()}}`
* (ereignisName) - Methode an Ereignis binden
* `<img [src]="imgPath">` - Eigenschaften binden = HTML-Eigenschaften binden
* `<img [attr.alt]="imgAlt">` - als Attribut binden. Attribut-Wert im DOM binden. An `<img alt>` im DOM binden

### 2 - Ausdrücke interpolieren

* `{{ 'string' }}` - geht auch mit statischen Werten, macht aber keinen Sinn
* Bsp:

```html
<h1>{{ name }}</h1>
```

```ts
import {OnDestroy} from '@angular/core'
@Component({
    selector: 'in-user-list', //in das Präfix in festgelegt wurde
    templateUrl: './user-list.component.html',
    styles: [ './user-list.component.scss' ],
    encapsulation: ViewEncapsulation.None
})
export class UserListComponent(){
    //public
    //name="John"

    //private
    private _name = 'John';

    constructor(){
        console.log("Consturcor");
    }

    get name(): string{
        return this._name
    }

    set name(value: string): void{
        this._name = value;
    }
}
```

### 3 - Eigeschaften binden

* man kann DOM Elemente in .ts Dateien erzeugen z.B hier in main.ts

```ts
let div: HTMLDivElement = document.createElement('div') as HTMLDivElement;
div.innerHTML = '<h1>my Div</h1>';
document.body.appendChild(div);
```

* Bsp:

```ts
htmlContent = '<p>Lalal</p>'

imgPath='/assets/img/lala.png';
```

```html
<div [innerHtml]="htmlContent"></div>
<img [src]="impPath">
```

### 4 - Attribute binden

* Attribute von HTML z.B `alt` bei `<img>`
* HTML-Attribute kann man ähnlich wie HTML-Eigenscahften binden
* Bsp:

```ts
htmlContent = '<p>Lalal</p>'

imgPath='/assets/img/lala.png';

altLabel="Alt Label";
```

```html
<div [innerHtml]="htmlContent"></div>
<img [src]="impPath" [attr.alt]="altLabel">
```

* eigentlich ist `src` ist auch ein Attribute also auch mit `[attr.src]` bindbar.
* Tipp: Attribute binden man z.B für `aria-XXX` (Barriere-freies Internet)

#### 5 - Styles binden

* ähnlihch wei Eigenschaftsbindungen
* Bsp:

```ts
htmlContent = '<p>Lalal</p>'

imgPath='/assets/img/lala.png';

fontColor='red';
```

```html
<div [innerHtml]="htmlContent"></div>
<img [src]="impPath">

<h3 style="color:red">{{ name }}</h3>
<h3 [style.color]="fontColor">{{ name }}</h3>
```

### 6 - Styles mit Einheit binden

```ts
fontSize1 = 1.2;
```

```html
<h3 [style.fontSize]="fontSize1 + 'em'">
<h3 [style.fontSize.em]="fontSize1">
```

#### 7 - Style-Klassen binden

```css
.class-name1{
    color: lightgrey;
}

.class-name2{
    color: red;
}
```

```ts
classNameStyleClass='class-name1';
```

```html
<h3 class="class-name"></h3>

<h3 [class]="classNameStyleClass">Lala</h3>
```

* !. wenn man normale Klassen auch benutzen will, werden sie von `[class]` überschrieben. Also ist nicht additiv.

### 8 - Style-Klassen konditional binden
```css
.class-name1{
    color: lightgrey;
}

.class-name2{
    color: red;
}
```

```ts
classNameStyleClass='class-name1';

get isAdminUser():boolean{
    return this.name === 'John';
}
```

```html
<h3 class="class-name"></h3>

<h3 [class.class-name1]="true/false">Lala</h3>

<h3 [class.class-name1]="isAdminUser">Lala</h3>
```

#### 9 - Ereignisse binden

```html
<button (click)="name='Lala'">Lala</button>
<button (click)="funktName()">Lala</button>
```

* mit Intellisence werden die Vorschläge für `()` vorgeschlagen
* hier direkt Inline: bei Klick `name` auf `Lala` gesetzt

```ts
funktName() {
    if (this.name !== 'Peter Müller'){
        this.name='Peter Müller';
    }
    else{
        this.name='Lala';
    }
}
```

#### 10 - Ereignisinformationen transponieren

* mit `$event` in .html - das Ereginis an Funkt. übergeben z.B. bei Klick wird `MouseEvent` übergeben

```html
<button (click)="funktName($event)">Lala</button>
```

```ts
funktName(event: MouseEvent) {
    debugger; //Breakboint
    if (this.name !== 'Peter Müller'){
        this.name='Peter Müller';
    }
    else{
        this.name='Lala';
    }
}
```

### 8 - Dekoratoren binden

#### 1 - HostListener

* Decorator `@HostListener()` - wird direkt der Komponente zugewiesen. aus `core` importieren

```html


```

```ts
@HostListener('click')
funktName(event: MouseEvent){
    //
}
```

```css
/*eigentlich nicht das Theme*/
:host {
    display: block
    background-color: beige;
    &:hover {
        cursor: pointer;
    }
}
```

* `@Hostlistener('click')` braucht den Namen des Events auf den Hören soll

#### 2 - HostListener-Optionen

* weitere Optionen für HostListener
  1. als weitere Param kann man Liste übergeben
* auch Target angeben, also auf was Event sich beziehen soll anstelle des Default, also der Componente. Erlaubt Targets: `window`, `body`, `document`

```ts
@HostListener('click', ['$event', 'name'])
funktName(event: MouseEvent, name: string){
    //
}

@HostListener('window:resize', ['$event', 'name'])
funktName(event: Event, name: string){
    //
}
```

#### 3 - HostBinding

* CSS-Klasse auch über `host` binden
* Listener - Ereignis bindet
* Binding - Styles binden

```html
<h3>{{ name }}</h3>
```

```ts
import {OnDestroy} from '@angular/core'
@Component({
    selector: 'in-user-list', //in das Präfix in festgelegt wurde
    templateUrl: './user-list.component.html',
    styles: [ './user-list.component.scss' ],
    encapsulation: ViewEncapsulation.None
})
export class Lala {
    @HostBinding('class.class-name1')
    myVar: boolean = false
}
```

* also abhängig von myVar wir die CSS-Klasse gesetzt
* in CSS müssen die CSS-Eigenschaften in `:host` stehen
* hier muss man noch `myVar` toggeln, da sonst immer false

### 9 - Daten austauschen

#### 1 - Eltern-Kind-Kommunikation

* Bsp;
  * Eltern: `UserList`

    ```ts
    export class UserList{
        userList: User[];

        selectUser(user: User){
            //
        }
    }
    ```

    ``` html
    <!--ist Kind -->
    <user
        [userData]="userList[0]"
        [onSelect]="selectUser($event)"
    >
    ```
  
  * User ist Kind und erwartet Info, die hier `[userData]` ist, hat auch ein Ereignis `onSelect`
  * Damit die Eltern-Comp die Info aus Kind-Comp bekommt =>

    ```ts
    export class User{
        @Input()
        userData: User;
        @Output()
        onSelect: EventEmitter;
    }
    ```

  * wird von Attr oder Getter/Setter gesetzt

#### 2 - Input-Decorator

* ermölgicht Komp mit Attr versehen, das man an in Eletern Komp verädnert kann

```ts
import {Input} from '@angular/core'

@Component({
    selector: '...',
    templateUrl '...html',
    stryleUrls [ '...css' ]
});

export class UserNameComp {
    // 1
    @Input()
    name = 'Lala 00'
    //2
    @Input('username') //als Param kann man Namen definieren falls Name anders als Attr-Name sein sollte
    name = 'Lala 01'
    //3
    get name (): string{
        return this _name;
    }
    set name(value: string){
        console.log(value);
        this._name = vale;
    }



    userNameStyleClass
}
```

```html
<in-user-name name="Lala 01"></in-user-name>

<in-user-name username="Lala 02"></in-user-name> <!--falls Attr-Name anders sein sollte>
```

#### 3 - Input-Eigenschaften binden

* Eigenschft einer Kind-Komp über Eltern-Komp binden

```html user.html
<h1>User List</h1>
<in-user-name name="Lala 00"></in-user-name>
<in-user-name [name] ="user1"></in-user-name>
<in-user-name [name] ="user2"></in-user-name>
<in-user-name></in-user-name> <!--für name wird Default-Wert genommen-->
```

```ts user-list-component.ts (ist Eltern-Komp)
//1
export class UserListComp{
    user1 = "Lala01";
    user2 = "Lala02";
    user3 = "Lala03";

    constructor(){}
}

```

#### 4 - OnChanges

```html user.html
<h1>User List</h1>
<in-user-name name="Lala 00"></in-user-name>
<in-user-name [name] ="user1"></in-user-name>
<in-user-name [name] ="user2"></in-user-name>
<in-user-name></in-user-name> <!--für name wird Default-Wert genommen-->
```

```ts user-list-component.ts (ist Eltern-Komp)
//1
import {OnChanges, SimpleChanges} from '@angular/core'
export class UserListComp implements OnChanges{
    user1 = "Lala01";
    user2 = "Lala02";
    user3 = "Lala03";

    constructor(){}

    // diese Methode muss man überschreiben => wird aufgerufen,wenn Attr(-e) die @Input hat sich ändert
    ngOnChanges(changes: SimpleChanges): void{
        //
    }
}
```

#### 5 - Output-Decorator

* der Eltern-Komp sagen, das Kind-Komp etwas gemacht hat. => `@Output`

```html user.html
<h1>User List</h1>
<in-user-name name="Lala 00"></in-user-name>
<in-user-name [name] ="user1"></in-user-name>
<in-user-name [name] ="user2"></in-user-name>
<in-user-name></in-user-name> <!--für name wird Default-Wert genommen-->
```

```ts user-list-component.ts (ist Eltern-Komp)
//1
import {OnChanges, SimpleChanges} from '@angular/core'
export class UserListComp implements OnChanges{
    user1 = "Lala01";
    user2 = "Lala02";
    user3 = "Lala03";

    @Output() //auf Attr anwenden, das von Typ EventEmitter
    nameChanged: EventEmitter<string> = new EventEmmiter()//aus reactivX-Framework => dann als Ereignis-Stream senden

    constructor(){}

    // diese Methode muss man überschreiben => wird aufgerufen,wenn Attr(-e) die @Input hat sich ändert
    ngOnChanges(changes: SimpleChanges): void {
        //
    }

    //..
    chgName(event MouseEvent, name: string){
        //
        this.nameChanged.emit(this.name); // der Angular-Env etwas senden
    }
}
```

* hier muss noch die Eltern-Komp diese Nachricht empfangen

#### 6 - Benutzerdefinierte Ereignisse

* = in Eltern-Komp die EventEmmitter Sendung abfangen und verarbeiten
* Eltern:

```html user.html
<h1>User List</h1>
<in-user-name name="Lala 00"></in-user-name>
<in-user-name [name] ="user1"></in-user-name>
<in-user-name [name] ="user2" (nameChanged)='onNameChanged($event)'></in-user-name> <!--das ist die mit @Output markiertes EventEmitter-Attr -->
<in-user-name></in-user-name> <!--für name wird Default-Wert genommen-->
```

```ts user-list-component.ts (ist Eltern-Komp)
//1
import {OnChanges, SimpleChanges} from '@angular/core'
export class UserListComp implements OnChanges{
    user1 = "Lala01";
    user2 = "Lala02";
    user3 = "Lala03";

    @Output() //auf Attr anwenden, das von Typ EventEmitter
    nameChanged: EventEmitter<string> = new EventEmmiter()//aus reactivX-Framework => dann als Ereignis-Stream senden

    constructor(){}

    // diese Methode muss man überschreiben => wird aufgerufen,wenn Attr(-e) die @Input hat sich ändert
    ngOnChanges(changes: SimpleChanges): void {
        //
    }

    //..
    chgName(event MouseEvent, name: string){
        //
        this.nameChanged.emit(this.name); // der Angular-Env etwas senden
    }

    onNameChanged(newName: string){
        console.log(newName);
    }
}
```

#### 7 - User-List-Komponente

* Eltern: User-List

```ts
import { } from '@angular/core'

@Component({
    selector: 'in-user-list',
    templateUrl: './user-list.component.html'
    styleUrl: [ './user-list.component.scss' ],
    encapsulation: ViewEncapsulation.Emulated,
})

export class UserListComponent implements OnInit{

    users: string[] = [
        'Lala1',
        'Lala2',
        'Lala3
    ];

    selectedUser: string;

    onSelectedUser(selectedUserName:string){
        this.selectedUser = selectedUserName
    }
}
```

```html
<h1>User List - {{ selectedUserName }} </h1>
<in-user-name [name]="users[0]" [isSelected]="selectedUserName===user[0]" selectUsr="OnSelectedUser($event)"></in-user-name>
<in-user-name [name]="users[1]" [isSelected]="selectedUserName===user[1]" selectUsr="OnSelectedUser($event)"></in-user-name>
<in-user-name [name]="users[2]" [isSelected]="selectedUserName===user[0]" selectUsr="OnSelectedUser($event)"></in-user-name>
```

* Kind: User-Name

```ts
import { Component, EventEmitter, HostBinding, HostListener, Input, OnInit, Output } from '@angular/core';

@Component ( {
  selector   : 'in-user-name',
  templateUrl: './user-name.component.html',
  styleUrls  : [ './user-name.component.scss' ]
} )
export class UserNameComponent implements OnInit {

  @Output ()
  selectUser: EventEmitter<string> = new EventEmitter ();

  get name (): string {
    return this._name;
  }

  @Input ()
  set name ( value: string ) {
    if ( value.trim () !== '' ) {
      this._name      = value;
    }
  }

  private _name = 'Lala;

  @Input()
  @HostBinding ( 'class.user-name' )
  isSelected = false;

  constructor () {
  }

  ngOnInit () {
  }

  @HostListener ( 'click' [ '$event', '_name'] )
  selectUser () {
    this.selectUsr.emit ( this.name );
  }
}

```
