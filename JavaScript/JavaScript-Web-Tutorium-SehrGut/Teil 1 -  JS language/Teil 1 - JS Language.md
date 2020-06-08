### 1 - An Intorduciton
* Tutorium: https://javascript.info/

### 2 - JavaScript Fundamentals
#### 3 - The modern mode `'use strict'`
* damit die neuen Features von JS-Code funtionieren, sollte man die Direktive `'use strict'` verwedent am Anfang der JS-Datei, da neue Feauters sind per Default deaktiviert (ab ES5).
* Man dann diese Derektive am Anfang der Funktion nutzen
* sollte als erstes im Code stehen, sonst nicht enabled. Nur Kommentare sind davor erlaubt.
* man kann in Browser-Console auch `'use strict'` aktivierten.
    1. `Shift+Enter` um Multilines einzugeben
    2. `use strict'`
* sonst wird **default mode** statt **strict** mode verwendet.
#### 4 - Variablen
* guter Stil Konstanten, die beim Start des Scripts initialisiert werden, komplett Groß zu schreiben
##### 5- Data types
* Java ist dynamically typed Sprache
* 8 Datentypen
    1. Number `let varX = 5;`
    2. BigInt `let varX = 1234567890123456789012345678901234567890n;`<- `n` am Ende
    3. String
        1. in `"`
        2. in `#`
        3. in \` - extended functionality Quotes. Variablen und Expression im String vereinen. `${..}` hat Expression drin
    4. Boolean
    5. `null`
    6. `undefined` - wenn Variable deklariert, aber nicht assigned
    7. Object
    8. Symbol - um unique identifier für Objekt zu erstellen
    9. `typeof`-Operator

#### 6 - Type Converions
##### String Convertion
```js
let value = true;
value = String (value);
```
##### Number Converion
```js
let str = "123";
let num = Number (str);
```
##### Boolean Converion
```js
let bool = Boolean (1); //true
bool = Boolean("test"); //true
bool = Boolean(""); //false
```
#### 7 - Operators
+ Unärere `+` und `-` kann man auch für Convertiertung zu Number verwenden => kürzere Schreibweise
* `2**3` - 2 hoch 3
* comma operator allows us to evaluate several expressions, dividing them with a comma ,. Each of them is evaluated but only the result of the last one is returned.
```js
let a = (1 + 2, 3 + 4);
alert( a ); // 7 (the result of 3 + 4)
```
* hat die niedrigste Priotirät, sogar `=` ist höhrer => deswegen hier im Bespiel `()`
#### 8 - Comparisons
* man kann auch Strings vergleichen
#### 9 - Interaction: alert, prompt, confirm
* Alert: `alert(message);`
* Prompt: `result = prompt(title, [default]);` - in `result` wird die Eingabe gespeichert.
* Confirm: `result = conrifm(question)`. ist yes-no-question
#### 10 - Conditional operators: if; ?
* `""`, `null`, `undefined`, `NaN`, `0` = false
* `let accessAllowed = (age > 18) ? true : false;`
* `(company == 'Netscape') ? alert('Right!') : alert('Wrong.');`
* Multiple `?`
```js
let message = (age < 3) ? 'Hi, baby!' :
  (age < 18) ? 'Hello!' :
  (age < 100) ? 'Greetings!' :
  'What an unusual age!';
```
#### 11 - Logical Operators
* sind in JS etwa powerfuller
* Bsp `||`
    * `result = value1 || value2 || value3;`
        * Evaluates operands from left to right.
        * For each operand, converts it to boolean. If the result is true, stops and returns the original value of that operand.
        * If all operands have been evaluated (i.e. all were false), returns the last operand.
    * `true || (x = 1);` - wenn erste Expression true => wird abgebrochen
* Bsp `&&`
    * `result = value1 && value2 && value3;`
        * Evaluates operands from left to right.
        * For each operand, converts it to a boolean. If the result is false, stops and returns the original value of that operand.
        * If all operands have been evaluated (i.e. all were truthy), returns the last operand.
* `!!` wird manchmal benutzt um Wert zu boolean zu convertieren.
#### 12 - Loops
* man kann Labels für `break` und `continue`
    * label = identifier with a colon before a loop. `break LabelName` - bricht aus dem gelabeltem Loop
    ```js
    outer: for (let i = 0; i < 3; i++) {

    for (let j = 0; j < 3; j++) {

        let input = prompt(`Value at coords (${i},${j})`, '');

        // if an empty string or canceled, then break out of both loops
        if (!input) break outer; // (*)

        // do something with the value...
    }
    }
    alert('Done!');
    ```
    * sonst würde nur inneren Loop beenden
#### 14 - Functions
* Parameter werden als Copy übergeben
* Default Values
    * kann auch Call der Funktion sein: `function showMessage(from, text = anotherFunction()) { ... }`
* empty return = `undefinded`
* wenn man längere Expression return will => Klammern benutzen:
```js
return (
  some + long + expression
  + or +
  whatever * f(a) + f(b)
  )
```
#### 15 - Function Expressions
* = alternative Schreibweis zum Deklarieren von Funktionen:
```js
let funcName = function(){

};
* braucht Semikolon am Ende, da Wert-Zuweisung
```
* wenn man z.B `alert(funtName)` also ohne `()` aufruft, wird Inhalt der Funktion ausgegeben. Funktion ist ein Objekt und so greift man einfach auf den Value dieses Objects
* => man kann z.B Funktioen kopieren: `let funcName2 = funcName1`
##### Callback functions
```js
function ask(question, yes, no) {
  if (confirm(question)) yes()
  else no();
}

function showOk() {
  alert( "You agreed." );
}

function showCancel() {
  alert( "You canceled the execution." );
}

// usage: functions showOk, showCancel are passed as arguments to ask
ask("Do you agree?", showOk, showCancel);
```
* `yes`/`showOK()` und `no`/`showCancel()` sind Callback-Funktionen. Funktioniert wegen dem oberen Teil, dass funcName=Value
* alternative für `ask()` mit Function Expression
```js
ask(
  "Do you agree?",
  function() { alert("You agreed."); },
  function() { alert("You canceled the execution."); }
);
```
* Vorteil: sind nur in `ask()` zugänglich, da keinen Varialben-Namen haben = Anonymous
#### Function Expression vs Function Declarion
* Function Declaration = Funktion als Statement deklariert <-> sind zu bervorzugen
    * Function Deklartion ist nur im Scope sichtbar indem diese Funktion definiert wurde.
+ Function Exprssion = Funktion deklariert als Expression
    * eigentliche Funktion wird erstellt, wenn Function Expressoin von Interpreter errreicht wird. => wenn Functional Expression nach dem Funtionsaufruf steht => Error
#### 16 - Arrow Functions, the Basics
* Arrow Funktions eigentlich küzere Schreibweise für Fuction Expressions:
```js
let func = (arg1, arg2, ...argN) => expression
// ==
let funcName = function(arg1, arg2, ...argN) {
  return expression;
};
```
* konreter Bsp:
```js
let sum = (a, b) => a + b;
// ==
let sum = function(a,b){
    return a + b;
}
```
* wenn `expression` mehrzeilig ist => in `{}`einschließen + `return` wenn man etwas return werden muss
```js
let sum = (a, b) => {  
  let result = a + b;
  return result;
};
```
### 3 - Code Quality
#### 1 - Debugging Chrome
* mit `debugger` im Code kann man direkt BreakPoint setzen für Chrome Debugger
* Chrome Debugger: 
    1. Watch = Werte der Varialben
    2. Call Stack = nested function calls
    3. Scope = current Variables
#### 2 - Codin Style
* Bsp wie man Linter in package.json einstellen kann
#### 3 - Comments:
* Bsp guter Kommentar:
```js
/**
 * Returns x raised to the n-th power.
 *
 * @param {number} x The number to raise.
 * @param {number} n The power, must be a natural number.
 * @return {number} x raised to the n-th power.
 */
```
* Doku zu JavaScript Kommentaren: https://en.wikipedia.org/wiki/JSDoc
* Tool das aus Dokumentations-Kommentaren Dokumentation erstellt: https://github.com/jsdoc3/jsdoc bzw. http://usejsdoc.org/
* Eventuall müssen Kommentare sagen **Why is the task solved exactly this way?**
* Fazit: folgendes sollte man kommentieren
    * Overall architecture, high-level view.
    * Function usage.
    * Important solutions, especially when not immediately obvious.
#### 5 - Automated testing with Mocha
* Development Flow von BDD - Behaviour Driven Development = zuerst Test, dann Implementation
    1. An initial spec is written, with tests for the most basic functionality.
    2. An initial implementation is created.
    3. To check whether it works, we run the testing framework Mocha (more details soon) that runs the spec. While the functionality is not complete, errors are displayed. We make corrections until everything works.
    4. Now we have a working initial implementation with tests.
    5. We add more use cases to the spec, probably not yet supported by the implementations. Tests start to fail.
    6. Go to 3, update the implementation till tests give no errors.
    7. Repeat steps 3-6 till the functionality is ready.
* Bsp: 
    * Benutzt:
        1. Mocha = Core Framework zum Testen (`describe`, `it`)
        2. Chai = Library mit `assert` + `toBe...`
        3. Sinon = Library zum `spyOn`
* One Test checks One Thing
#### 6 - Polyfills
* Babel = Transpiler = rewrites aktuellen JS-code zu früherer Version
+ Babel besteht aus zwei Teilen
    1. Transpiler = Programm, das Code rewritet. z.B WebPack führt Transpiler automatisiert aus = Integriert in Development Prozess.
    2. Polyfill = A script that updates/adds new functions is called “polyfill”. It “fills in” the gap and adds missing implementations. Zwei wichitgsten Polifills:
        1. `core.js`
        2. `polyfill.io`
### 4 - Objects: The basics
#### 1 - Objects
+ Object erstellen
    1. `let obj = {key: value}` mit `{...}` = Object-Literal
    2. `let obj = new Object();` = Object-Konstruktor
* `delete obj.key` - Eigenschaft entfernen
* mit `obj[key]` = `obj.key` -> wobei in `key` bei `[]` kann man einen String speichert => so über Variablen auf Eigenschften zugreifen. <- kann man auch bei Object-Literal verwendet werden z.B
```js
let fruit = apple;
let basket = {
    [fruit]: 5;
};
```
##### Property value shorthand
```js
function makeUser(name, age) {
  return {
    name: name,
    age: age,
  };
}
// ==
function makeUser(name, age) {
  return {
    name,
    age,
  };
}
```

* <- in Key bekommen den gleichen Namen wie Values
* wenn man Eigenschaft anspricht, die nicht existeirt => `undefiened`, kein Error
    * `"key" in obj` - chekcen, ob `key` in Objekt existiert; tuue wenn ja.
##### for .. in - Loop
```js
for (key in obj){
    //...
}

for (let key in obj){
    //...
}
```
* `obj.newKey="lala"` - so kann man dem Obje neue Eigenschaften adden
* Objekte sind Referenzen. => bei Paramterüber bzw. Kopieren `let admin = user` = byReference
#### Const Object
```js
const user = {
    name: "John"
};
user.age = 25;
```
* wird funktionieren, da const nur für Obj `user` gilt, d.h wenn man z.B `user = user2` würde meckern
#### Cloning and Mergin
* neues Objekt erstellen und über Eigenschaften iterieren und kopieren.
* man kann auch die `Object.assign(dest, [src1, src2, ...])` dafür benutzen. Wenn `dest` schon die Eigenschaft hat => wird überschrieben.
```js
let user = { name: "John" };

let permissions1 = { canView: true };
let permissions2 = { canEdit: true };

Object.assign(user, permissions1, permissions2);

// now user = { name: "John", canView: true, canEdit: true }
```
* wenn Eigenschaft des Obj selbst ein Obj ist => deep Cloning = über Eigenschaftn iterieren und checken, ob sie selbst ein Obj sind. 
#### Summary
* Obj = assosiatives Array mit besonderen Features
#### 2 - Garbage Collector
* `roots` - Variablen oben im Stack
* Garbage Collector monitort alle Objekte und löscht die, die unreachble geworden sind.
* reachble = sind über `root`-Objekte erreichbar.
#### 3 - Symbol Type
```js
let id = Symbol("id");
let user = {
  name: "John",
  age: 30,
  [id]: 123
};
```
* statt normaler `id` als String `id` als `Symbol`-Obj benutzen => ist unique => wenn anderer Teil des Programms braucht eigene `id` wird diese nicht überschrieben.
    * werden in `for ..in` nicht berücksichtigt = werden übersprungen.
    * Zugriff nur mit `obj.[id]`
* Globale Symbole = wenn verschiedene Teile des Programms gleiches Symbol ansprechen sollen
    1. Sybmol in **global symbol registery** erstellen mit `Symbol.for(key)`
    ```js
    // read from the global registry
    let id = Symbol.for("id"); // if the symbol did not exist, it is created

    // read it again (maybe from another part of the code)
    let idAgain = Symbol.for("id");

    // the same symbol
    alert( id === idAgain ); // true
    ```
    2. `Symbol.keyFor(sym)` - returnt Namen des globalen Symbols
    ```js
    // get symbol by name
    let sym = Symbol.for("name");
    let sym2 = Symbol.for("id");

    // get name by symbol
    alert( Symbol.keyFor(sym) ); // name
    alert( Symbol.keyFor(sym2) ); // id
    ```
* System Symbols
    * es gibt Syste Symole, die von JS intern benutzt werden. -> Siehe Doku von JS (Well-known Symbols)
+ Summary:
    * Symbole haben zwei Ziele:
        1. Obj Propeties verstecken. = Etwas in das Objekt einschmugeln
        2. System-Symbole kann man mit `Symbol.*` ansprechen. => um Build-in Behaviors zu verändern z.B Iterator-Verhalten ändern über `Symbol.iterator`
#### 4 - this
* Optionen Methode einem Obj zuzuweisen
    * Optioen 1:
    ```js
    let user = {
        name: "John",
        age: 30
    };

    user.sayHi = function() {
        alert("Hello!");
    };

    //Aufruf
    user.sayHi();
    ```
    * Option 2:
    ```js
    let user = {
        name: "John",
        age: 30
    };

    function sayHi() {
        alert("Hello!");
    };

    // Methdoe dem Obj zuweisen
    user.sayHi = sayHi;

    //Aufruf
    user.sayHi();
    ```
    * Option 3:
    ```js
    user = {
        sayHi: function() {
            alert("Hello");
        }
    };
    ```
    * Option 4:
    ```js
    user = {
        sayHi() {
            alert("Hello");
        }
    };
    ```
    * Optionen 3 und 4 sind im Background unterschiedlich (Inheritance)
* Bsp mit `this`
    * mit `this`
    ```js
    let user = {
        name: "John",
        age: 30,

        sayHi() {
            // "this" is the "current object"
            alert(this.name);
        }
    };
    ```
    * ohne `this` stattdessen direkt über Obj-Namen ansprechen -> Nachteil: wenn man jetzt Obje `user` z.B zu `admin` umbenennt muss man es auch in der Funktion machen. Oder die `user`-Instanz kopiert => wird dann aus der kopierten Instanz dieser `user` angesprochen
    ```js
    let user = {
        name: "John",
        age: 30,

        sayHi() {
            // "this" is the "current object"
            alert(user.name);
        }
    };
    ```
* `this` kann in jeder Funktion benutzt werden. `this` wird bei run-time mit dem Context belegt. Wenn es auf `this.xxx` nicht zugreifen kann => `undefined` in strict mode, nicht strict mode => wird `window`. Bsp:
```js
let user = { name: "John" };
let admin = { name: "Admin" };

function sayHi() {
  alert( this.name );
}

// use the same function in two objects
user.f = sayHi;
admin.f = sayHi;

user.f(); // John  (this == user)
admin.f(); // Admin  (this == admin)
```
* Arrow-Funktionen haben keinen eigenen `this`. Sie benutzen `this` der/des äußeren Object/Funktion=Context:
```js
let user = {
  firstName: "Ilya",
  sayHi() {
    let arrow = () => alert(this.firstName);
    arrow();
  }
};

user.sayHi();
```
* <- noch Mal lesen + Aufgaben noch Mal durchgehen
#### 5 - Object to primitive conversion
* Um zu Convertiert versucht JS drei Object-Methoden zu finden:
1. Call `obj[Symbol.toPrimitive](hint)` – the method with the symbolic key `Symbol.toPrimitive` (system symbol), if such method exists:
    1. build-In-Symbol wo die Kovertierungsmethode gespeichert ist: `obj[Symbol.toPrimitive] = function(hint) {...}` => muss dann (über)-schreiben
2. Otherwise if hint is "string" try `obj.toString()` and `obj.valueOf()`, whatever exists.
    * wandelt Obj zum Stirng, wenn 1) nicht da ist. Kann man auch überschreiben also `toString()` für String-Operationen und/oder `valueOf()` für nummerische Operationen überschreiben
3. Otherwise if hint is "number" or "default" try `obj.valueOf()` and `obj.toString()`, whatever exists

#### 6 - Constructor, operator "new"
##### Constructor Function
1. Name der Funktioen mit Großbuchstaben beginnen (ist aber kein Muss)
2. wird mit `new` executed
* Bsp:
```js
function User(name = "Musterman") {
    this.name = name;
    this.isAdmin = false;
}
let user = new User("Kirill");
```
+ wenn Funktion mit `new` ausgeführt wird => folgendes passiert:
    1. `this = {}` - leeres Obj wird erstellt und an `this` zugewiesen
    2. `this.xxx` - Eigenschaften ans `this` werden vergeben
    3. `this` wird returned
* Bsp: Konstructor direkt callen:
```js
let user = new function() {
  this.name = "John";
  this.isAdmin = false;
}
```
* `new.target` - gibt innerhalb des Objects an, ob Construktor-Funktion mit `new` aufgerufen wurde.
* Wenn man Constr-Funkt mit `return xxx` beendet => wird anstelle von `this` `xxx` returnt.
##### Methoden in Constructor
```js
...
this.funcName = function(){
    ...
};
```
### 5 - Data Types
#### 1 - Methods of primitives
* auf Primitive Typen kann auch Obj.Methoden ihrer Wrapper Klassen anwenden. d.h wenn man so eine Methode aufruft es wird Wrapper-Obj des Prim. Typen erstellt und Methode ausgeführt. => sind immernoch "lightweight"
* man kann Wrapper ohne `new` benutzen um zu konvertieren, z.B. `let num = Number("123");`
#### 2 - Numbers
* = Integers und Doubles
* `255..toString(16)` - als Hex; `255..toString(2)` - als Binär
    * `..` da sonst würde als double annehmen
* weitere Number-Methoden
* `isNan(x)` - checken ob NaN
* `isFinite(x)` - checken ob angemessene Zahl
* `Object.is(obj1, obj2)` vergleicht, ob zwei Object gleich sind
* `parseInt('100');`, `parseFloat('100)`, `parseInt('100px');`
#### 3 - Strings
* Format ist UTF-16
* mit \` kann man auch mehrzeilige Strings schreiben, die dann mehrzeilig ausgegeben werden. Außerdem kann man damit **template functions** realisieren -> siehe Doku
mit `"\u{xxxxxxxx}` kann man Unicode-Zeichen realisieren
* `str.length`
* `str.[i]` oder `str.charAt(i)`
* über String iterieren
```js
for(let charAt_i of "Hello"){
    console.log(charAt_i);
}
```
* Strings sind immutable
* weitere String-Methoden
#### 4 - Arrays
##### Declaration
* `let arr = new Array();` oder `let arr = []` oder `let arr = ['zero', 'one', two', 'three' ]`;
* Element adden: `arr[4] = 'four'`
* `arr.length`
* Array kann verschiedene Objekte beinhalten sogar Funktionen
* Arrays als Queue FIFO=> `push("new")`, `shift()`
* Arrays als Stack LIFO => `push("new")`, `pop()`
* `unschift("new")` - wird aber an den Anfang des Array angehängt
* da Arrays Objekte sind => folgendes ist erlaubt, dabei geht aber die Array-Optimisierung verloren: 
```js
let fruits = []; 
fruits[99999] = 5; 
fruits.age = 25; 
```
* `for (let i of arr)` - spezielle for-Form für Arrays -> sind aber eigentlich für Generische Objekte gedacht
* `length` = letzter Index + 1, nicht Anzahl der Elemente
+ man kann `lenght` beschreiben, wenn man es erhöht passiert nichts, wenn man es verkleinert => Array wird verkleinert
* `let arr = new Array("zero", "one")` oder `let arr = new Array(2)`
* Multidim Arrays:
```js
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
```
#### 5 - Array methods
* 
#### 6 - Iterables
#### 7 - Map and Set
#### 8 - WeakMap and WeakSet
#### 9 - Object.keys, values, entries
#### 10 - Destructuring assign
#### 11 - Date and time
#### 12 - JSON methods, toJSON

### 6 - Advanced working with functions
### 7 - Object properties configurations
### 8 - Prototypes, inheritance
### 9 - Classes
### 10 - Error handling
### 11 - Promises, async/await
### 12 - Generators, advanced iteration
### 13 - Modules
### 14 - Miscellaneous
