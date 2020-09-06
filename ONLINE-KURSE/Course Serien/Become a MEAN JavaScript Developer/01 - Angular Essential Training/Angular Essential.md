# Angular Essential Training

## 0 - Introduction

* Github: [https://github.com/coursefiles/angular-essential-training]

### 1 - Why use Angular

* ist Java-Framework
* hat Dependency Injection eingebaut
* -> zum bilden Client-Applications

### 2 - What you should know

### 3 - Using the exercise files

* nmp lernen
* angluar cli lernen
  * <- gibt es alles auf Lynda

### 4 - Basics of TypeScript

* Angular ist in TypoScript geschrieben
  * TypoScript:
    * ES2015 classen
    * Module
    * Typisierung der Variablen
    * Funktionssignaturen
    * in TypoScript kann man auch JS schreiben
* TypoScript to Know:
  * Klassen schreiben
  * Angular Decoratoren
  * Parameter Type Annotationen
* man kann auch nur JS ES2015 schreiben
* Bsp TypoScript:

```javascript
import {Component} from 'angular2/core';
import {FromBuilder} from 'angular2/core'; //Imports = Module laden

@Component({ //TypeScript-Dekorator
    selector: 'media-tracker-app'
    templateUrl: './app.component.html'
    styleUrls: ['./app.compoments.css']
})

export class AppComponent { //Klass-Def - Klass-Syntax ist ES2015; export (TS) - Klasse zum Modul umwandlen
    constructor(fromBuilder: FromBuilder) {} //Konsturktor ist ES2015-syntax; in () - TS-Typisierung
}
```

### 5 - Course overview

## 1 - Architecture Overview

### 1 - Components, Bootstrap and the DOM

* Angular wird aus Componenten gebildet (Baum-Struktur ähnlich dem DOM-Baum). Starte ist **Bootstraping-Component**
* Angular startet mit Bootstrap-Call -> dann schauet es nach ob es weitere Componenten gibt und lädt diese in den Baum
* Componenten rendert Teil von HTML und zugehörige Funktionen zu diesem Teil. In diesem Component-Klasse ist die Logik des Components
  * Component kann z.B *mediaItem* haben und *onDeleteClick*.
* Mit Componenten kann man HTML-Templates erstellen
  * in HTML selbst wird Template-Syntax benutzt.
* Compoente wird anstelle des HTML-Elements gerendert

### 2 - Directives and pipes

* Componente = Direktive mit Template. Direktiven enthalten Funktionalität und DOM-Tranformationen
* Direktiven können sein:
  * Structural - ändern Elemente im DOM
  * Attribute - ändern Verhalten von DOM-Elem
* Direktive wird auch mit Selecotoren konfiguriert:

```javascript
@Decorator({
    selector: "mwFavorite"
})
<div mvFavorite>  //Selektor
<div [mvFavorite]=true >   // Template
    <img src="lala.img" />
</div>
```

* Angular hat schon ein paar Direktiven für bekannte Web-Constructs:
  * `ngIf` - conditional rendering
  * `ngFor` - Looping
  * `routerLink` - Routing

* Angular Pipe; man kann auch eigene Pipes schreiben

### 3 - Data binding

* Templating
* Direcitven - Logik zu Templates hinzufügen
* Elemente zu Template Syntax:
  * Interpolation
  * Build-In-Directiven
  * Konstuktoren
  * Bindings
    * Expressions and Statements
    * Value Binding
    * Event Binding
    * Expression operators
* man kann locale Template Variablen erstellen und mit Markup-Syntax (#) zu diesen Variablen referenzieren

### 4 - Dependendy injection

* DI
* `Constructor(formBuilder: formBuilder){}` - wird oft in Konstruktoren benutzt
* `bootstrap(App, [FormulaService]);` - auch bei bootstrap oft benutzt
* d.h. Dependencies für Componenten liefert

### 5 - Services and other business logic

* Serivces -> Pattern, Klasslogik
* dann mit DI an Componenten ausliefern
* Klassen müssen nicht unbedingt in Angular sein

### 6 - Data persistence

* man kann Daten zu/von API holen mit http (XHR, JSONP). Angular hat ein Modul dafür.

### 7 - Routing

## 2 - Components

### 1 - NgModule and the root module

* Decorator = Ausdrücke, die Annotationen zu Designzeit erlauben
* Syntax:
  * `@Component()` - DecoratorIndicator DecoratorName ()
* Angular-App beginnt mit Angular-MOdul, das mit Decorator konfiguriert wird.
  * Root-Modul ist der Start-Punkt für Angular-App
* app.module.ts - Root-Modul-Class erstellen

```javascript
import { NgModule } from '@angular/core'; //NgModul importieren aus angular/core, mit Komma kann man mehrere Module einfügen
import { BrowserModule } from '@angular/platform-browser'; //um mit DOM arbeiten zu können
import { AppComponent } from './app.component'; //wird die StartComponente, muss noch erstellt werden

//@NgModule-Decorator = man sagt damit das folgende Klasse ein Angular-Modul ist
@NgModule({
    imports: [ //weitere Module/Imports, das dann mein Modul (AppModul) bracht
        BrowserModule
    ],
    declarations: [ //Direktiven, Componenten, Pipes available für eigenen Modul/AppModul machen
        AppComponent
    ],
    bootstrap: [
        AppComponent
    ] //für Root-Modul
}) //was auf den Code danach angewendent werden soll; imports, declarations, bootstrap = Eigenschaften die AppModule benutzt werden sollen
export class AppModule{} //export = sowas wie public
```

### 2 - Directives and pipes

* app.component.ts

```javascript
import { Component } form '@angular/core'; //um Klasse als Componente zu markieren

@Component({
    selector: 'app-root', //Selector, dass in html Stelle für Angular markiert
    template: '<h1>My App</h1>'
})
export class AppComponent {

}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <app-root></app-root> <!-- Root für Angular markieren-->
</body>
</html>
```

### 3 - Bootstrapping the module for the browser

### 4 - The component selector

### 5 - The component template

### 6 - Styling a component

### 7 - Using other components in a component

### 8 - Interpolation and the expression context

### 9 - Property binding

### 10 - Event binding

### 11 - Getting data to the component with @Input

### 12 - Subscribing to component events with @Output

<!-- AB HIER -->
## 3 - Directives and Pipes

### 3 - Attribute directives: Built-in

* Attr Directive = Verhalten der DOM-Elemente verändern
* Structural Directives = Erstellen/Deleten DOM-Elemente

```html media-item-list.component.html
<section>
  <mw-media-item 
    *ngFor="let mediaItem of mediaItems"
    [mediaItem]="mediaItem"
    (delete)="onMediaItemDelete($event)"
    [ngClass]="{'medium-movies': mediaIteam.media === 'Movies', media-series': 'mediaItem.series === 'Series'}"></mw-media-item>
    <!-- ngClass: erwaretet Object-Struktur: {ClassNamen: true/false-Statement}>
</section>
```

### 4 - Attribute directives: Custom

* eigene Direktive erstellen
* die Klasse `is-favorite` zum HTML-Element hinzufügen, wenn HTML-Element die Directive `isFavorite` hat

```ts favorite.directive.ts
@Directive({
  selector: '[mwFavorite]', // [] nötig, da mvFavorite da DOM-Attr sein wird
})

export class FavoriteDirective(){
  @HostBinding('class.is-favorite') isFavorite = true;  // um Klasse auf mit Directive Markiertes Element anzwenden. Verwendet um Host-Eleme zu Directive-Property binden
}
```

```html media-item.component.html
<h2>{{ mediaItem.name }}</h2>
<ng-template [ngIf]="mediaItem.watchedOn">
  <div>Watched on {{ mediaItem.watchedOn }}</div>
</ng-template>
<div>{{ mediaItem.category }}</div>
<div>{{ mediaItem.year }}</div>
<div class="tools">
  <!-- da hier kein Bidning => keien []-->
  <svg mvFavorite class="favorite" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <path d="M12 9.229c.234-1.12 1.547-6.229 5.382-6.229 2.22 0 4.618 1.551 4.618 5.003 0 3.907-3.627 8.47-10 12.629-6.373-4.159-10-8.722-10-12.629 0-3.484 2.369-5.005 4.577-5.005 3.923 0 5.145 5.126 5.423 6.231zm-12-1.226c0 4.068 3.06 9.481 12 14.997 8.94-5.516 12-10.929 12-14.997 0-7.962-9.648-9.028-12-3.737-2.338-5.262-12-4.27-12 3.737z"
    />
  </svg>
  <a class="delete" (click)="onDelete()">
    remove
  </a>
  <a class="details">
    watch
  </a>
</div>
```

* in app.module noch die Direktive bekannt machen

### 5 - Using directive values

```ts favorite.directive.ts
@Directive({
  selector: '[mwFavorite]', // [] nötig, da mvFavorite da DOM-Attr sein wird
})

export class FavoriteDirective(){
  @HostBinding('class.is-favorite') isFavorite = true;  // um Klasse auf mit Directive Markiertes Element anzwenden. Verwendet um Host-Eleme zu Directive-Property binden

  @Input()
  set mwFavorite(value){
    this.isFavorite = value;
  }
}
```

```html
 <svg [mvFavorite]="mediaItem.isFavorite" class="favorite" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <path d="M12 9.229c.234-1.12 1.547-6.229 5.382-6.229 2.22 0 4.618 1.551 4.618 5.003 0 3.907-3.627 8.47-10 12.629-6.373-4.159-10-8.722-10-12.629 0-3.484 2.369-5.005 4.577-5.005 3.923 0 5.145 5.126 5.423 6.231zm-12-1.226c0 4.068 3.06 9.481 12 14.997 8.94-5.516 12-10.929 12-14.997 0-7.962-9.648-9.028-12-3.737-2.338-5.262-12-4.27-12 3.737z"/>
</svg>
```

### 6 - Working with events in directives

* auf Host-Element Events reagieren (hier auf Hover reagieren)
* auf Events reagieren mit `@HostListener`

```ts favorite.directive.ts
@Directive({
  selector: '[mwFavorite]', // [] nötig, da mvFavorite da DOM-Attr sein wird
})

export class FavoriteDirective(){
  @HostBinding('class.is-favorite') isFavorite = true;  // um Klasse auf mit Directive Markiertes Element anzwenden. Verwendet um Host-Eleme zu Directive-Property binden
  @HostBinding('class.is-favorite-hovering') hovering = false;

  @HostListener('mouseenter')
  onMouseEnter(){
    this.hovering = true;
  }

  @HostListener('mouseleave')
  onMouseLeave(){
    this.hovering = false;
  }

  @Input()
  set mwFavorite(value){
    this.isFavorite = value;
  }

  @HostListener
}
```

### 7 - Angular pipes: Built-in

* Anuglar Pipe: Template Expression Operator, das Wert bekommt und return neuen transformierten Wert

```html media-item.component.html
<div> Watched on {{mediaItem.watchedOn | date }} </div>

<div> Watched on {{mediaItem.watchedOn | date: 'shortDate' }} </div>

<h2>{{mediaItem.name | slice: 0: 10}}</h2>

<h2>{{mediaItem.name | slice: 0: 10 | uppercase }}</h2>
```

* Pipe können auch Parameter haben

### 8 - Angular pipes: Custom

```ts category-list.pipe.ts
@Pipe({
  name: 'categoryList' // Name der Pipe
  //pure: true // pure: true => wird die Daten nicht verändern (ist optional)
}) // Param ist Obj
export class CategoryListPipe() implements PipeTransform{
  // man muss die Methode transform implementieren
  transform(mediaItems){ //falls die Pipe Parameters haben soll
    const categories = [];
    mediaItems.forEach(mediaItem => {
      if (categories.indexOf(mediaItem.category) <= -1) {
        categories.push(mediaItem.category);
      }
    });
    return categories.join(', '); // Pipe muss nicht unbedingt einen String returnen
  }
}
```

```html media-item-list.component.html
<section>
  <header>
    <div>{{mediaItems | categoryList }}</div>
  </header>

  <mw-media-item 
    [ngClass]="{'medium-movies': mediaItem.medium==='Movies', 'medium-series':mediaItem.medium==='Series'}"
    *ngFor="let mediaItem of mediaItems"
    [mediaItem]="mediaItem"
    (delete)="onMediaItemDelete($event)"></mw-media-item>
</section>
```

* die Pipe noch in app.modules.ts eintragen

## 4 - Forms

### 1 - Angular forms

* Aufgaben:
  1. Submit = Daten sammeln
  2. in Forms Changes tracken
  3. Daten validieren
      1. Angular Built-in Validators
      2. Custom Validators
      3. Async Validators
      4. Form-Fields in Obj wrappen
  4. Errors anzeigen

* zwei Wege Forms zu erstellen
  1. Template Driven = Form-Logik ist Template
  2. Model Driven = Form-Logi ist in Class-Comp

### 2 - Template-driven forms

* in app.module.ts `FormModule` importieren

* mit NgForm-Directive kann man mit Forms interagieren
* mit NgModel-Directive sagen welche Felder Teil der Form sind

```html media-item-form.component.html
<header>
  <h2>Add Media to Watch</h2>
</header>
<form #mediaItemForm="ngForm"
  (ngSubmit)="onSubmit(mediaItemForm.value)">
  <!-- ngSubmit für Default HTML-Submit Action -->
  <!-- mit #mediaIteForm="ngForm" wird Angular die Form in Variable mediaItemForm exportieren-->
  <ul>
    <li>
      <label for="medium">Medium</label>
      <select name="medium" id="medium" ngModel> <!-- ohne weiter Angaben ngModel ist nur in eine Richtung mit medium verbunden-->
        <option value="Movies">Movies</option>
        <option value="Series">Series</option>
      </select>
    </li>
    <!-- Momentan nur bis hierhin mit der dem ts-Code verbunden da nur hier ngModel-->
    <li>
      <label for="name">Name</label>
      <input type="text" name="name" id="name" ngModel>
    </li>
    <li>
      <label for="category">Category</label>
      <select name="category" id="category" ngModel>
        <option value="Action">Action</option>
        <option value="Science Fiction">Science Fiction</option>
        <option value="Comedy">Comedy</option>
        <option value="Drama">Drama</option>
        <option value="Horror">Horror</option>
        <option value="Romance">Romance</option>
      </select>
    </li>
    <li>
      <label for="year">Year</label>
      <input type="text" name="year" id="year" maxlength="4" ngModel>
    </li>
  </ul>
  <button type="submit">Save</button>
</form>
```

```ts
@Component({
  selector: 'mw-media-item-form',
  templateUrl: './media-item-form.component.html',
  styleUrls: ['./media-item-form.component.css']
})
export class MediaItemFormComponent implements OnInit {
  onSubmit(mediaItem) {
    console.log(mediaItem);
  }
}
```

### 3 - Model-driven forms

* Form wird in .ts definiert. Vorteile:
  1. Form Field contract
  2. Field validation
  3. Change tracking
  4. können unit-getestet werden

* Also
  1. Template Drive: einfach
  2. Model Driven: Full Power

* statt: `FormModule` `ReactiveFormsModule` in app.module.ts importieren. Geht auch beides zu importieren

```ts media-item-form.component.ts
@Component({
  selector: 'mw-media-item-form',
  templateUrl: './media-item-form.component.html',
  styleUrls: ['./media-item-form.component.css']
})
export class MediaItemFormComponent {
  form: FormGroup;

  ngOnInit(){
    this.form = new FormGroup({
      medium: new FormControl('Movies'),
      name: new FormControl(''),
      category: new FormControl(),
      year: new FormControl(),
    });
  }

  onSubmit(mediaItem) {
    console.log(mediaItem);
  }
}
```

```html media-item-form.component.html
<header>
  <h2>Add Media to Watch</h2>
</header>
<!-- Variable form mit diser Form verbinden -->
<form
  [formGroup]="form"
  (ngSubmit)="onSubmit(form.value)"> <!-- als Param Attr des Obj. form werden übergeben-->
  <ul>
    <li>
      <label for="medium">Medium</label>
      <select name="medium" id="medium" formControlName="medium"> <!-- mit FormControl verbinden -->
        <option value="Movies">Movies</option>
        <option value="Series">Series</option>
      </select>
    </li>
    <li>
      <label for="name">Name</label>
      <input type="text" name="name" id="name" formControlName="name">
    </li>
    <li>
      <label for="category">Category</label>
      <select name="category" id="category" formControlName="category">
        <option value="Action">Action</option>
        <option value="Science Fiction">Science Fiction</option>
        <option value="Comedy">Comedy</option>
        <option value="Drama">Drama</option>
        <option value="Horror">Horror</option>
        <option value="Romance">Romance</option>
      </select>
    </li>
    <li>
      <label for="year">Year</label>
      <input type="text" name="year" id="year" maxlength="4" formControlName="year">
    </li>
  </ul>
  <button type="submit">Save</button>
</form>
```

### 4 - Validation: Build-in

```ts
// man kann Build-In Validators an FormControl-Obj und FormGroup-Obj anwenden
ngOnInit() {
    this.form = new FormGroup({
      medium: new FormControl('Movies'),
      //name: new FormControl('', Validators.pattern('[\\w\\-\\s\\/]+')),
      name: new FormControl('', Validators.compose([
        Validators.required,
        Validators.pattern('[\\w\\-\\s\\/]+')
      ])), // im Konstruktor Validator übergeben. Zweite Param bei FormControl ist Validator. Mit compose([]) kann man mehrere Validators übergeben ~ Validators verketten
      category: new FormControl(''),
      year: new FormControl(''),
    });
  }
```

* Angular wird Klasse. `ng-invalid` anwenden an die Form

* `<button type="submit" [disabled]="!form.valid">Save</button>` - Submit-Button disablen, falls Feld invalid ist

### 5 - Validation: Custom

```ts media-item-form.component.ts

year: new FormControl('', this.yearValidator), // eigene Function als Validator verwenden

yearValidator(control: FormControl) {
  if (control.value.trim().length === 0) {
    return null;
  }
  const year = parseInt(control.value, 10);
  const minYear = 1900;
  const maxYear = 2100;
  if (year >= minYear && year <= maxYear) {
    return null;
  } else {
    return { year: true };
  }
}
```

### 6 - Error handling

* Angular fügt Error-Attr wenn Form ist invalid um Errors dann in HTML anzeigen. Ist Attr von `FormGroup`

```html
<header>
  <h2>Add Media to Watch</h2>
</header>
<form
  [formGroup]="form"
  (ngSubmit)="onSubmit(form.value)">
  <ul>
    <li>
      <label for="medium">Medium</label>
      <select name="medium" id="medium" formControlName="medium">
        <option value="Movies">Movies</option>
        <option value="Series">Series</option>
      </select>
    </li>
    <li>
      <label for="name">Name</label>
      <input type="text" name="name" id="name" formControlName="name">
       <!-- Hier wird dann Error angezeigt-->
      <div *ngIf="form.get('name').hasError('pattern')" class="error">
        Name has invalid characters
      </div>
    </li>
    <li>
      <label for="category">Category</label>
      <select name="category" id="category" formControlName="category">
        <option value="Action">Action</option>
        <option value="Science Fiction">Science Fiction</option>
        <option value="Comedy">Comedy</option>
        <option value="Drama">Drama</option>
        <option value="Horror">Horror</option>
        <option value="Romance">Romance</option>
      </select>
    </li>
    <li>
      <label for="year">Year</label>
      <input type="text" name="year" id="year" maxlength="4" formControlName="year">
      <!-- Hier wird dann Error angezeigt. Da man hier ein Obj bei Error return => man kann es hier genauer anzeigen-->
      <div *ngIf="form.get('year').errors as yearErrors" class="error">
        Must be between 
        {{yearErrors.year.min}}
        and 
        {{yearErrors.year.max}}
      </div>
    </li>
  </ul>
  <button type="submit" [disabled]="!form.valid">Save</button>
</form>
```

## 5 - Dependency Injection and Services

### 1 - How Angular does dependency injection

* Dependency Injection => Modularity. Geschieht in zwei Schritten:
  1. Service registrieren = Classen, die injecten werden können. Wird beim Bootstrap registriert + was Decoratro `@Injectobar()`
  2. Services bekommen im Construktor. Man kann auch über globalen Provider Injector auf Services zugreifen

### 2 - Services in Angular

* Services sind:
  1. Data/API-Service => nicht jedes Mal neu die Verbindung aufbauen
  2. Business-Logik z.B gleiche Forms
* Angualar Services: Http, FormBuilder, Router
* sind dann einfacher zu Unit-Testen

### 3 - Class constructor injection

### 4 - Building and providing a service

### 5 - Providing service in the root

### 6 - Using the service in components

### 7 - The @Inject decorator

### 8 - Injection token

## 6 - HTTP

### 1 - The Angular HttpClient

### 2 - Using a mock backend for HTTP calls

### 3 - Using the HttpClient for GET calls

### 4 - Using search params in GET calls

### 5 - Use HttpClient for POST, PUT, and DELETE calls

### 6 - Handling HTTP errors

## 7 - Routing

### 1 - Setting the base href and configuring routes

### 2 - Resitering routing in the app module

### 3 - Routes outlets

### 4 - Routes links

### 5 - Working with route parameters

### 6 - Using the Router class to navigate

### 7 - Using a feature NgModule for routes

### 8 - Lazy loading a route module

## 8 - Styling Components

### 1 - The view encapsulation modes

### 2 - How Angular scopes styles to components

### 3 - Using common CSS selectors

### 4 - Special CSS selectors Angular supports

### 5 - Working with global styles
