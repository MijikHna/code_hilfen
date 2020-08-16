# 5 - Data Types

## 1 - Methods of primitives

* auf Primitive Typen kann auch Obj.Methoden ihrer Wrapper Klassen anwenden. d.h wenn man so eine Methode aufruft es wird Wrapper-Obj des Prim. Typen erstellt und Methode ausgeführt. => sind immernoch "lightweight"
* man kann Wrapper ohne `new` benutzen um zu konvertieren, z.B. `let num = Number("123");`

## 2 - Numbers

* = Integers und Doubles
* `255..toString(16)` - als Hex; `255..toString(2)` - als Binär
  * `..` da sonst würde als double annehmen
* weitere Number-Methoden
* `isNan(x)` - checken ob NaN
* `isFinite(x)` - checken ob angemessene Zahl
* `Object.is(obj1, obj2)` vergleicht, ob zwei Object gleich sind
* `parseInt('100');`, `parseFloat('100)`, `parseInt('100px');`

## 3 - Strings

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

## 4 - Arrays

### Declaration

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
* man kann `lenght` beschreiben, wenn man es erhöht passiert nichts, wenn man es verkleinert => Array wird verkleinert
* `let arr = new Array("zero", "one")` oder `let arr = new Array(2)`
* Multidim Arrays:

```js
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
```

## 5 - Array methods

### Add/Remove

* `arr.push(...items)` – adds items to the end,
* `arr.pop()` – extracts an item from the end,
* `arr.shift()` – extracts an item from the beginning,
* `arr.unshift(...items)` – adds items to the beginning.

### splice

* Bsp:

```js
let arr = ['one', 'two', 'three'];
delete arr[1]; //wird nicht wirgklich gelöscht, sonder wird null gesetzt
console.log(arr.length);
console.log(arr[1]) //undefinded
```

* => Array muss noch geshiftet werden
* Syntax: `arr.splice(index[, deleteCount, elem1, ..., elemN])` - wird für insert, remove und replace verwendet- startet bei `index` und löscht von da die Anzahl an Elementen von `deleteCount` und insertet an diese Stellen `elem1 .. elemN`; auch negatives Index erlaubt.

```js
let arr = ['one', 'two', 'three'];
arr.splice(1, 1); //da kein elemX => wird nichts inserted
console.log(arr);

arr.splice(0,2, 'one.one', 'one.two'); // wird nur inserted
```

### `slice`

* Syntax: `arr.slice([start], [end]);`
* returnt Copy von start bis end

```js
let arr = ['one', 'two', 'three'];
console.log(arr.slice(1,3)
console.log(arr.slice(-2))
```

* ohne Argument => wird oft zum Kopieren des Array benutzt

### `concat`

* `arr.concat(arg1, arg2, ...);` - returnt `arr mit angehängtem arg1 ...

```js
let arr = [1, 2];
console.log(arr.concat([3,4]));
console.log(arr.concat([3,4], [5,6]));
//man kann auch Obj anhängen:
let lala = { //ArrayLike-Obj
  0: "lala";
  length: 1;
}:
console.log(arr.concat(lala)); wird als object Object angehängt

//Wenn aber ArrayLike Obj Sybmol.isConcatSpreadable Eigenschaft hat => wird auch als Array interpretiert
let lala2 0 {
  0: "lala";
  1: 'lala2";
  [Symbol.isContatSpreadable]: true;
  length: 2;
};
console:log(arr.concat(lala2));
```

### Iterate: forEach

* für jedes Element des Array gleiche Funkt/callback laufen lassen
* `arr.forEach(function(item, index, array){ ... });`

```js
let arr = [1,2,3];
arr.forEach(alert);

arr.forEach((item, index, array) => {
  alert(`${item} is at index ${index} in ${array}`)
});
```

### Searching in Array

* `arr.indexOf(item. from)`
* `arr.lastIndexOf(item, from)` - returnt index von `item` oder `-1` wenn nicht gefunden.
* `arr.includes(item,from)` - returt `true` wenn gefunden
  * sucht nach `item` ab Index `from`

### find and findIdex

* `arr.find(function(item, index, array)){}` bzw. `arr.find(func)` - wenn gefunden bzw. `true` returned, wir item zurückgegeben und Iteration aufgehört

```js
let users = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"}
];

let user = users.find(item => item.id == 1);

console.log(user.name);
```

* `arr.findIndex()` ist ungefähr gleich. Aber return index des gefundenObj.

### filter

* `arr.filter(func)`; - ähnich wie find, aber returnt Array von gefundenen Obj.

```js
let users = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"}
];

let someUsers = users.filter(item => item.id < 3); //returnt id==1, und id=2
console.log(someUsers);
```

### map

* `arr.map(fn)` bzw.let `result = arr.map(function(item, index, array) { ... });` - ruft Function `fn` die dann auf jedes Elem des Array angewendet wird und returnt den neuen Wert

```js
let lengths = ["Bilbo", "Gandalf", "Nazgul"].map(item => item.length);
alert(lengths); // 5,7,6
```

### sort(fn)

* sortiert Array **in place**. returnt sortierten Array

```js
let arr = [ 1, 2, 15 ];

arr.sort();

console.log(arr); // 1,15, 2 -> da nach ASCII sortiert wird

fucntion compareNumber(a,b){
  if (a > b)
    return 1;
  if (a == b)
    return 0;
  if (a < b)
    return -1;
}

arr.sort(compareNumeric);

console.log(arr); //1,2,3
```

* `fn` kann beliebige Zahl returnen: <0 => less, ==0 => equal, >0 => greater

```js
let arr = [1,2,15];
arr.sort(function(a,b) {return a-b;});
console.log(arr);

//ODER

let arr = [1,2,15];
arr.sort((a,b) => a - b);
console.log(arr);
```

* bei Strings von anderen Alphabeten `str.localCompare()` benutzen:

```js
let countries = ['Österreich', 'Andorra', 'Vietnam'];
alert( countries.sort( (a, b) => a.localeCompare(b) ) ); // Andorra,Österreich,Vietnam (correct!)
```

### reverse

* Reihenfolge von Elementen reversen `arr.reverse()`

### split and join

* `str.split(delim)`
* `str.split()` hat optionales zweites Param = Limit des Arrays
* `arr.join(delim)`

```js
let names = 'Bilbo, Gandalf, Nazgul';

let arr = names.split(', ');

for (let name of arr) {
  console.log(`A message to ${name}.`);
}

let splitted = arr.split(', ', 2); //Bilbo, Gandalf

let chars = "test".split(''); //trennt bei jedem Zeichen

let strName = splitted.join(';');
```

### reduce/reduceRight

* über einen Array iterieren: `forEach`, `for` oder `for..of`
* über einen Array iterieren und Daten jedes Elements returnen: `map()`
* `arr.reduce()` bzw. `arr.reduceRight()` - Wert kalkulieren, der von bestimmten Werten der Elemente des Array abhängt: `let value = arr.reduce(function(accumulator, item, index, array) { // ...}, [initial]);`
* `accumulator` – is the result of the previous function call, equals initial the first time (if `initial` is * provided).
* `item` – is the current array item.
* `index` – is its position.
* `array` – is the array.

```js
let arr = [1, 2, 3, 4, 5];

let result = arr.reduce((sum, current) => sum + current, 0);

alert(result);
```

### Array.isArray

* da Arrays auch Obj sind => wird `typeof []` auch `object` liefern
* ABER: `Array.isArray([])` wird `true` liefern, wenn Array übergeben wird.
* alle Methoden wie `find, fitler, map usw.` können als Param auch `thisArg` annehmen. wird zu `this` für `fn`

```js
let army = {
  minAge: 18,
  maxAge: 27,
  canJoin(user) {
    return user.age >= this.minAge && user.age < this.maxAge;
  }
};

let users = [
  {age: 16},
  {age: 20},
  {age: 23},
  {age: 30}
];

// find users, for who army.canJoin returns true
let soldiers = users.filter(army.canJoin, army); //hier wird eigentlich nur Funktion canJoin außerhalb des Obj army aufgerufen => weiß nicht was this.minAge/this.age usw. ist, deswegen, wird army als Context für den canJoin Aufruf mitgegeben.
```

## 6 - Iterables

* Iterable Obj => ist dann `for .. of` verwendbar
* Arrays sind iterierbar. Aber auch strings
* Um Obj. iterierbar zu machen => Methode `Symbol.iterator` hinzufügen
* wenn `for..of` aufgerufen wird => wird iterator-Obj returnt, der Methode `next()` hat. Wenn `for..of` dann zum nächsten Obj springen will ruft es `next()` auf.

```js
let range001 = {
  from: 1;
  to: 5;
}; // momentan noch nicht iterierbar

let range002 = {
  from: 1;
  to: 5;
};

range002[Symbol.iterator] = function(){
  return {
    current this.from,
    last: this.to,

    next(){
      if (this.current <= this.last){
        return {
          done: false;
          value: this.current++;
        }
      }
      else{
        return{
          done: true;
        }
      }
  };
};

for (let num of range){
  console.log(num);
}
```

* eigentlich hat `range002` hat eigentlich keine Methode `next()`. Mit dem Aufruf `range[Symbol.itrator]` wird ein anderes Obj. (iterator-Obj) returnt, der diese Methode hat und `next()` generiert dann `value` für die Iteration. Also iterator-Obj ist vom eigentlich Obj. getrennt
* Implementierung Variante 2:

```js
let range003 = {
  from: 1,
  to: 5,

  [Symbol.iterator]() {
    this.current = this.from;
    return this;
  },

  next() {
    if (this.current <= this.to) {
      return { done: false, value: this.current++ };
    } else {
      return { done: true };
    }
  }
};

for (let num of range) {
  alert(num); // 1, then 2, 3, 4, 5
}
```

* Bsp Iteration über string

```js
for (let char of "test") {
  alert( char ); // t,e,s,t
}
```

### Iterator explizit aufrufen

* Bsp: Iterator für String erstellen und die Werte des Iterator manuell bekommen

```js
let str = "Hello";

let iterator = str[Symbol.iterator]();

while (true) {
  let result = iterator.next();
  if (result.done) break;
  console.log(result.value); // outputs characters one by one
}
```

* hier hat `range003` selbst die Methode `next()`. Nachteil hierbei, dass man nicht mehr kann den Iterator an mehreren Stellen gleichzeitig aufrufen
* ! man kann auch unendliche Iteratoren erstellen

### Iterables und Array-Likes

1. Iterables = Objekte, die Symbol.iterator() implmenetieren
2. Array-Like = Objekte, die Index und Length haben

* Strings sind beides: Array-Like + Iterables (for..of)
* Obiges Bsp sind keine Array-Like, da kein `length` haben
* Bps Array-Like:

```js
let arrayLike = {
  0: "Hello",
  1: "World",
  length: 2
};


for (let item of arrayLike) {} //Error, da nicht Iterables
```

* beide haben kein `push()` `pop()`

### Array.from
* `Array.from()` nimmt als Param Iterables oder Array-Like und macht darauch echtes Array:

```js
let arrayLike = {
  0: "Hello",
  1: "World",
  length: 2
};

let arr = Array.from(arrayLike);
console.log((arr.pop()); // 
```

* checkt ob `arrayLike` Iterables oder Array-Like ist, macht neues Array kopiert die Werte darein und return den Array
* Eigentliche Syntax: `Array.from(obj[, mapFn, thisArg])` -> Bsp 1:

```js
let arr = Array.from(range, num => num * num);
```

* Bsp 2 :

```js
let str = '𝒳😂';

// splits str into array of characters
let chars = Array.from(str);

alert(chars[0]); // 𝒳
alert(chars[1]); // 😂
alert(chars.length); // 2
```

## 7 - Map and Set

* Map = Sammlung von keyed Items. Key kann von beliebigem Typ sein.
* Wichtige Methoden:
  * `new Map()` – creates the map.
  * `map.set(key, value)` – stores the value by the key.
  * `map.get(key)` – returns the value by the key, undefined  if key doesn’t exist in map.
  * `map.has(key)` – returns true if the key exists, false  otherwise.
  * `map.delete(key)` – removes the value by the key.
  * `map.clear()` – removes everything from the map.
  * `map.size` – returns the current element count.
* Bsp:

```js
let map = new Map();

//Key ist beliebiger Typ
map.set('1', 'str1');
map.set(1, 'num1');
map.set(true, 'bool1');

alert( map.get(1)   ); // 'num1'
alert( map.get('1') ); // 'str1'

alert( map.size ); // 3
```

* funktioniet auch `map[key] = 2` ist aber besser über Methoden
* Key kann auch Obj sein

### Iteration über Map

* dafür drei Methoden:
  1. `map.keys()` – returns an iterable for keys,
  2. `map.values()` – returns an iterable for values,
  3. `map.entries()` – returns an iterable for entries [key, value], it’s used by default in for..of.
  * Bsp: siehe Seite
* hat eingebaute Methode `forEach()`, Bsp. recipeMap.forEach( (value, key, map) => {console.log(`${key}: ${value}`);`

### Object.entries: Map from Object

* wenn `Map` erstellt wird, kann man Iterables-Obj dem Map-Konstruktor übergeben, er wird daraus selbst die Map-Einträge erstellen:

```js
let map = new Map([
  ['1',  'str1'],
  [1,    'num1'],
  [true, 'bool1']
]);

console.log( map.get('1') );
```

* wenn man Plain-Text hat, kann man daraus `Map` mit Methode: `Object.entries(obj)` erstellen. Bsp:

```js
let obj = {
  name: "John",
  age: 30
};

let map = new Map(Object.entries(obj));

alert( map.get('name') );
```

* `Object.entries` returnt eigentlich Array von key-value Paaren: [ ["name","John"], ["age", 30] ]
* `Object.fromEntries` macht das Gegenteil, also erstellt Obj aus Key-Value-Array z.B `let obj = Object.fromEntries(map.entries())`. als Param erwartet Iterables

### Set

* eigentlich Map aber wo jedes Wert nur ein Mal vokommen kann.
* Basis Funktionen:
  1. `new Set(iterable)` – creates the set, and if an iterable object is provided (usually an array), copies values from it into the set.
  * `set.add(value)` – adds a value, returns the set itself.
  * `set.delete(value)` – removes the value, returns true if value existed at the moment of the call, otherwise false.
  * `set.has(value)` – returns true if the value exists in the set, otherwise false.
  * `set.clear()`  – removes everything from the set.
  * `set.size` -  is the elements count.

* über Set kann man mit `for..of` oder mit `.forEach()` iterieren. (Callback für `forEach()` ist etwas spezifisch)

## 8 - WeakMap and WeakSet

* WeakMap/Set => hindert den GC nicht davon das Obj, dass Key in Map ist zu zerstören.
  1. Key muss Obj sein
  2. wenn es keine Ref außer in WeakMap/Set gibt => wird zerstört => wird auch aus WeakMap/Set gelöscht
* Basis Funktionen:
  * `weakMap.get(key)`
  * `weakMap.set(key, value)`
  * `weakMap.delete(key)`
  * `weakMap.has(key)`

### Use Case 1: Additional Data:

* wenn man mit Obj. der anderen Libs arbeitet, die weitern Data Storage benutzen. Man addet das Obj. zu WeakMap und wenn das Obj zuerstört wird => wird auch aus WeakMap deleted. (mit normaler Map, müsste man dann selbst aufräumen)

### Use Case 2: Caching

* wenn z.B Ergebnis einer Funkt. sollte gecached werden.

## 9 - Object.keys, values, entries

* Methoden für Plain Obj.
  * `Object.keys(obj)` – returns an array of keys.
  * `Object.values(obj)` – returns an array of values.
  * `Object.entries(obj)` – returns an array of [key, value] pairs.
* eigentlich ähnliches Verhalten für Objekte wie bei Maps implementieren:
* Bsp: 

```js
let user = {
  name: "John",
  age: 30
};

// loop over values
for (let value of Object.values(user)) {
  alert(value); // John, then 30
}
```

### Transforming Objects:

* Objekte haben keine Methoden, die Arrays haben z.B keine `map()`, `filter()` => um diese auch bei Obj zu haben => muss man so vorgehen:
  1. `Object.entries(obj)`
  2. Methoden des Arrays benutzen z.B map()
  3. `Object.fromEntries(array)` wieder zurück zum Obj zu verwandeln
* Bsp:

```js
let prices = {
  banana: 1,
  orange: 2,
  meat: 4,
};

let doublePrices = Object.fromEntries(
  // convert to array, map, and then fromEntries gives back the object
  Object.entries(prices).map(([key, value]) => [key, value * 2])
);

console.log(doublePrices.meat); // 8
```

## 10 - Destructuring assign

### Array Destructuring

* Syntax um Arrays/Obj auszupacken z.B bei Übergabe als Param an Funktionen und als andere Variablen zu übergeben.

```js
let arr = ["Ilya", "Kantor"]

// destructuring assignment
let [firstName, surname] = arr;

alert(firstName); // Ilya
alert(surname);  // Kantor

//kürzere Alternative mit split()
let [firstName, surname] = "Ilya Kantor".split(' ');

//eigentlich eine Erleichterung für folgende Schreibweise
let firstName = arr[0];
let surname = arr[1];

//mit leerer Var kann man bestimmte Werte überschrieben bei Destructuring
let [firstName, , title] = ["Julius", "Caesar", "Consul", "of the Roman Republic"]; //Caeser übersprungen

// kann für jedes Iterable-Obj verwendet werden
let [one, two, three] = new Set([1, 2, 3]);

//kann man auch mit Attr. der Obj machen
let user = {};
[user.name, user.surname] = "Ilya Kantor".split(' ');

//Object.entries(obj) kann man Destructuring für Obj verwenden
let user = {
  name: "John",
  age: 30
};

// loop over keys-and-values
for (let [key, value] of Object.entries(user)) {
  alert(`${key}:${value}`); // name:John, then age:30
}

// Bsp für Destructuring für Map
let user = new Map();
user.set("name", "John");
user.set("age", "30");

for (let [key, value] of user) {
  alert(`${key}:${value}`); // name:John, then age:30
}

// oft wird Destructuring zum Werte vertauschen verwendet
[guest, admin] = [admin, guest];
```

#### The rest `...`

* wenn man den Rest in andere Var. speichern möchte

```js
let [name1, name2, ...rest] = ["Julius", "Caesar", "Consul", "of the Roman Republic"];

alert(name1); // Julius
alert(name2); // Caesar

alert(rest[0]); // Consul
alert(rest[1]); // of the Roman Republic
alert(rest.length); // 2
```

* wenn rechte Seite keine Werte für die linke Seite mehr hat => werden sie `undefined` gesetzt
* man kann aber Default-Werte verwenden: `let [name = "Guest", surname = "Anonymous"] = ["Julius"];`

### Object Destructuring

* Syntax: `let {var1, var2} = {var1:…, var2:…}`

```js
let options = {
  title: "Menu",
  width: 100,
  height: 200
};

// hier Destructuring
let {title, width, height} = options;

// Die Reihenfolge ist egal
let {height, width, title} = { title: "Menu", height: 200, width: 100 }

// wenn die Variablen anders als Obj-Attr heißen soll
let {width: w, height: h, title} = options; //hier z.B Var w und h statt width and height (width geht in w, height geht in h rein)

//genauso kann man Default-Werte verwenden (Default Werte können auch Funktionen sein)
let options = {
  title: "Menu"
};

let {width = 100, height = 200, title} = options;

// Default Werte können auch Funktionen sein
let {width = prompt("width?"), title = prompt("title?")} = options;

// andere Namen + Default-Werte
let {width: w = 100, height: h = 200, title} = options;

// man kann auch Obj-Att auslassen
let options = {
  title: "Menu",
  width: 100,
  height: 200
};

let { title } = options;

// rest pattern ...
let {title, ...rest} = options;

alert(rest.height);  // 200
alert(rest.width);   // 100

// wenn man keinen let benutzt => Fehler, da ohne let werden {} als Block und nicht als Obj interpretiert
let title, width, height;
{title, width, height} = {title: "Menu", width: 200, height: 100}; // hier Error
//Work around ausdruck in () packen
let title, width, height;
({title, width, height} = {title: "Menu", width: 200, height: 100});
```

### Nested destructing

* wenn Array oder Obj weiteres Obj enthält

```js
let options = {
  size: {
    width: 100,
    height: 200
  },
  items: ["Cake", "Donut"],
  extra: true
};

// für title wird Defautl benutzt, extra wird nicht extrahiert
let {
  size: {
    width,
    height
  },
  items: [item1, item2],
  title = "Menu"
} = options;
```

### Smart function params

* wenn man eine Funktion hat mit vielen Params z.B `function showMenu(title = "Untitled", width = 200, height = 100, items = []) {// ...}`, kann man statt jedes einzelne Param zu übergeben Destructuring benutzen -> Obj als Param übergeben und die entsprechenden Param werden gemappt.

```js
// we pass object to function
let options = {
  title: "My menu",
  items: ["Item1", "Item2"]
};

function showMenu({title = "Untitled", width = 200, height = 100, items = []}) {
  // ..
}
function showMenu({
  title = "Untitled",
  width: w = 100,  
  height: h = 200,
  items: [item1, item2] 
}) {
  // ..
}

//
showMenu({}); // alle Werte sind Defaults, showMenu() wird Error liefern
```

#### 11 - Date and time

#### 12 - JSON methods, toJSON
