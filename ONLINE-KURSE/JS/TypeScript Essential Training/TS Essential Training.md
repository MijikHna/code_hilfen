### 0 - Introduction
* TS erweitert JS
* github.com/jchadwick/EssentialTypeScript
#### 4 - Introducing TypeScript
ist Static-Typ Sprache
Dynamic Language | Static Language
---| ---
typisiert | typisiert
"Duck" Typing <- Objekt die sozusagen Klasse "ANY" sind | Static Typing <- Klasse
Forgiving = Fehler erst zur Laufzeit | Rigid = Compiler findet Fehler
Gut für Browserr object Model | Mehr Stabilität udn Maintabilität

#### 5 - Defining JS
* TS ist SuperSet von JS
* ECMASCript Browser Compatibility chechen, wenn man eine JS-Technik verwendet
* TS => wird zu ECMAScript 5 übersetzt (JS Transpiler)
    * ECMAScript 5 versucht in JS "Klassen" einzuführen
#### 6 - Writing first TS function
* *typescriptlang.org* -> auch Downloaden
    * **Play** - Lifeübersetzung von TS zu JS
```ts
function speak(value){
function speak(value: string){ //Parameter als string definieren
function speak(value: string): string{
    document.write(value);
    return value;
    return value.length;
    return value;
}

var greeted = "World";
var greeted = 42;
var greeted = 42;



var greeting = "Hello, ";
var greeting = "Hello, ";
var greeting = 1;

var whatToSay = greetig + greeted;
var whatToSay: string = greetig + greeted; //zu string explizit konvertieren
var whatToSay: string = greetig.toString() + greeted.toString();

speak(whatToSay);
```

### 1 - Configuring Your Environment
#### 1 - Choosing your TS editor
* Editor + TS Compiler
* TS Compiler installieren
    1. als VS Erweiterung installieren
    2. mit npm 
* TS wurde von Microsoft entwickelt

#### 2 - Installing TS in VS
* nicht VS Code
#### 3 - Installing TS CLI
* `npm install -g typescript`
    * `tsc --version` 
* Lite-Server installieren
    * `npm install -g lite-server` (oder auch live-server usw.)
#### 4 - Creating a TS project
* Ordner erstellen -> dort .ts-Dateien ablegen
    * dort auch `index.html` erstellen mit `<script type="text/javascript" src="app.js"></script>`
    * `tsc datei.ts` - .ts zu .js kompilieren, dabei gleicher Name verwendet für .hs
    * `tsc -w datei.ts` - -w = --watch = schauet, ob .ts Datei verändert wurde.
* damit man nicht jedes Mal lange Optionen von `tsc` eingeben muss => tsconfig.json erstellen
    * mit STRG+SPACE => Vorschläge anzeigen
```json
{
    "compilerOptions": {
        "target": "es5"
    }
}
```
* wenn `tsc` sieht diese Dateie => er behandelt ganzen Order + Subordner als großen Project dann
    * `tsc -w` = schauen nach Änderungen im ganzen Ordner
### 2 - ES6 Language Features ( - sind JS Feateures, nicht TS)
#### 1 - Review ES6 language features
#### 2 - Default parameters
* Optionale Parameter -> Default Values
```ts
var container = document.getElementById("container");

function countdonw(initial, final = 0, interval = 1){
    var current = initial;

    while(current > final){
        container.innerHTML 0 current;
        current -= internal;
    }
}

countdown(10,0,1);
countdonw(10);
```
* man kann in .js-Datei schauen, was JS daraus macht
#### 3 - Template strings
```ts
var container = document.getElementById("container");

var todo = {
    id: 123;
    name: "Pick up";
    completed: true;
}

var displayName = `ToDo #${todo.id}`
```
* statt normalen Quotes (', ") \` benutzen
* `${}` hier kommt beliebige JS-Ausdruck
+ in \` kann " und ' und mehrere Zeilen im String benutzen
    * ```<i class="${ todo.completed ? "" :"hidden" }>...</i>```
#### 4 - Let and const
* davor war nur `var`
    * `var` ist immer global
    * `let` - Variable wird nur im Scope bekannt/gesehen
    * `const` - wie in anderen Normalen Sprachen
#### 5 - For...of loops
* früher:
```js
for (var index in array){
    var value= array[index];
    console.log(value);
}
```
* jetzt
```js
for (var value of array){
    console.log(value);
}
```
#### 6 - Lambdas
* JS
```javascript
var container = document.getElementById("container");

function Counter(el){
    this.count = 0;

    el.innerHTML = this.count;

    el.addEventListener("click", function(){
        this.count += 1;
        el.innterHTML = this.count;
    });
}

new Counter(container);
```
* Problem `this` in `function(){..}` bezieht sich auf übergeben-Objekt = DOM-Objekt
+ Lösung:
```javascript
var container = document.getElementById("container");

function Counter(el){
    this.count = 0;

    el.innerHTML = this.count;

    let _this = this;

    el.addEventListener("click", function(){
        _this.count += let _this:any;
        el.innterHTML = _this.count;
    });
}

new Counter(container);
```
* Referenz zu this speichert => 
* bessere Lösung:
```javascript
var container = document.getElementById("container");

function Counter(el){
    this.count = 0;

    el.innerHTML = this.count;

    el.addEventListener("click", () => {
        this.count += 1;
        el.innterHTML = this.count;
    });
}

new Counter(container);

var filtered = [1,2,3].filter((x)) => {
    return x > 0;
}

var filtered = [1,2,3].filter((x) => x > 0);
```
* `=>` = Arrow-Funktionen in ES5 => Lambda (wie in JAVA und C#)
* jede JS-Funtion kann man zu Arrow-Funktion umwandeln
* ??? nicht ganz verstanden
#### 7 - Destructuring
* Wert mehreren Variablen zuweisen in einer Anweisung
```js
var array = [123, "String", false];
var [id, title, completed] = array; //Werte aus array den Array aus Variablen zuweisen

var a = 1;
var b = 5;
[a,b]=[b,a]; //erleichtert Variablen-Switching

var todo = {
    id: 124,
    title: "String",
    completed: false;
}
var {id, title, completed} = todo; //{}, da todo.id, todo.title usw.
var {title, completed, id} = todo; //wird trotzdem richtig zugwiesen
var {title, completed : isCompleted, id} = todo; //todo.completed an "var isCompleted" zuweisen


function countdown( {title, completed : isCompleted, id} ){
    //...
}

countdown(todo); //Vorteil in Funkt-Parameter-Übergabe

```

#### 8 - The spread operator
* JS alt. Funktion die variable Liste an Parametern aufnmmt. Nachteil Code ist schwer lesbar
```ts
function add(){
    var values = Arrays.prototype.splice.call(arguments, [1]), total=0;
    for (var value of values){
        total += value;
    }
    return total;
}
```
* JS ES5
```ts
// 1. Verwendung 
function add(...values){
    vat total = 0;
    for (var value of values){
        total += value;
    }
    return total;
}

function add(action, ...values){
    vat total = 0;
    for (var value of values){
        total += value;
    }
    return total;
}
//2. Verwendung -> Injection
var source = [3,4,5];
var target = [1,2,3,...source, 6,7,];


var list = [1,2];
var toAdd= [3,4];
list.push(...toAdd);
```
#### 9 - Computed properties
* Variablennamen eines Objekt dynamisch erstellen dafür `[]` benutzen
```ts
var support = {
    "os_Windows" : isSupported("Windows");
    "os_iOS" : isSupported("iOS");
}

const osPrefix="os_";

var support = {
    [osPrefix + "Windows"] : isSupported("Windows"), //sind jetzt Compputed Properties
    [osPrefix + "iOS"] : isSupported("iOS"),
}

function isSupported(os){
    return Math.random() >=0.5;
}
```
### 3 - Type Fundamentals
#### 1 - Introducing JS types
* JS-Typen -> ECMAS5Script Typen:
    * `boolean` - immutable (nicht veränderbar)
    * `number` - immutable
    * `string` - immutable
    * `null/undefined`
    * `object` -> "key" : "value"
        * `function` - hat auch Eigenschaften
        * `array` - hat auch Eigenschaftene -> "value"
        * `...prototype`
    * Object Literal:
        * `{}` - leeres Object
        * `{ name: "Fido", species: "Dog",}`
        * `{ name: "Fido", species: "Dog", speak: function(){...}}`
        * `var animal = { name: "Fido", species: "Dog", speak: function(){...}}`
            * `animal.speak();`    
#### 2 - Understanding type inference
* in TS kann man immer noch JS programmieren
* man muss nicht unbedingt in TS den Typen deklarieren. TS kann es zur Programmierzeit selbst herausfinden.
    * wenn TS den Typen nicht herausfinden kann => ordnet `any` zu. `any` ist beliebiges Object auch Funktion.
#### 3 - Specifying JavaScript types
* Bsp:
```js
//function totalLength(x, y){
//function totalLength(x:, y): number {
function totalLength(x: any[], y): number { // x als Array deklarieren
    var total = x.length + y.length;
    //var tot(local var) total: any h; - intern wird dieses gemacht
    var total: number = x.length + y.length;
    return total;
}
```
* 
#### 4 - Specifying function parameter types
* Union-Type: mit Pipe-Operator: `|` + Typen in Klammern
* Bsp:
```js
function totalLength(x: (string | any[]), y: (string | any[])): number {

    var total = x.length + y.length;
    //var tot(local var) total: any h; - intern wird dieses gemacht
    x.slice(0);

    if ( x instanceof Array ){
        x.push("abs");
    }

    if (typeof x === "string" ){ //typeof funktioniert nur für Primitive Typen (String ist in JS/TS primitiver Typ)
    //if( x instanceof String){
        x.substr(1);
    } 
    var total: number = x.length + y.length;
    return total;
}
```
* weiterer Vorteil: Intellecens wird Funktion von beiden anzeigen
* damit TS-Intelicense nicht mekert muss man bei Callen der entsprechenden Funktionen in if verpacken:
```js
if ( x isinstanceof Array ){
    x.arrayFunktion();
}
```
#### 5 - Adding function overloads = Überladung
* Bsp:
```js
function totalLength(x: string, y:string): number{/*..*/}
function totalLength(x: any[], y:any[]): number {/*..*/}
//<- wird nicht funktionieren, da zweiter Funktionsname würde einfach die erste Funktion überschreiben. In JS wird einfach überschrieben
//ABER
function totalLength(x: string, y:string): number
function totalLength(x: any[], y:any[]): number
//funktioniert und unten die Funktionen komplett programmieren

function totalLength(x: (string | any[]), y: (string | any[])): number {

    var total = x.length + y.length;
    //var tot(local var) total: any h; - intern wird dieses gemacht
    x.slice(0);

    if ( x instanceof Array ){
        x.push("abs");
    }

    if (typeof x === "string" ){ //typeof funktioniert nur für Primitive Typen (String ist in JS/TS primitiver Typ)
    //if( x instanceof String){
        x.substr(1);
    } 
    var total: number = x.length + y.length;
    return total;
}
```
* wobei am Ende in JS wird erstellt nur eine Funktion mit den `instanceof`-Abfragen.

## Hier fängt wirkliches TS an
### 4 - Custom Types
#### 1 - Defining custom types with interfaces
* Drei Möglichkeiten eigene Typen zu deklarieren
    1. Interfaces
    2. Classes
    3. Enums
* Interface - beschreibt Daten und Funktionen, die ein Objekt haben soll
```ts
interface ToDo{
    name: string;
    completed?: boolean; //mit ? optionales Attr definieren
}

interface IToDoService{
    add(toDo: ToDo): ToDo; //Funktionen deklarieren (function-keyWord auslassen)
    delete(toDoId: number): void;
    getAll(): ToDo[];
    getById(toDoId: number): ToDo;
}

var todo: ToDo = {}; //Fehler, da ein leeres Objekt, obwohl zwei Attr haben sollte
var todo  = <ToDo>{}; //Ok (Casting-Syntag) - Typ des Objekts spezifizieren
var todo: ToDo = {
    name: "123";
    completed: true;
};
var todo: ToDo = {
    name: "123";
};
```
* *IToDoServer* muss man noch als Klasse erstellen
* werden zur Compilier-Zeit ausgewertet
#### 2 - Using interfaces to describe
* Funktionen sind auch Objekte, die selbst Attribute haben können
```ts
var $ = function(selector){
    //
}

$.version = 1.12 //da von Object/any erbet hat diesen Attribute


//
interface jQuery{
    (selector: string): HTMLElement;
    version: number;
}

var $ = <jQuery>function(selector){ //Interface an Funktion anwenden. Diese Funktion ist jetzt vom Typ jQuery
    //
}
var element = $('#container')
```
#### 3 - Extending interface definitions
#### 4 - Defining constant values with enums
#### 5 - Defining anonymous types

### 5 - Classes
#### 1 - Understanding prototypical inheritance
#### 2 - Defining a class
#### 3 - Applying static properties
#### 4 - Making properties smarter with accessors
#### 5 - Inheritance bahaviour from a base
#### 6 - Implementing an abstract class
#### 7 - Controlling visibility with access modifier
#### 8 - Implementing interfaces

### 6 - Generics
#### 1 - Introducing generics
#### 2 - Creating generic classes
#### 3 - Applying generic constraints

### 7 - Modules
#### 1 - Understanding the need for modules in JS
#### 2 - Organizing your code with namespaces
#### 3 - Using namespaces to encapsulate private members
#### 4 - Understanding the difference between internal and external modules
#### 5 - Switching from internal to external modules
#### 6 - Importing modules using CommonJS syntax
#### 7 - Importing modules using ECMAScript 2015 syntax
#### 8 - Loading external Modules

### 8- Real-World Application Dev
#### 1 - Introducing the sample JS app
#### 2 - Converting existing JS code to TS
#### 3 - Generating declaration files
#### 4 - Referencing third-pary libraries
#### 5 - Converting to external modules
#### 6 - Debugging TS with source maps

### 9 - Decorators
### 1 - Implementing method decorators
### 2 - Implementing class decorators
### 3 - Implementing property decorators
### 4 - Implementing decorator factories