### 4 - Objects: The basics
#### 1 - Objects
+ Object erstellen
    1. `let obj = {key: value}` mit `{...}` = Object-Literal
    2. `let obj = new Object();` = Object-Konstruktor
* `delete obj.key` - Eigenschaft entfernen
##### Square Brackets und Computed Properties
* mit `obj[key]` = `obj.key` -> wobei in `key` bei `[]` kann man einen String speichert => so über Variablen auf Eigenschften zugreifen. <- kann man auch bei Object-Literal verwendet werden z.B
```js
let fruit = 'apple';
let basket = {
    [fruit]: 5; //computed propety, wird der Wert von fruit genommen
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
* man kann `__proto__`-Wert von Obj nicht auf Non-Obj-Wert setzen:
```js
let obj = {};
obj.__proto__ = 5; // assign a number
alert(obj.__proto__); // [object Object] wird returnt. Also 5 in ein Obj gewrappt.
```
##### Property Exsitence mit "in"-Opertaror abfragen
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
##### Const Object
```js
const user = {
    name: "John"
};
user.age = 25;
```
* wird funktionieren, da const nur für Obj `user` gilt, d.h wenn man z.B `user = user2` würde meckern
##### Cloning and Mergin
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
##### Summary
* Obj = assosiatives Array mit besonderen Features

#### 2 - Object copying, references
* Obj werden by Ref übergeben
* Primitive Var: string, number, boolean werden als by Copy übergeben
```js
let user = {name: "John"}; //user zeigt auf Obj, der Attr. name hat
let admin = user; //zeigt jetzt auf das gleiche Obj.
admin.name = "Jack" // wird auch user.name geändert
``` 
##### Cloning and Merging, Object.assign
* Clonen muss man selbst machen z.B:
```js
let user = {
  name: "John",
  age: 30
};

let clone = {}; // leeres Obj.

// alle Attr. kopieren/clonen
for (let key in user) {
  clone[key] = user[key];
}
```
* alles in Obj mit `Object.assign` reinkopieren
```js
let user = { name: "John" };

let permissions1 = { canView: true };
let permissions2 = { canEdit: true };

Object.assign(user, permissions1, permissions2);

//Ergebnis:
user{
    name: 'John';
    canView: true;
    canEdit: true
}

Object.assign(user, {name: "Jack"}); // hier wird user.name geändert

let clone = Object.assing({}, user); // wird use in leeres Obj kopieren und returnt
```
##### Nestes Cloinig
* Probelem, wenn Obj selbst Obj hat => beim diesem `Object.assing` wird Nested Obje als Ref kopiert => Cloning Loop verwenden und wenn z.B `user[key]` sebst ein Obj ist wieder Clone bzw. `Object.assign` ausführen.
#### 3 - Garbage Collector
* `roots` - Variablen oben im Stack
* Garbage Collector monitort alle Objekte und löscht die, die unreachble geworden sind.
* reachble = sind über `root`-Objekte erreichbar.
#### 4 - Symbol Type
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

function ClassName(lala){
    ...
    this.funcName = function(){
        ...
    };
}

let john = new ClassName(lala);
john.funcName();
```
#### 7 - Optional chaining `?`
* error-proof Method um Nested Obj-Attr zu erreichen.
* Bsp:
```js
let user = {
    x = user.address.street; //Error, da user kein Attr address und address.streat hat

    // z.B kritisch bei Anwendungen
    let html = document.querySelector('.my-element').innerHTML;
}
``` 
* früher hat mans es mit `&&` gelöst: `x = user && user.address && user.address.street`
* `x = user?.address?.street` - hört auf die Attr durchzugehen, sobald eins vor `?` null oder undefined ist.
* `x = user?.address.street.anything` - prüft nur user, wenn existiert wirde komplett bis anything durchgegangen.
* geht auch für Funktionen.
```js
let user1 = {
  admin() {
    alert("I am admin");
  }
}

let user2 = {};

user1.admin?.(); // I am admin
```
+ Bsp mit delete: `delete user?.name;`