# Angular Grundkurs - Erweiterte Komponente

## 1 - Komponentenbasierte Entwicklung und Lebenszyklen

### 1 - Grundlagen: Komponentbasierte Enwtwicklung

- innhalb Komponenten KindsKomponenten erzeugen => Komponeten-Baum erzeugen
- Komponente und Inhalte transkludieren Inhalte = sagen welche Elemente dargestellt werden sollen

  - einfach `<app-KINDNAMDE></app-KINDNAME>` eingeben
  - um zu transkludieren:

  ```html app.html
  <user-list>
    <user-header></user-header>
    <user-item></user-iterm>
    <user-item></user-iterm>
    <user-item></user-iterm>
  </user-list>
  ```

  ```html user-list.html
  <div>
  <!--
    ...
  -->
  </div>
  <ng-content select="user-header"></ng-content> <!-- bestimtme Elemente an besimmte Position transkludieren>
  <ng-content></ng-content>
  ```

  - `<ng-component>` sagt: Ich werden die Inhalte von Eltern-Comp übernehmen, die für diese Comp. implementiert sind

### 2 - Grundlagen: Komponentenlebenszyklen

- Lebenszyklus:
  1. `constructor`
  2. `ngOnChange` - wird nach `constructor` und auch dann ausgeführt, wenn sich Bindungen aktualisieren
  3. `ngOnInit` - wenn Comp. initialisiert wird. Ist aussagekräftiger, da besagt, dass die Komponente komplett initialisiert wurde
  4. `ngDoCheck` - sobald eine Änderung in der Kompomente stattgefundnen wurden
     1. `ngAfterContentInit` - sagt dass transkludierte Inhalte fertig initialisiert wurden
     2. `ngAfterContentChecked` - ob transkludierte Inhalte sich geändert haben
     3. `ngAfterViewInit` - ob Kinds-Komp ngOnInit ausgefürht hat
     4. `ngAfterViewChecked`
  5. `ngOnDestroy` - wenn man bestimmte Sachen zerstörten möchte

## 2 - Vorlagenelemente ermitteln

### 1 - Grundlagen: ViewChild-Dekorator

- auf Elemente in der Vorlage referenzieren = Element in der Vorlage(html) mit Attr der Klasse(ts) verbinden:
  1. Parameter:
     1. Komponentkalsse `<myComponent>`, Directivenklasse `<div myDirective>`, Hash-ID `<div #myID>`
     2. Options-Obj `{static: true|false}` = ob statisches oder dynamische Obj
     3. `read: ElementRef | ViewContainerRef | TemplateRef` - ob nur Element, Template oder ViewContainter - Referenz
  2. dynamisch = haben `*ngIf|For`. Bei dynamischen, kann man auf die Elemente erst nach `ngAfterViewInit` und nicht nach `ngInit` zugreifen, wie bei statischen Elementen
- `@ViewChildren` - wenn man auf mehrere Elemente schauen will
  1. nur bei dynamischen Objekten
  2. erzeugt `QueryList<Type>`. man kann sich bei QueryList mit `changes -> Observable` registrieren

### 2 - ViewChild-Dekorator nutzen

- Eltern (user.component.ts) auf Kind (user-list.component.ts) zugreifen

```ts user.component.ts
@Component({
  selector: "in-user",
  templateUrl: "./user.component.html",
  styleUrls: ["./user.component.scss"],
})
export class UserComponent implements OnInit, AfterViewInit, OnDestroy {
  /*@ViewChild(UserListComponent, { static: true })statisches Element wenn man hier false macht => erst nach ngAfterViewInit*/
  @ViewChild(UserListComponent, { static: true })
  userList: UserListComponent;

  private selectionSub: Subscription;

  constructor() {
    /*Error, da UserList ist noch undefined. Erst nach ngOnInit ist definiert*/
    // console.log ( this.userList );
    // console.log ( this.userList.selectUsr );
  }

  ngOnInit() {
    /* { static: true }
     Für static: true */
    // console.log ( this.userList );
    // console.log ( this.userList.selectUsr );
  }

  ngAfterViewInit(): void {
    /* { static: false }
     für static: false */
    console.log(this.userList);
    console.log(this.userList.selectUsr);

    /* an den Emitter sich dranhängen: jedes Mal mal mouseover ist */
    //this.userList.selctUsr.subscribe(next => console.log('selected', next ));

    /* Damit man die Subsciption auch merkt um später zu destroen */
    this.selectionSub = this.userList.selectUsr.subscribe((next) =>
      console.log("selected", next)
    );
  }

  ngOnDestroy(): void {
    /* beim Zerstören auch unsubscirben*/
    this.selectionSub.unsubscribe();
  }
}
```

```ts user-list-component.ts
@Component({
  selector: "in-user-list",
  templateUrl: "./user-list.component.html",
  styleUrls: ["./user-list.component.scss"],
  encapsulation: ViewEncapsulation.Emulated,
})
export class UserListComponent implements OnInit {
  @Output()
  selectUsr: EventEmitter<User> = new EventEmitter();

  users: User[] = [
    { name: "Frank Müller", age: 12 },
    { name: "Hans Müller", age: 13 },
    { name: "Peter Müller", age: 14 },
    { name: "Paul Müller", age: 15 },
  ];

  selectedUsr: User;

  constructor() {}
  ngOnInit() {}

  onSelectedUsr(selectedUsr: User) {
    this.selectedUsr = selectedUsr;
    this.selectUsr.emit(this.selectedUsr);
  }
}
```

### 3 - ViewChild-Dekorator einsetzen

- mit `read: ElementRef` - nur HTML-Element der Comp referenzieren, nicht auch den JS-Teil

```ts user.compoment.ts
@Component({
  selector: "in-user",
  templateUrl: "./user.component.html",
  styleUrls: ["./user.component.scss"],
})
export class UserComponent implements OnInit, AfterViewInit, OnDestroy {
  @ViewChild(UserListComponent, { static: false })
  userList: UserListComponent;

  @ViewChild(UserListComponent, { static: true, read: ElementRef }) //mit red: ElementRef = DOM und nicht die Instanz der Element haben
  userListRef: ElementRef;

  private selectionSub: Subscription;

  constructor(private elemRef: ElementRef, private renderer: Renderer2) {}

  ngOnInit() {
    /* { static: true }
     console.log ( this.userList );
     console.log ( this.userList.selectUsr );
    */
    console.log(this.userListRef);
    this.renderer.setStyle(this.userListRef.nativeElement, "color", "red");
  }

  ngAfterViewInit(): void {
    /* { static: false } */
    this.selectionSub = this.userList.selectUsr.subscribe((next) =>
      console.log("selected", next)
    );

    /* Element vom Konstruktor */
    console.log(this.elemRef);
    this.renderer.setStyle(this.elemRef.nativeElement, "color", "red");
  }

  ngOnDestroy(): void {
    this.selectionSub.unsubscribe();
  }
}
```

### 4 - ViewChild mit Hash-ID

- auf Elemente zugreifen, die mit `#HASH-ID` versehen sind. (Hier in der selben Komponente)

```ts
@Component({
  selector: "in-user",
  templateUrl: "./user.component.html",
  styleUrls: ["./user.component.scss"],
})
export class UserComponent implements OnInit, AfterViewInit, OnDestroy {
  @ViewChild(UserListComponent, { static: false })
  userList: UserListComponent;

  @ViewChild(UserListComponent, { static: true, read: ElementRef })
  userListRef: ElementRef;

  @ViewChild("helloWorld", { static: true }) // helloWorld ist die Hash-ID
  paragraphElementRef: ElementRef<HTMLParagraphElement>;

  private selectionSub: Subscription;

  constructor(private elemRef: ElementRef, private renderer: Renderer2) {}

  ngOnInit() {
    // { static: true }
    // console.log ( this.userList );
    // console.log ( this.userList.selectUsr );
    // console.log ( this.userListRef );
    // this.renderer.setStyle( this.userListRef.nativeElement, 'color', 'red' );
    console.log(this.paragraphElementRef);
    this.paragraphElementRef.nativeElement.innerHTML = "hello world";
  }

  ngAfterViewInit(): void {
    // { static: false }
    this.selectionSub = this.userList.selectUsr.subscribe((next) =>
      console.log("selected", next)
    );
    // console.log ( this.elemRef );
    // this.renderer.setStyle( this.elemRef.nativeElement, 'color', 'red' );
  }

  ngOnDestroy(): void {
    this.selectionSub.unsubscribe();
  }
}
```

### 5 - ViewChilden-Dekorator verwenden

- List von Elemente ermitteln sowas wie `selecteElementByTag`

```html user-list.component.html
<h3>User List</h3>

<!-- Hier wird die Komponente user-name so oft erstellt wie es users gibt -->
<in-user-name
  *ngFor="let user of users; even as e"
  [user]="user"
  [isSelected]="selectedUsr===user"
  [ngClass]="{even: e}"
  (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
```

```ts user-list.component.ts
@Component ( {
  selector     : 'in-user-list',
  templateUrl  : './user-list.component.html',
  styleUrls    : [ './user-list.component.scss' ],
  encapsulation: ViewEncapsulation.Emulated
} )
export class UserListComponent implements OnInit, AfterViewInit {

  @Output ()
  selectUsr: EventEmitter<User> = new EventEmitter ();

  @ViewChildren ( UserNameComponent ) userNames: QueryList<UserNameComponent>; //man muss dann auch ngAfterViewInit implementieren

  users: User[] = [
    { name: 'Frank Müller', age: 12 },
    { name: 'Hans Müller', age: 13 },
    { name: 'Peter Müller', age: 14 },
    { name: 'Paul Müller', age: 15 }
  ];

  selectedUsr: User;

  constructor () {
  }

  ngOnInit () {
  }

  onSelectedUsr ( selectedUsr: User ) {
    // this.selectedUsr = selectedUsr;
    // this.selectUsr.emit ( this.selectedUsr );
    // this.users.pop();
    this.users.push( {age: 44, name: 'Lala });
  }

  ngAfterViewInit (): void {
    console.log(this.userNames);
    console.log(this.userNames.toArray());
  }
}
```

### 6 - QueryList und Changes-Eigenschaften

- wenn sich einzelne Kind-Komponenten sich ändern reagieren

```ts user-list.component.ts
@Component({
  selector: "in-user-list",
  templateUrl: "./user-list.component.html",
  styleUrls: ["./user-list.component.scss"],
  encapsulation: ViewEncapsulation.Emulated,
})
export class UserListComponent implements OnInit, AfterViewInit {
  @Output()
  selectUsr: EventEmitter<User> = new EventEmitter();

  @ViewChildren(UserNameComponent)
  userNames: QueryList<UserNameComponent>;

  users: User[] = [
    { name: "Frank Müller", age: 12 },
    { name: "Hans Müller", age: 13 },
    { name: "Peter Müller", age: 14 },
    { name: "Paul Müller", age: 15 },
  ];

  selectedUsr: User;

  constructor() {}

  ngOnInit() {}

  onSelectedUsr(selectedUsr: User) {
    // this.selectedUsr = selectedUsr;
    // this.selectUsr.emit ( this.selectedUsr );
    // this.users.pop();
    this.users.push({ age: 44, name: "Lala" });
  }

  ngAfterViewInit(): void {
    // mit changes kann man auf die Änderungen bei userNames reagieren. Möglich da von Typ QueryList
    this.userNames.changes.subscribe((next) => {
      console.log(next);
    });
  }
}
```

## 3 - Inhalte transkudieren und ermitteln

### 1 - Grundlagen: Transklusion

- Komponente = View

- View = wird mit HTMLVorlage beschrieben

- Vorlage kann weiter Komponten (Kinder) haben. Bsp

```html
<user-list>
  <user-item>name</user-item
  ><!--Kind-->
</user-list>
```

- Inhaltsknonten (Kinder) werden trankludiert, wenn die HTML-Vorlagen die Direktive `ng-content` benutzen = ist Platzhalter = sagt hier kommt eine View (Komponente) rein

- auf diese transkludierte Inhalte dann mittels `@ContentChild` bzw. `@ContentChildren` (ist vom Typ `QueryList<TYPE>` zugreifen (ähnelt dem `@ViewChild` bzw. `@ViewChildren`)
  - erst nach `ngAfterContentInit` zugreifbar

### 2 - ng-content und Inhaltstransklusion

```html user.compoment.html
<in-user-list>
  <p>TEST</p>
  <!-- wird nicht angezeigt, da Inhalt nicht transkludiert wird-->

  <ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
  </ul>
</in-user-list>
```

```ts user.component.ts

```

```html user-list.component.html
<h3>User List</h3>
<ng-content></ng-content>
<!-- hier wird dann Inhalt von user.compoment.html eingesetzt trasnkludiert-->
<in-user-name
  *ngFor="let user of users; even as e"
  [user]="user"
  [isSelected]="selectedUsr===user"
  [ngClass]="{even: e}"
  (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
```

### 3 - ng-content-select-Attribut anwenden

- mit `select` auch sagen was genau wo eingefügt werden soll

```html user.component.html
<in-user-list>
  <span class="title">Mitarbeiter</span>

  <p>
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi deserunt
    dolor doloribus earum enim, et eveniet exercitationem expedita facilis
    maxime minus nesciunt nobis porro quaerat quod rem, similique soluta vitae?
  </p>

  <span class="title">Mitarbeiter</span>
</in-user-list>
```

```html user-list.compoment.html
<h3>
  User List <ng-content select="span.title"></ng-content>
  <!-- hier kommt <span class="title" reinkommt auch Mehrmals, fall es in Kind-Komp es mehrmals gibt-->
</h3>

<ng-content></ng-content>

<in-user-name
  *ngFor="let user of users; even as e"
  [user]="user"
  [isSelected]="selectedUsr===user"
  [ngClass]="{even: e}"
  (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
```

### 4 - ContentChild-Decorator einsetzen

- auf transkludierte Inhalte zugreifen

```html user-list.component.html
<ng-content select="in-user-list-header"></ng-content>
<ng-content select="in-user-list-sub-header"></ng-content>
<ng-content select="in-user-list-info"></ng-content>
<!-- 1 wird eigentlich an Component user-list-info weitergegeben-->

<in-user-name
  *ngFor="let user of users; even as e"
  [user]="user"
  [isSelected]="selectedUsr===user"
  [ngClass]="{even: e}"
  (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
```

```html user.component.html
<in-user-list>
  <!--1 -->
  <in-user-list-info
    >Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium
    deleniti maiores quos. Asperiores deserunt doloribus dolorum eius explicabo,
    facere fugiat illum in, labore magni non quia reprehenderit sequi vel
    voluptatum.</in-user-list-info
  >
  <!--2 --->
  <in-user-list-header>Mitarbeiter</in-user-list-header>
  <!-- 3 -->
  <in-user-list-sub-header>Graz</in-user-list-sub-header>
</in-user-list>
```

```html user-list-info.component.html
<p>
  <ng-content></ng-content>
</p>
```

```ts user-list.component.ts
@Component({
  selector: "in-user-list",
  templateUrl: "./user-list.component.html",
  styleUrls: ["./user-list.component.scss"],
  encapsulation: ViewEncapsulation.Emulated,
})
export class UserListComponent implements OnInit, AfterContentInit {
  @Output()
  selectUsr: EventEmitter<User> = new EventEmitter();

  // auf transkludierte Inhalt zugreifen
  @ContentChild(UserListInfoComponent, { static: false })
  userListInfo: UserListInfoComponent;

  @ContentChild(UserListSubHeaderComponent, { static: true })
  userListSubHeader: UserListSubHeaderComponent;

  @ContentChild(UserListHeaderComponent, { static: true })
  userListHeader: UserListHeaderComponent;

  @ContentChild(UserListHeaderComponent, { static: true, read: ElementRef })
  userListHeaderRef: ElementRef;

  users: User[] = [
    { name: "Frank Müller", age: 12 },
    { name: "Hans Müller", age: 13 },
    { name: "Peter Müller", age: 14 },
    { name: "Paul Müller", age: 15 },
  ];

  selectedUsr: User;

  constructor() {}

  ngOnInit() {
    console.log(
      this.userListHeader,
      this.userListSubHeader,
      this.userListHeaderRef.nativeElement
    );
  }

  onSelectedUsr(selectedUsr: User) {
    this.selectedUsr = selectedUsr;
    this.selectUsr.emit(this.selectedUsr);
  }

  ngAfterContentInit(): void {
    console.log(this.userListInfo);
  }
}
```

### 5 - ContentChildren-Decorator nutzen

- Komponenten mehrmals benutzen => statt `@ContentChild` `@ContentChildren` verwenden

```html user.component.html
<in-user-list>
  <in-user-list-info>Lorem 1</in-user-list-info>
  <in-user-list-info>Lorem 2</in-user-list-info>
  <in-user-list-info *ngIf="testing" (click)="testing = !testing"
    >Lorem 3</in-user-list-info
  >
  <in-user-list-header>Mitarbeiter</in-user-list-header>
  <in-user-list-sub-header>Graz</in-user-list-sub-header>
</in-user-list>
```

```html
<ng-content select="in-user-list-header"></ng-content>
<ng-content select="in-user-list-sub-header"></ng-content>
<ng-content select="in-user-list-info"></ng-content>

<in-user-name
  *ngFor="let user of users; even as e"
  [user]="user"
  [isSelected]="selectedUsr===user"
  [ngClass]="{even: e}"
  (selectUsr)="onSelectedUsr ( $event )"
></in-user-name>
```

```ts user-list.component.ts
@Component({
  selector: "in-user-list",
  templateUrl: "./user-list.component.html",
  styleUrls: ["./user-list.component.scss"],
  encapsulation: ViewEncapsulation.Emulated,
})
export class UserListComponent implements OnInit, AfterContentInit, OnDestroy {
  @Output()
  selectUsr: EventEmitter<User> = new EventEmitter();

  @ContentChild(UserListInfoComponent, { static: false })
  userListInfo: UserListInfoComponent;

  // Hier die Children
  @ContentChildren(UserListInfoComponent)
  infos: QueryList<UserListInfoComponent>;

  @ContentChild(UserListSubHeaderComponent, { static: true })
  userListSubHeader: UserListSubHeaderComponent;

  @ContentChild(UserListHeaderComponent, { static: true })
  userListHeader: UserListHeaderComponent;

  @ContentChild(UserListHeaderComponent, { static: true, read: ElementRef })
  userListHeaderRef: ElementRef;

  users: User[] = [
    { name: "Frank Müller", age: 12 },
    { name: "Hans Müller", age: 13 },
    { name: "Peter Müller", age: 14 },
    { name: "Paul Müller", age: 15 },
  ];

  selectedUsr: User;
  private sub: Subscription;

  constructor() {}

  ngOnInit() {
    console.log(
      this.userListHeader,
      this.userListSubHeader,
      this.userListHeaderRef.nativeElement
    );
  }

  onSelectedUsr(selectedUsr: User) {
    this.selectedUsr = selectedUsr;
    this.selectUsr.emit(this.selectedUsr);
  }

  ngAfterContentInit(): void {
    console.log(this.userListInfo, this.infos.toArray());
    // hier wird an changes() von User-List-Info.component subscripted
    this.sub = this.infos.changes.subscribe((value) =>
      console.log("changed infos", value)
    );
  }

  ngOnDestroy(): void {
    // Subscription löschen, wenn Componente von Angular gelöscht wird.
    this.sub.unsubscribe();
  }
}
```

## 4 - Dynamische Inhalte erstellen

### 1 - Grundlagen: Dynamische Inhlate

- Jede Komponnete ist in `ViewRef` zusammengefasst
  - ist ein Block von Elementen
  - auf diesen Blöcken bzw. `ViewRef` aggiert Änerungserkennung
  - jedes Element hat `ViewContainerRef`
    - ist Referenz zum Container für dynamische Inhalte, die hinter dem Element angehängt werden
    - hat zwei Views:
      1. Embedded View = über Vorlagenreferenzen (Templage-Ref)
      2. Host View = über Komponentenreferenz (ganze Komponenten dynamisch erstellten)
- Vorlagen dynamisch nutzen
  1. `*ngTemplateOutlet` - strukturelle Direktive (z.B im `ng-container` verwendet)
  2. `ViewContainerRef` (via Dependency Injection)
  3. dann kann man mit `createEmbeddedView()` über Template-Ref (z.B: `templateRef: TemplateRef<T>`) neue Inhalte über Templates generieren
  4. Template-Ref kann man auch z.B über Option `{read: TemplateRef}` von `@ViewChild` oder `@ContentChild` bekommen
- man kann Komponenten auch dynamisch erstellen
  1. zuvor in `entryComponents` aufnehmen
  1. über `ngComponentOutlet` - strukturele Direktive
  1. über Komponent-Factory (`ComponentFactoryResolver`), die von Dependency Injection zur Verfügung gestellt wird:
  1. mit `resolveComponentFactor()` braucht die Klasse der Komponente, die in ComponentFactory registriert wurde
  1. über `ViewContainerRef` über Dependency Injection
  1. mit `createComponent()`

### 2 - ngTemplateOutlet mit ng-template nutzen

- mit VorlagenReferenz

```ts dynamic module.ts
@NgModule({
  imports: [CommonModule],
  declarations: [DynamicComponent, TemplateBaseComponent],
  exports: [DynamicComponent],
})
export class DynamicModule {}
```

```html dynamic.component.ts
<h3>Dynamische Inhalte</h3>

<in-template-base>
  <ng-template let-myname="name" let-msg>
    {{myname}}
    <hr />
    <p>{{msg}}</p>
  </ng-template>
</in-template-base>
```

```ts dynamic.component.ts
@Component({
  selector: "in-dynamic",
  templateUrl: "./dynamic.component.html",
  styleUrls: ["./dynamic.component.scss"],
})
export class DynamicComponent implements OnInit {
  constructor() {}

  ngOnInit() {}
}
```

```ts template-base.component.ts
@Component({
  selector: "in-template-base",
  templateUrl: "./template-base.component.html",
  styleUrls: ["./template-base.component.scss"],
})
export class TemplateBaseComponent implements OnInit {
  myContext = { $implicit: "Hello World!", name: "Lala" };

  @ContentChild(TemplateRef, { static: false })
  myTemp: TemplateRef<HTMLElement>;

  constructor() {}

  ngOnInit() {}
}
```

```html
<!-- Inhalte dynmisch erstellen auf Basis TemplateRef.  HIER mit *ngTemlateOutlet. Hier wird Template-Ref "myTemp" --->
<ng-template #myTemp>
<p>Lala</p>
</ng-temlate>

<ng-container *ngTemplateOutlet="myTemp; context: myContext"></ng-container>
```

```html app.component.ts
<div>
  <h1>Welcome to {{ title }}!</h1>
  <!-- HIER die dynamische Komponente-->
  <in-dynamic></in-dynamic>
</div>
<footer>
  <a
    href="https://www.linkedin.com/learning/instructors/saban-unlu"
    target="_blank"
  >
    <img src="../assets/img/linkedin-logo.png" alt="linkedin" />
  </a>
  <a href="https://www.nettrek.de/" target="_blank">
    <img src="../assets/img/logo.png" alt="netTrek" />
  </a>
  <a
    href="https://github.com/netTrek/LinkedIn_Angular_Vertiefung"
    target="_blank"
  >
    <img src="../assets/img/github.png" alt="github" />
  </a>
</footer>
```

### 3 - ngTemplateOutlet mit ng-template nutzen

- ngTemplateOutlet mit Context verwenden
- Context = Obj die innerhalb des Templates genutzt werden können

```ts template-base.component.ts
@Component({
  selector: "in-template-base",
  templateUrl: "./template-base.component.html",
  styleUrls: ["./template-base.component.scss"],
})
export class TemplateBaseComponent implements OnInit {
  // Context erstellen
  //myContext = { name: 'Lala' };
  myContext = { $implicit: "Hello World!", name: "Lala" };

  @ContentChild(TemplateRef, { static: false })
  myTemp: TemplateRef<HTMLElement>;

  constructor() {}

  ngOnInit() {}
}
```

```html
<!-- HIER den Context nutzen -->
<ng-template #myTemp let-myname="name" let-msg>
  {{ myname }} {{ msg}}
  <!-- ist Variable $implicit>
<p>Lala</p>
</ng-temlate>

<!-- HIER den Context nutzen -->
  <ng-container *ngTemplateOutlet="myTemp; context: myContext"></ng-container
></ng-template>
```

### 4 - Vorlagenreferenz transkludieren

- obiger Ansatz ist etwas umständlich, da `<ng-temlate>` in der gleichen Datei steht => doppelt gemoppelt

```html dynamic.component.html
<h3>Dynamische Inhalte</h3>

<in-template-base>
  <ng-template let-myname="name" let-msg>
    {{myname}}
    <p>{{msg}}</p>
  </ng-template>
</in-template-base>
```

```html template-base.component.html
<ng-container *ngTemplateOutlet="myTemp;  context="myContext"></ng-container>
```

```ts template-base.component.ts
@Component({
  selector: "in-template-base",
  templateUrl: "./template-base.component.html",
  styleUrls: ["./template-base.component.scss"],
})
export class TemplateBaseComponent implements OnInit {
  // Hier die Ref für myTemp erstellen
  @Content Child(TemplateRef);
  myTemp: TemplateRef<HTMLElement>;

  myContext = { $implicit: "Hello World!", name: "Lala" };

  constructor() {}

  ngOnInit() {}
}
```

- jetzt kann _template-base.component_ ihre eigene Logik haben, die dann an _dynamic.component_ weitergegeben wird

### 5 - Vorlagenreferenz über strukturelle Direktiven erzeugen

- sturkturelle Direktive Anstelle von `ng-temlplate` umd TemplateRef durchreichen.

```ts address.directive.ts
import { Directive } from "@angular/core";

// ist eigentlich egal was hier steht, da nur selector benötigt wird
@Directive({
  selector: "[inAddress]",
})
export class AddressDirective {
  constructor() {}
}
```

```html
<h3>
  Dynamische Inhalte
</h3>

<in-template-base>
  <div *inAddress="let msg; name as myname">
    {{myname}} <br>
    Dorsten <br>
    {{msg}}
  </div>

  <!-- mit der *inAddress-Direktive kann man hier belibiges (HTML)-Tag verwenden-->
  <address *inAddress="let msg; name as myname">
    Lala
  <address>
</in-template-base>
```

```ts tempate-base.component.ts
@Component({
  selector: "in-template-base",
  templateUrl: "./template-base.component.html",
  styleUrls: ["./template-base.component.scss"],
})
export class TemplateBaseComponent implements OnInit {
  myContext = { $implicit: "Deutschland", name: "Lala" };

  // ContentChild anpassen, damit man es hier erreichen kann
  @ContentChild(AddressDirective, { static: false, read: TemplateRef })
  myTemp: TemplateRef<HTMLElement>;

  constructor() {}

  ngOnInit() {}
}
```

### 6 - ViewContainerRef für Vorlagenreferenzen nutzen

- auch ohne strukturellen Direktive Vorlagen erstellen => `ViewContainerRef` = umgebende Objekt der Componente

```ts
@Component({
  selector: "in-template-base",
  templateUrl: "./template-base.component.html",
  styleUrls: ["./template-base.component.scss"],
})
export class TemplateBaseComponent implements OnInit {
  myContext = { $implicit: "Deutschland", name: "Lala" };

  @ContentChild(AddressDirective, { static: true, read: TemplateRef })
  myTemp: TemplateRef<any>;

  // hier and die Referenz für Möglichkeit 2 rankommen
  @ViewChild(TemplateRef, { static: true, read: ViewContainerRef })
  private viewContainerRef: ViewContainerRef;

  constructor(/*private viewContainerRef: ViewContainerRef*/) {}

  // ViewContainerRef als Dependency Injection
  constructor(private viewContainerRef: ViewContainerRef) {}

  ngOnInit() {
    //Möglichkeit 1
    this.viewContainerRef.createEmbeddedView(this.myTemp, this.myContext); // Instanz der Ref erzeugen (man kann hier noch index übergeben)
    //Möglichkeit 2
    const viewRef: ViewRef = this.myTemp.createEmbeddedView({
      $implicit: "USA",
      name: "Peter Müller",
    });
    this.viewContainerRef.insert(viewRef);
  }
}
```

```html template-base.component.html
<!--
Möglichkeit 1
<ng-container *ngTemplateOutlet="myTemp; context: myContext"></ng-container>
-->

<!-- Möglichkeit 2 => man muss dann aber die Ref nicht über Dependency Injection reinbekommen-->
<ng-template></ng-template>
```

### 7 - ngComponentOutlet einstezen

### 8 - ViewContainerRef für Component-Factory verwenden

## 5 - Änderungserkennung

### 1 - Grundlagen: Änderungserkennung

### 2 - ChangeDetectionStrategy and ChangeDetectorRef

### 3 - async pipe und Input-Dekorator

### 4 - Änderungserkennung im Kontext einer Liste

### 5 - ChangeDetectorRef detach und reattach

## 6 - Tipps zum Abschluss

### 1 - Derivate einer Komponente

### 2 - Komponentenservices nutzen
