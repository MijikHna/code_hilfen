# 4 - Angular Grundkurs - Dependency Injection, Directiven Bindungen

## 1

* die Übung ist in Branchens organisiert.
* <https://github.com/netTrek/LinkedIn_Angular_Vertiefung>
* eventuell bei Angular updates die Angular-Update-Seite besuchen und Hinweise durchlesen

## 2 - Grunlagen zu Direktiven

### 1 - Was ist Direktive

* Funktionserweiterung für HTML-Element
* werden in HTML-Elementen als HTML-Elemente eingetragen
* zwei Typen
  1. strukturelle Direktiven = manipuliert den DOM -> fangen mit `*` an. Bsp: `<img *ngIf="showImg">` - zeigt `<img>` nur an wenn `showImg=true` ist, wobei man statt `showImg` direkt einen Vergleich machen kann
  2. Attribut-Direktive = Aussehen + Verhalten des HTML-Elem manipulieren

### 2 - Wie wendet man Direktiven an

* Bsp1: `<input matInput>` = hier ist `matInput`-Attribut = Direktive
* Bsp2: `<textarea matAutosizeMinRows="2">` - Attr-Direktive mit Wertzuweisung. `matAutosizeMinRows`-Direktive von Material-Design = Textarea 2 Zeile groß sein soll.
* Bsp3: `<input [ngClass]="inputClass">` - Attr-Direktive mit gebundener Wertzuweisung = Wertzuweisung über eine Bindung. `[]` represäntieren eine Bindung einer Eigenschaft

## 3 - Hauseigene Direktiven nutzen

### 1 - ngIf

```html

<!-- in *inIf kann beliebiger Vergleich stehen -->
<img  *ngIf="true" src="../assets/img/linkedin-logo.png" alt="logo">

<img  *ngIf="showImg" src="../assets/img/linkedin-logo.png" alt="logo">

<img  *ngIf="1 === 1" src="../assets/img/linkedin-logo.png" alt="logo">

<img  *ngIf="1 !== 1" src="../assets/img/linkedin-logo.png" alt="logo">

<!-- also wenn showImg true ergibt => wird angezeigt-->
<img  *ngIf="showImg" src="../assets/img/linkedin-logo.png" alt="logo">

 <button (click)="toggle()">toggle</button>

```

```ts
// ..

showImg = true;

// Bild wird angezeigt in dem showImg true/false mit toggle() gesetzt wird
toggle() {
    this.showImg = !this.showImg;
  }

//
```

### 2 - ngTemplate mit ngIf

* mit `*`sagt man dem Compiler war er damit machen soll
* eigentlich wird *ngTemplate mit ngIf erzeugt wird

```html
<!-- da es nur Template ist wird es von Compiler ignoriert, da nur Vorlage die ein/ausgeblendet wird-->
<ng-template>
  <img  src="../assets/img/linkedin-logo.png" alt="logo">
</ng-template>


<!-- Template mit ngIf-Bidnung versehen -->
<ng-template [ngIf]="showImg">
  <img  src="../assets/img/linkedin-logo.png" alt="logo">
</ng-template>
```

* also `*ngIf` ist `<ng-template [ngIf]="showImg">`

### 3 - ngifElse

```html
<!-- wenn showImg===true => zeigt diesen Block sonst elseBlock (= Reference auf einen ngTemplate-Block)
<img  *ngIf="showImg; else elseBlock" src="../assets/img/linkedin-logo.png" alt="logo">

<ng-template #elseBlock>
  <img  src="../assets/img/logo.png" alt="logo">
</ng-template>
```

### 4 - ngFor

* durch Liste iterieren.

```html user-list.component.html
<!--
<in-user-name [name]="users[0]"
              [isSelected]="selectedUsrName===users[0]"
              (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
<in-user-name [name]="users[1]"
              [isSelected]="selectedUsrName===users[1]"
              (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
<in-user-name [name]="users[2]"
              [isSelected]="selectedUsrName===users[2]"
              (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
<in-user-name [name]="users[3]"
              [isSelected]="selectedUsrName===users[3]"
              (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
-->

<!-- hier mit der Bindung name und age weitergegeben an user.name Componente, dabei wird auch <in-user-name>-Selector in ngFor erstellt -->
<in-user-name *ngFor="let user of users"
  [name]="user.name"
  [age]="user.age"
  [isSelected]="selectedUsrName===user"
  (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
```

```ts user-list.component.ts
export class UserListComponent implements OnInit{
  users: User[] = [
    { name: 'Frank Müller', age: 12},
    { name: 'Hans Müller', age: 13},
    { name: 'Peter Müller', age: 14},
    { name: 'Paul Müller', age: 15}
  ];

  selectedUsrName: string;

  constructor() { }
  ngOnInit() {  }

  onSelectedUsr ( selectedUsrName: string ) {
    this.selectedUsrName = selectedUsrName;
  }
```

```html user-name.component.ts
{{ name }} # {{age}}
```

``` ts user-name.component.ts
@Output ()
  selectUsr: EventEmitter<string> = new EventEmitter ();

  get name (): string {
    return this._name;
  }

  @Input ()
  set name ( value: string ) {
    if ( value.trim () !== '' ) {
      this._name      = value;
    }
  }

  @Input()
  age: number;

  private _name = 'Lala';

  @Input()
  @HostBinding ( 'class.user-name' )
  isSelected = false;

  constructor () {
  }

  ngOnInit () {
  }

  @HostListener ( 'click' )
  selectUser () {
    this.selectUsr.emit ( this.name );
  }
```

### 5 - ngFor Variables

* ngFor hat folgende Interne Variablen:
  1. index
  2. count = Länge des Arrays
  3. first = ob es erstes Element ist
  4. last
  5. middle
  6. even/odd = gerade order ungerade index

```html user-list.component.html
<!-- user wird an user-Obj gebunden + interne nFor-Variablen werden mittels Aliases nach außen gegeben + class .even binden, wenn e===true ist-->
<in-user-name *ngFor="let user of users; index as i count as c; even as e"
              [user]="user"
              [data]="i + ' ' + c + ' ' + 'isEven:' + e"
              [class.even]="e"
              (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
```

```ts user-list.component.ts
@Component ( {
  selector: 'in-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: [ './user-list.component.scss' ],
  encapsulation: ViewEncapsulation.Emulated
})
export class UserListComponent implements OnInit {

  users: User[] = [
    { name: 'Frank Müller', age: 12},
    { name: 'Hans Müller', age: 13},
    { name: 'Peter Müller', age: 14},
    { name: 'Paul Müller', age: 15}
  ];

  selectedUsr: User;

  constructor() { }
  ngOnInit() {  }

  onSelectedUsr ( selectedUsr: User) {
    this.selectedUsr = selectedUsr;
  }
}
```

```html user-name.component.html
<span class="user-age">{{ user.age }}</span>
<span class="user-name">{{ user.name }}</span>
<span class="user-data"
  *ngIf="data">[{{data}}]</span>
```

```ts user-name.component.ts
@Component ( {
  selector   : 'in-user-name',
  templateUrl: './user-name.component.html',
  styleUrls  : [ './user-name.component.scss' ]
} )
export class UserNameComponent implements OnInit {

  @Output ()
  selectUsr: EventEmitter<User> = new EventEmitter ();

  @Input ()
  user: User;

  @Input ()
  data: any;

  @Input ()
  @HostBinding ( 'class.user-name' )
  isSelected = false;

  constructor () {
  }

  ngOnInit () {
  }

  @HostListener ( 'click' )
  selectUser () {
    this.selectUsr.emit ( this.user );
  }
}
```

### 6 - ngTemplate mit ngFor

* ngFor mit ngTemplate benutzen

```html user-list.html
<!-- dem Template Namen ngFor geben + ngForOf-Directive benutzen die Variable users benutzen, Variablen sind. user = let-user; even = let-e -->

<ng-template ngFor [ngForOf]="users" let-user let-e="even">
  <in-user-name [user]="user"
                [isSelected]="selectedUsr===user"
                [class.even]="e"
                (selectUsr)="onSelectedUsr ( $event )"
  ></in-user-name>
  <hr>
</ng-template>
```

* diese Vorgehensweise, wenn man komplexere For-s machen möchte

### 7 - ngSwitch

```html
<div [ngSwitch]="company">
  <img *ngSwitchCase="'netTrek'" src="../assets/img/logo.png" alt="netTrek">
  <img *ngSwitchCase="'github'" src="../assets/img/github.png" alt="github">
  <img *ngSwitchDefault="" src="../assets/img/linkedin-logo.png" alt="linkedIn">
</div>
```

* in .ts wird es dann Variable `company` geben

### 8 - ngContainer mit ngSwitch

* eigentlich nicht immer gut `<div>`s für strukturele Direktiven zu nutzen. Bessere Lösung einen Container zu nutzen

```html
<ng-container [ngSwitch]="company">
  <img *ngSwitchCase="'netTrek'"
    src="../assets/img/logo.png" alt="netTrek">
  <img *ngSwitchCase="'github'"
    src="../assets/img/github.png" alt="github">
  <img *ngSwitchDefault=""
    src="../assets/img/linkedin-logo.png"alt="linkedIn">
  </ng-container >
```
### 9 - ngClass

```html
<!-- class binden -->
<in-user [class]="class2bind"></in-user>

<!-- Problem, dass class="beweis" komplet ignoriert wird (überschrieben)--->
<in-user class="beweis" [class]="class2bind"></in-user>

<!-- Lösung  ngClass ist additiv + unterstützt Bedingugnen -->
<in-user class="beweis" [ngClass]="class2bind"></in-user>

<!-- Klasse even Binden, wenn e===true ist + wird als Objekt an ngClass gebunden -->
<in-user-name *ngFor="let user of users; even as e; odd as o"
              [user]="user"
              [isSelected]="selectedUsr===user"
              [ngClass]="{even: e, odd: o}"
              (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
```

### 10 - ngStyle

```html
<in-user
    [style.color]="fontColor"
    [style.fontSize.em]="fontSiez"
  ></in-user>

<in-user
    [ngStyle]="{'color': fontColor, 'fontSize.em': fontSize}"
  ></in-user>

<in-user
    [ngStyle]="styleObj"
  ></in-user>
```

```ts

styleObj = {
  'colorÄ': 'red',
  'font-size': '1 em',  
}
```

## 4 - Direktiven erstellen und nutzen

### 1 - Direktiven erzeugen

* Schritte:
  1. `export class NameDirective` - Klasse anlegen
  2. davor die Directive: `@Directive({/*MetaDaten*/})` setzen. Metadaten:
      1. `selector` = CSS-Selector für HTML-Attribute`[appDirName]`, `.appClass`. HTML-Elemente
  3. die Direktive im Modul deklarieren, in der man sie nutzen will
* Bsp:

```ts
import { Directive } from '@angular/core';

@Directive ( {
  selector: '[inHover]' //wenn man jetzt in HTML-Element inHover alt Attr. setzen wird diese Direktive angewendet auf dieses Element
})
export class HoverDirective {
  constructor () {
    console.log ( 'dir hover' );
  }
}
```

```html
<in-user-list inHover></in-user-list>
```

### 2 - Direktiven über CLI anlegen

* Schritte:
  1. `ng generate module utils`
  2. `ng generate directive utils/hover --export` auch Direktive über Modul exportieren
  3. dieses Modul dann in entsprechenden Modulen importieren

* jetzt kann man die Directive `inHover` als HTML-Attr. benutzen wie z.B `*ngIf`

### 3 - Elements mit Direktiven erweitern

```ts inHover.directive.ts
import { Directive, ElementRef, Renderer2 } from '@angular/core';

@Directive ( {
  selector: '[inHover]'
} )
export class HoverDirective {

  // hier in constructor die Dependency Injection (muss Typ haben)
  constructor ( elem: ElementRef, renderer: Renderer2 ) {
    console.log ( 'inHover' , elem );

    // Farbe ändern
    // elem.nativeElement.style.color = 'red'; //Könnte Probleme haben, wenn man die Anwendung nicht im Browser, sondern auf dem Server laufen hat. Server kennt keinen DOM => über Render2 -Klasse-Obj
    renderer.setStyle( elem.nativeElement , 'color', 'red');
  }
}
```

### 4 - Direktiven-Werte übermitteln

* = Parameter an Directive übergeben, geschieht über `="XYZ"`

```html app.module.html
<div>
  <h1 inHover="green">
    Welcome to {{ title }}!
  </h1>
  <!-- Bsp mit der Bindung (fontColor) ist Variable in app.component.ts-->
  <h2 [inHover]="fontColor">saban</h2>
  <h2 inHover="blue">ünlü</h2>

  <in-user></in-user>
</div>
```

```ts inHover.directive.ts
@Directive ( {
  selector: '[inHover]'
} )
export class HoverDirective implements OnInit{

  //1 Variante 1
  @Input() // um Parameter zu übergeben
  inHover: string;

  //2 Variante 2
  get inHover (): string {
    return this._inHover;
  }
  @Input() // um Parameter zu übergeben
  set inHover ( value: string ) {
    if ( value.trim() !== '' ) {
      this._inHover = value;
      this.renderer.setStyle( this.elem.nativeElement , 'color', this._inHover);
    }
  }


  private _inHover: string;

  constructor ( private elem: ElementRef, private renderer: Renderer2 ) {
  }

  // für einen Standard-Wert (red) für _inHover
  ngOnInit (): void {
    if ( this._inHover === undefined ) {
      this.renderer.setStyle( this.elem.nativeElement , 'color', 'red');
    }
  }
}
```

### 5 - Direktiven mit HostBindings

```ts inHover.directive.ts
@Directive ( {
  selector: '[inHover]'
} )
export class HoverDirective implements OnInit {

  get inHover (): string {
    return this._inHover;
  }

  @Input ()
  set inHover ( value: string ) {
    if ( value.trim () !== '' ) {
      this._inHover = value;
    }
  }

  private _inHover: string;

  // Style-Color des Hosts binden
  @HostBinding('style.color')
  color: string|null = null;

  // da man Farbe über HostBinding macht => braucht man keinen Redner2
  constructor () {  }

  // ermöglicht, dass man auf Host einen Event-Listener registrieren kann. Parameter = Event auf den man Hören sollte
  @HostListener ( 'mouseenter' )
  enter () { //enter() = Event-Handler der getriggert wird
    this.color = this.inHover;
  }

  @HostListener ( 'mouseleave' )
  leave () {
    this.color = null;
  }

  ngOnInit (): void {
    if ( this._inHover === undefined ) {
      this.inHover = 'red';
    }
  }

}
```

### 6 - Strukturelle Direktiven erstellen

* bestimmte DOM Elemente anzeigen, wenn User Admin oder NormalUser ist

* `ng generate directive role` + in export bei Modul packen

* mit strukturelen Direktive kann man `ngTemplate` bzw. `*` verwenden + dieses Template wird dann in View in Abhängikeit von bestimmten Gegenbenheiten (die die Directive besimmt) eingefügt/entfernt

```ts role.directive.ts
@Directive ( {
  selector: '[inRole]'
} )
export class RoleDirective {
  get inRole (): string {
    return this._inRole;
  }

  @Input ()
  set inRole ( value: string ) {
    this._inRole = value;
    // die Role setzen + überpfügen
    const access = this.hasRolePermission( value );
    // in Abhängikeit von der Role die View de/aktivieren
    if ( access && ! this._hasView ) {
      // template init.
      this.viewContainer.createEmbeddedView( this.templRef );
      this._hasView = true;
    } else if ( !access && this._hasView ) {
      // remove template
      this.viewContainer.clear();
      this._hasView = false;
    }
  }

  private _hasView = false;
  private _inRole: string;

  // damit man ngTemplate und * nutzen kann
  constructor ( private templRef: TemplateRef,
                private viewContainer: ViewContainerRef ) {
  }

  // Funktion um die Role zu prüfen
  hasRolePermission ( role: string ): boolean {
    return role === environment.role;
  }
}
```

```ts environment.ts
export const environment = {
  production: false,
  role: 'admin' // für role.direktive
  // role: 'client' // wenn man admin auskommentier und client einkommentiert => wird inRole nicht mehr angezeigt
};
```

```html app.compoment.thml:
<button *inRole="'admin'">Admin</button>`

<ng-template inRole="admin">
    <h1>admin version</h1>
  </ng-template>

```

## 5 - Grundlagen zu Pipes

### 1 - Was ist eine Pipe

* dienen dazu Ausgaben zu modifizieren = Ausgabe formatieren
  * z.B Datum ins richtige Format setzen
  * Preise (Komma <-> Punkt)

### 2 - Pipes in HTML anwenden

* Syntax: `Ausdruck | PipeName [:'Paramter']`
  1. `<h1>{{name | uppercase}}</h1>`
  2. `<h1>{{createdAt | date :'long'}}</h1>`
* man kann Pipes auch verschachteln `<h1>{{createdAt | date :'long' | uppercase }}</h1>`

### 3 - Pipes via JS anwenden

1. Pipe-Klasse-Namen herausfinden: `PIPENAMEPipe`
2. Pipe-Instanz erzeugen + `transform()` aufrufen

```ts
const reversePipe: ReversePipe = new ReversePipe();
reversePipe.tranform(123);
```

### 6 - Hauseigene Pipes nutzen

#### 1 - Lower- & UpperCasePipe

#### 2 - CurrencyPipe

#### 3 - Locale

#### 4 - DecimalPipe

#### 5 - PercentPipe

#### 6 - DatePipe

#### 7 - SlicePipe

#### 8 - JsonPipe

### 7 - Pipes erstellen und nutzen

#### 1 - Pipe erstellen

#### 2 - ReversePipe via CLI

#### 3 - pure

### 8 - Grundlagen zur Dependency Injection

#### 1 - Dependency Injection in der Angular-Welt

* einer Abhängigkeit geschuldet die Informationen zur Laufzeit injezieren d.h. abhängig von bestimmten Zustand bestimmtes Objekt injezieren

* Schema:
  1. ModulA
      1. in `declarations` KomponentA registieren
      2. in `providers` ServiceA bereitstellen => dadurch kann man Instanzen (andere Component-s, Service-s, Pipe-s, Directiv-en), die von Angular erzeugt werden nicht mehr mit `new` jede Mal neu erzeugen, sondern direkt die erzeugten benutzen (im Angular macht man dan die Injezierung im `constructor()` des Komponent)
  2. KomponentA
      1. `constructor(lala: Typ)` - Typ ist wichtig. Angular schauet, ob es schon diese Instanz gibt und gibt diese mit oder erzeugt neue wenn noch nicht erzeugt
* Rootinjektor der Anwendung = Array/Container mit Info wie Dep Inj ablaufen soll. Dieser RootInjector wird mit Infos aus ModuelXYZ `providers:` gefüllt
* die Services/Injection werden aber auch über Rootinjektor sonder Injector Bubbling geschieht. Jede Komponente bekommt hat eigenen Injector-Service. Zuerst wird in dem geschaut, dann im Eltern-Injector erst RootInjector gefragt. Oft kann es vorkommen, dass es verschiedene Instanzen verschiedenen Komponenten gegeben werden z.B wenn Eltern-Injector einer Komponente diesen Service hat und andere Komponente bekommt die Injection aus Rootinjector (RootInjector hat alle declarierten + exportieren Klassen).

#### 2 - Vorhanden Services nutzen

* Angular (Haus-)Services:
  1. in Component/Servcie/Directive auf Injector direkt zugreifen: `Injector` indezieren + über `injector.get(token)` Infor aus Injector bekommen. Also Injector selbst ist injizierbar
  2. ElementRef - Instanz eigener Directive/Komponente mit `elementRef.nativeElement` auf das DOM-Element der Directive/Componente zugreifen
  3. Render2 - DOM anpassen: rendere.setStyle `(elementRef.nativeElement, "color", 'red')`

### 9 - Provider nutzen

#### 1 - Eigene Services bereitstellen

1. Klasse app-model.service.ts erstellen

```ts
export class AppModelService {
  startTime = Date.now();
  counter = 0;
}
```

2. als provider bereitstellen in app.module.ts, damit man es in anderen Componenten indizieren kann

```ts
@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    UserModule
  ],
  providers: [ AppModelService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

3. in app.component.ts verwenden

```ts
@Component ( {
  selector   : 'in-root',
  templateUrl: './app.component.html',
  styleUrls  : [ './app.component.scss' ]
} )
export class AppComponent {

  title        = 'in';
  showUserInfo = true;

  class2bind = 'class-name-1 class-name-2 class-name-3';

  // mit 
  constructor ( public appModel: AppModelService, login: LoginService ) {
    console.log ( appModel, login );
  }

  increment () {
    this.appModel.counter ++;
  }

}
```

```ts user.component.ts
@Component({
  selector: 'in-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {
  // mit public kann man auch in .html zurgreifen, sonst nur in der eigenen .ts
  constructor( public appModel: AppModelService, login: LoginService ) {
    console.log ( appModel, login );
  }
  ngOnInit() {  }
}
```

```html user.compomnent.html
<h4>{{appModel.startTime | date }}</h4>
<h4>{{appModel.counter }}</h4>
<in-user-list></in-user-list>
```

```html app.component.html
<button (click)="increment()">increment {{appModel.counter}}</button>
```

* `@Injectable()` bedeutet eigentlich, dass diese Klasse selbst im `constructor` Injection aufnehmen kann. In `AppModelService` kann man es nicht machen

```ts login.service.ts
import { Injectable, Injector } from '@angular/core';

@Injectable()
export class LoginService {
  constructor( injector: Injector ) {
    console.log ( injector );
  }

}
```

```ts user.module.ts
@NgModule({
  imports: [
    CommonModule
  ],
  providers: [ LoginService ],
  declarations: [UserComponent, UserListComponent, UserNameComponent],
  exports: [UserComponent]
})
export class UserModule { }
```

#### 2 - Werte bereitstellen

* Werte die via Dependency Injection bereitgestellt werden können

```ts app.module.ts
@NgModule ( {
  declarations: [
    AppComponent
  ],
  imports     : [
    BrowserModule,
    UserModule
  ],
  providers   : [
    AppModelService,
    { provide: 'username', useValue: 'Lala1' }, //Objekt, die Attr. provide hat (besser hier Inject-Token übergeben ABER hier im Bsp: String username = Lala2)
    { provide: 'users', useValue: 'Lala2' }
  ],
  bootstrap   : [ AppComponent ]
} )
export class AppModule {
}
```

```ts user.compoment.ts
@Component({
  selector: 'in-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {
  constructor( public appModel: AppModelService,
               login: LoginService,
               @Inject('users') users: string, //da kein Eindeutiger Typ (wie bei den Serveses) hier Decorator @Inject(TOKEN). Hier ist Token 'users' und 'username' 
               @Inject('username') username: string, ) {
    console.log ( users, username );
  }
  ngOnInit() {  }
}
```

#### 3 - Multi-Option

```ts app.module.ts
@NgModule ( {
  declarations: [
    AppComponent
  ],
  imports     : [
    BrowserModule,
    UserModule
  ],
  providers   : [
    AppModelService,
    { provide: 'username', useValue: 'Lala'},
    { provide: 'users', useValue: 'Peter', multi: true }, // mit Option multi: true kann man sagen, ob Werte Unique oder List von Werten gespeichert werden soll => Wird zu Array 
    { provide: 'users', useValue: 'Hans', multi: true },
    { provide: 'users', useValue: 'Frank', multi: true }
    // man kann dann weitere users in anderen Modulen anlegen, die dann zu dieser Liste mitangenommen werden
    // wenn nicht multi wird, wird es überschrieben, falls gleicher provide: NAME irgendwo noch vorkommt
  ],
  bootstrap   : [ AppComponent ]
} )
export class AppModule {
}
```

#### 4 - Klasseninstanz bereitstellen

* ganze Klasse mit Klasse-Provider Klassen-Instanzen in provider-Listen hinzufügen

```ts app.module.ts
export class UseMe{
  val = 123;
}

export class UseMe1 implements IUseMe {
  val = 123;
}

export class UseMe2 implements IUseMe {
  val = 456;
}


@NgModule ( {
  declarations: [
    AppComponent
  ],
  imports     : [
    BrowserModule,
    UserModule
  ],
  providers   : [
    AppModelService,
    <ClassProvider>{provide: 'useMe', useClass: UseMe, multi: true},
    <ClassProvider>{provide: 'useMe', useClass: UseMe1[], multi: true},
    <ClassProvider>{provide: 'useMe', useClass: UseMe1[], multi: true}
  ],
  bootstrap   : [ AppComponent ]
} )
export class AppModule {
}
```

```ts user.component.ts
@Component ( {
  selector   : 'in-user',
  templateUrl: './user.component.html',
  styleUrls  : [ './user.component.scss' ]
} )
export class UserComponent implements OnInit {
  constructor (
    public appModel: AppModelService,
    @Inject ('useMe') useMe: useMe: any,
    @Inject ('useMe') useMe1: useMe: any
    login: LoginService
  ) {
    console.log ( useMe );
  }

  ngOnInit () {
  }
}
```

```ts iuse-me-ts
export interface IUseMe {
  val: number;
}
```

#### 5 - Bereitstellung "konkatieren"

* innerhalb des Provider, einen Wert bereitstellen der aus anderen Werten erstellen => mit existing Provider

```ts 
@NgModule ( {
  declarations: [
    AppComponent
  ],
  imports     : [
    BrowserModule,
    UserModule
  ],
  providers   : [
    AppModelService,
    <ValueProvider>{provide: 'user', useValue: 'Lala'}, // 
    <ClassProvider>{provide: 'useMe', useClass: UseMe, multi: true},
    <ClassProvider>{provide: 'useMe', useClass: UseMe2, multi: true},
    <ExistingProvider>{provide: 'useExist', useExisting: 'useMe', multi: true}, // existeirende Werte kann man dann bei useExisting = Ref. auf existierendes Obj
    <ExistingProvider>{provide: 'useExist', useExisting: 'user', multi: true}
  ],
  bootstrap   : [ AppComponent ]
} )
export class AppModule {
}
```

```ts user.compoment.ts
@Component ( {
  selector   : 'in-user',
  templateUrl: './user.component.html',
  styleUrls  : [ './user.component.scss' ]
} )
export class UserComponent implements OnInit {
  constructor ( public appModel: AppModelService,
                @Inject ('useMe') useMe: IUseMe[],
                //@Inject ('useExist') useExist: 'useMe'
                @Inject ('useExist') useExist: any[],
                login: LoginService ) {
    console.log ( useMe, useExist );
  }

  ngOnInit () {
  }
}
```
#### 6 - Bereitstellung über Factory-Methode

```ts app.module.ts
@NgModule ( {
  declarations: [
    AppComponent
  ],
  imports     : [
    BrowserModule,
    UserModule
  ],
  providers   : [
    AppModelService,
    <ValueProvider>{provide: 'user', useValue: 'Saban Ünlü'},
    <ClassProvider>{provide: 'useMe', useClass: UseMe, multi: true},
    <ClassProvider>{provide: 'useMe', useClass: UseMe2, multi: true},
    <ExistingProvider>{provide: 'useExist', useExisting: 'useMe', multi: true},
    <ExistingProvider>{provide: 'useExist', useExisting: 'user', multi: true},
    // Werte bereitstellen die über Factory-Methode erzeugt wurden
    <FactoryProvider>{provide: 'mixed', useFactory: () => {
      return 'Lala';
    }},  //UseFator erwarten Funktion, die Wert für mixed zurückliefert
    <FactoryProvider>{provide: 'mixed', deps: ['user'], useFactory: ( usr: string ) => {
      return `factory return ${usr}`; //hier die Funktion mit Funktionen
    }},
  ],
  bootstrap   : [ AppComponent ]
} )
export class AppModule {
}
```

```ts user.compoment.ts
export class UserComponent implements OnInit {
  constructor ( public appModel: AppModelService,
                @Inject ('useMe') useMe: IUseMe[],
                @Inject ('useExist') useExist: any[],
                @Inject ('mixed') mixed: any[], // hier wird Injeziert
                login: LoginService ) {
    console.log ( 'mixed', mixed );
  }

  ngOnInit () {
  }
}
```

#### 7 - Injectable Decorator seit Angular 6

* `@Injectable()` hat auch weiter Bedeutung: man kann als Param. Konfig-Obj angeben, der sagt, in welchem Modul oder Injector bereitgestellt werden soll `@Injectable(provideIn: 'root')`, `@Injectable(provideIn: UserModule)` - landet im Root-Injector. Vorteil: falls dieser Service nirgendwo benutz wird, wird er weg optimiert. Man kann auch darin `useValue` benutzen
  * Alles was in `providers:` ist landet in Root-Injector

### 10 - Tipps zur Dependency Injection

#### 1 - Token Injection

* Token ist eine Const, die man projekt-weit benutzen kann

```ts user-token.ts
import { InjectionToken } from '@angular/core';

// Token erzeugen
export const USER_TOKEN: InjectionToken<string> = new InjectionToken<string> ( 'userToken ' );
```

```ts app.module.ts
@NgModule ( {
  declarations: [
    AppComponent
  ],
  imports     : [
    BrowserModule,
    UserModule
  ],
  providers   : [
    AppModelService,
    <ValueProvider>{provide: USER_TOKEN, useValue: 'Saban Ünlü'},
    <ClassProvider>{provide: 'useMe', useClass: UseMe, multi: true},
    <ClassProvider>{provide: 'useMe', useClass: UseMe2, multi: true},
    <ExistingProvider>{provide: 'useExist', useExisting: 'useMe', multi: true},
    <ExistingProvider>{provide: 'useExist', useExisting: USER_TOKEN, multi: true},
    <FactoryProvider>{provide: 'mixed', deps: [USER_TOKEN], useFactory: ( usr: string ) => {
      return `factory return ${usr}`;
      }},
    {provide: LOCALE_ID, useValue: 'de'}
  ],
  bootstrap   : [ AppComponent ]
} )
export class AppModule {
}
```

```ts user.compoment.ts
@Component ( {
  selector   : 'in-user',
  templateUrl: './user.component.html',
  styleUrls  : [ './user.component.scss' ]
} )
export class UserComponent implements OnInit {
  constructor ( public appModel: AppModelService,
                @Inject ('useMe') useMe: IUseMe[],
                @Inject ('useExist') useExist: any[],
                @Inject ('mixed') mixed: any[],
                @Inject ( USER_TOKEN ) user: string,
                login: LoginService ) {
    console.log ( 'user', user);
  }

  ngOnInit () {
  }
}
```

#### 2 - Der LOCALE_ID-Token

#### 3 - Host-, Self- und Optional Decorator
