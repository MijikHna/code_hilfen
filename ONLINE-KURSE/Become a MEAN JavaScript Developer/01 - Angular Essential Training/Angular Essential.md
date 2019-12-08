### 0 - Introduction
#### 1 - Why use Angular?
* ist Java-Framework
* hat Dependency Injection eingebaut
* -> zum bilden Client-Applications
#### 2 - What you should know?
#### 3 - Using the exercise files
* nmp lernen
* angluar cli lernen
    + <- gibt es alles auf Lynda
#### 4 - Basics of TypeScript
* ist in TypoScript geschrieben
    * TypoScript:
        * ES2015 classen
        * Module
        * Typisierung der Variablen
    * in TypoScript kann man auch JS schreiben
* TypoScript to Know:
    * Klassen schreiben
    * Angular Decoratoren
    * Parameter Type Annotationen
* Bsp TypoScript:
```javascript
import {Component} from 'angular2/core';
import {FromBuilder} from 'angular2/core'; //Imports

@Component({ //TypeScript-Dekorator
    selector: 'media-tracker-app'
    templateUrl: './app.component.html'
    styleUrls: ['./app.compoments.css']
})

export class AppComponent { //Klass-Def - Klass-Syntax ist ES2015; export - Klass zum Modul umwandlen
    constructor(fromBuilder: FromBuilder) {} //Konsturktor ist ES2015-syntax; in () - Angular-Typisierung
}
```
#### 5 - Course overview

### 1 - Architecure Overview
#### 1 - Components, Bootstrap and the DOM
* Angular wird aus Componenten gebildet (Baum-Struktur ähnlich dem DOM-Baum). Starte ist **Bootstraping-Component**
* Angular startet mit Bootstrap-Call -> dann schauet es nach ob es weitere Compoenent gibt
* Componenten rendert Teil von HTML und zugehörige Funktionen zu diesem Teil. In diesem Component-Klasse ist die Logik des Components
    * Component kann z.B *mediaItem* haben und *onDeleteClick*. 
* Mit Componenten kann man HTML-Templates erstellen
    * in HTML selbst wird Template-Syntax benutzt.
#### 2 - Directives and pipes
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
#### 3 - Data binding
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
#### 4 - Dependendy injection
* DI
* `Constructor(formBuilder: formBuilder){}` - wird oft in Konstruktoren benutzt
* `bootstrap(App, [FormulaService]);` - auch bei bootstrap oft benutzt
* d.h. Dependencies für Componenten liefert
#### 5 - Services and other business logic
* Serivces -> Pattern, Klasslogik
* dann mit DI an Componenten ausliefern
* Klassen müssen nicht unbedingt in Angular sein
#### 6 - Data persistence
* man kann Daten zu/von API holen mit http (XHR, JSONP). Angular hat ein Modul dafür.
#### 7 - Routing
* 

### 2 - Components
#### 1 - NgModule and the root module
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
#### 2 - Directives and pipes
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

#### 3 - Bootstrapping the module for the browser
#### 4 - The component selector
#### 5 - The component template
#### 6 - Styling a component
#### 7 - Using other components in a component
#### 8 - Interpolation and the expression context
#### 9 - Property binding
#### 10 - Event binding
#### 11 - Getting data to the component with @Input
#### 12 - Subscribing to component events with @Output

### 3 - Directives and Pipes
#### 1 - Structural directives: nglf
#### 2 - Structural directives: ngFor
#### 3 - Attribute directives: Built-in
#### 4 - Attribute directives: Custom
#### 5 - Using directive values
#### 6 - Working with events in directives
#### 7 - Angular pipes: Built-in
#### 8 - Angular pipes: Custom

### 4 - Forms
#### 1 - Angular forms
#### 2 - Template-driven forms
#### 3 - Model-driven forms
#### 4 - Validation: Build-in
#### 5 - Validation: Custom
#### 6 - Error handling

### 5 - Dependency Injection and Services
#### 1 - How Angular does dependency injection
#### 2 - Services in Angular
#### 3 - Class constructor injection
#### 4 - Building and providing a service
#### 5 - Providing service in the root
#### 6 - Using the service in components
#### 7 - The @Inject decorator
#### 8 - Injection token

### 6 - HTTP
#### 1 - The Angular HttpClient
#### 2 - Using a mock backend for HTTP calls
#### 3 - Using the HttpClient for GET calls
#### 4 - Using search params in GET calls
#### 5 - Use HttpClient for POST, PUT, and DELETE calls
#### 6 - Handling HTTP errors

### 7 - Routing 
#### 1 - Setting the base href and configuring routes
#### 2 - Resitering routing in the app module
#### 3 - Routes outlets
#### 4 - Routes links
#### 5 - Working with route parameters
#### 6 - Using the Router class to navigate
#### 7 - Using a feature NgModule for routes
#### 8 - Lazy loading a route module

### 8 - Styling Components
#### 1 - The view encapsulation modes
#### 2 - How Angular scopes styles to components
#### 3 - Using common CSS selectors
#### 4 - Special CSS selectors Angular supports
#### 5 - Working with global styles