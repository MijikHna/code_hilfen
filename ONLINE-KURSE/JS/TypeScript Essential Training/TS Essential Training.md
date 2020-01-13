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
* Interface beschreibt Eigenschaften + Methoden eines Obj
* Bsp: eigene jQuery
```ts
interface toDo{
    name: string
    completed?: boolean;
}

interface jQuery{
    (selector: (string|any)):jQueryElement;
    fn: any;
    version: number;
}

interface jQueryElement{
    data(name: string): any;
    data(name: string, data: any): jQueryElement;
}

interface jQueryElement{
    todo(): Todo;
    todo(todo: Todo): jQueryElement;
} //erweitert statt überschreibt schon vorhandene Interface -> sollte man für den Code anwenden, der einem nicht gehört

$.fn.todo = function(todo?: Todo) : ToDo {
    if(todo){
        $(this).data("todo", todo);
    }
    else{
        return $(this).data("todo");
    }
} //hier wird todo-Funktion an fn-Object added => man kann es an jedem jQuery aufrufen

var todo = {name: "pick up dycleaning"};
var container = $('#container');
container.data("todo", todo);
var savedTo = container.data("todo");

container.todo(todo);
```
* jQuery return jQuery-Object und nicht HTML-Obj. jQuery-Obj hat Methoden
#### 4 - Defining constant values with enums
* so wie in andren Sprachen
```ts
interface Todo {
    name: string;
    state: number;
}

var todo: ToDo = {
    name: "Test"
    state: ToDoState.New //oder TodoState[1]
}

enum ToDoState{
    New = 1,
    Active,
    Complete,
    Deleted,
}

//Zugriff z.B:
ToDoState[todo.state]
```
#### 5 - Defining anonymous types
+ = interfaces inline deklarieren
```ts
var todo: {name: string}; //inline

todo = {age: 41}

function totalLength(x: {length: number}, y {lenght: number}): : number { //hier inline => jedes Obje, dass Eigenscahft length hat
    var total = x.length + y.length;
    //var tot(local var) total: any h; - intern wird dieses gemacht
    var total: number = x.length + y.length;
    return total;
}
```
### 5 - Classes
#### 1 - Understanding prototypical inheritance
* JS hat mit ES2015 Schlüsselwort `class` aber eigentlich ist immer noch bloß ein Objekt. JS kann auch Inheritance
* Inheritance wird über `varName.prototyp` gamacht. Ref zu "Basisklasse". Geschieht im Konstruktor.
```ts
// ist Konstuktor
function ToDoService(){
    this.todos = [];
}

//Funktion am prototype erstellen
ToDoService.prototype.getAll = function{
    return this.todos;
}

var service = new TodoService();
service.getAll();

// beide greifen auf das gleiche Obj.
```
+ in Entwickler Tools: `Object.prototype` eingeben bzw. an verschiedenen Objekten testen
#### 2 - Defining a class
```ts
class TodoService{ //Klasse definieren

    //Möglichkeiten Attribute zu definieren
    todos: //ES2015
    todos: Todo[]; //TS
    todos: Todos[] = []

    constructor(todos: Todo[]){
        this.todos = [];
    }

    //ODER alles in einem
    constructor(private todos: Todo[]){

    }

    getAll(){
        return this.todos
    }

}
```
* besser als prototype-Sachen von JS
#### 3 - Applying static properties
* statisches Attribute, dass für alle Instanzen z.B **conter**
* in JS hat man einfach globale Variable deklariert
```ts
//ES2015
function TodoService(){

}

TodoService.lastId = 0;

TodoService.getNextId = function(){
    return TodoService.lastId += 1;
}

Todoservice.prototype.add = function(todo){
    var newId = TodoService.getNextId();
}

//TS
class TodoService{ //Klasse definieren
    
    static lastId: number = 0;

    //ODER alles in einem
    constructor(private todos: Todo[]){
    }

    add(todo: Todo){
        var newId = TodoService.getNextId();
    }

    getAll(){
        return this.todos
    }

    static getNexId(){
        return TodoService.lastId += 1;
    }

}
```
#### 4 - Making properties smarter with accessors
* getter und setter erstellen
```ts
interface Todo{
    name: string;
    state: ToDoState; //ist enum
}

var todo = {
    name: "test"
    get state(){ //getter direkt im Obj definieren
        return this._state;
    }
    set state(newState){

        if (newState == ToDoState.Complete){
            var canBeCompleted = this.state == ToDoState.Active || this.state ==TodoState.Deleted;

            if(!canBeCompleted){
                throw "Error"
            }
        }
        this._state = newState; //hier _state dynamisch erstellt.
    }
}

todo.state = ToDoState.Complete;
```
* wenn man getter + setter in Klasse definiert => muss man `_state` als Attribure haben
#### 5 - Inheritance bahaviour from a base
+ ES2015 hat auch Inheritance
```ts
class ToDoStateChanger {

    constructor(private newState: ToDoState): boolean{

    }

    canChangeState(todo: Todo){

    }
}
```
```ts
class CompleteTodoStateChanger extends ToDoStateChanger{

    //man kann hier auch keinen Konstruktor geben => wird Konstruktor von Basis genommen
    constructor(){
        super(ToDoState.Complete); //Basis-Konstruktor aufrufen
    }

    //Methoden von Basis überschreiben
    canChangeStage(todo: Todo): boolean{
        return super.canChangeState(todo); //auf Basis-Funktionen mit super zugreifen 
    }
}
```
* Abstrakte Klassen können nicht Basis-Klassen sein
#### 6 - Implementing an abstract class
* ES2015 hat keine abstrakten Klassen
```ts
abstract class ToDoStateChanger {

    constructor(private newState: ToDoState): boolean{

    }

    abstract canChangeState(todo: Todo);
}
```
* <- einfach `abstract` benutzen, auch Methoden der Klasse kann man abstrakt machen => muss in Child überschrieben werden.
```ts
class CompleteTodoStateChanger extends ToDoStateChanger{

    //man kann hier auch keinen Konstruktor geben => wird Konstruktor von Basis genommen
    constructor(){
        super(ToDoState.Complete); //Basis-Konstruktor aufrufen
    }

    //Methoden von Basis überschreiben
    canChangeStage(todo: Todo): boolean{
        return super.canChangeState(todo); //kann dann aber hier nicht aufgerufen werden, da Methode absrakt
    }
}
```
#### 7 - Controlling visibility with access modifier
* `private`, `public`, `protected` usw.
+ `public` ist default
* ABER JS hat kein `private` => sind eigentlich zum Entwickeln gedacht
```ts
class ToDoService{
    private static lastId: nubmer = 0;
    
    constructor(private todos: ToDo[]){

    }

    private get nextId(){
        return ToDoService.getNextId();
    }

    private set nextId(nextID){
        ToDoService.lastId = nextId - 1;
    }

}
```
* getter und setter müssen gleichen Modifier haben
* da TS von Microsfot ist => markiert private mit `_varName` markieren und im Code sollte man diese Namen nicht benutzen.
#### 8 - Implementing interfaces
* Interface an Klasse binden
* eigentlich sollte nur die Obj-Struktur mit der Interface-Struktur übereinstimmen.
```ts
class ToDoService() implements IToDoService, IIdGenerator {

    getAll(): ToDo[]{
        var clone = JSON.stringify(this.todos);
        return JSON.parse(clone);
        //es werden hier nicht die Original-Daten versenden, dami man mit Ihnen nichts anstellen kann.
    }
}
```
* RANDNOTIZ: wenn man in der Klasse `get` bzw. `set` implementiert => werden direkt als `priate` Attriubte der Klasse angelegt
### 6 - Generics
#### 1 - Introducing generics
* 
```ts
function clone(value){ //hier sollte Funktion den Typ zurückgeben, der auch value ist
//ABER: in JS kann jetzt string Inhalt von belibigem Typen sein => return könnte komplett was anderes als String sein
    let serialized = JSON.stringify(value);
    return JSON.parse(serialized)
}

function clone<T>(value: T): T{ //jetzt kann man T an Stellen nutzen ,wo man einen Typ eingeben 
    let serilized = JSON.stringify(value);
    return JSON.parse(serialized)
}

clone("String");
clone(123);
clone(todo);
clone({name: "String"}) //hier wir z.B unnamed Typ benutzt
```
#### 2 - Creating generic classes
* 
```ts
var array: number[] = [1,2,3];
var arrray2: Array<number> = [1,2,3];

class KeyValuePair<TKey, TValue>{

    construktor(
        public key: TKey,
        public value: TValue,
    ){

    }
}

let pair1 = new KeyValuePair(1, "First");
let pair = new KeyValuePair("First", 1);

let pair1 = new KeyValuePair<number, String>(1, "First");
let pair = new KeyValuePair<stirng, Date>("First", 1);
```
#### 3 - Applying generic constraints
* 
```ts
function totalLength<T extends {length: number }>(x: T, y: T): T {
function totalLength<T extends IterfaceX >(x: T, y: T): T
    var total: number = x.length + y.length;
    return total
}

var length = totalLength()

class CustomArray<T> extends Array<T> {
} // Basic-Array erweitern
```
* aber hier wird Error kommmen, da es nicht bekannt ist ob T Attribute `lenght` hat => Lösung `extends Typ`
### 7 - Modules
#### 1 - Understanding the need for modules in JS
* Module = Komponenten getrennt halten
* ES2015 hat Module bekommen
* Methoden der Abschottung:
    * Module Pattern und revealing(aufschlussreich) Module Pattern
    + Namespaces
    + Module Loader
#### 2 - Organizing your code with namespaces
* 

```ts
namespace ToDoApp.Module{
    export interface Todo{

    }

    export enum ToDoState{
        New = 1;
    }
}

namespace DataAccess{

    import ToDo = ToDoApp.Module 

    export interfac IToDoServie{
        add (todo ToDoApp.Module.todo);
        delete (todo Todo)
    }
}
```
* <- ist alles erlaubt
* <- JS wird aber erst Code produzieren, wenn man im Namespace Definitionen sind, die Code brachen z.B `enum` (`interface` => kein Code)
+ mit `export` den Typen exportieren = nach Außen bekannt machen + im andren Namespace mit `import` bekannt machen, da sonst nur über ganzen Namen erreichbar sind
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