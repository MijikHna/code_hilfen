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
#### 12 - Nullish coalescing operator ??
* älter Browser brauchen eventuell polyfills
* verkürzte Syntax um ersten `defined` zu wählen aus einer Liste
* `a ?? b` - return ist `a` wenn `a` nicht `null` oder `undefined` sonst `b`
* also `x = a ?? b` =  `x = (a !== null && a !== undefined) ? a : b;`
* Bsp:
```js
let firstName = null;
let lastName = null;
let nickName = "Supercoder";

// Code zum belegen von firstName, lastName, wenn User z.B nichts einträgt bleibt null

// show the first not-null/undefined value
alert(firstName ?? lastName ?? nickName ?? "Anonymous"); // Supercoder
```
* eigentlich ziemlich änlich mit `||`
    1. `||` returnt ersten **truthy**
    2. `??` returnt ersten `defined`
* verboten `||` oder `&&` mit `??` zu benutzen. Ausnahme, wenn man Ausdrücken klammert:
    1. error: `let x = 1 && 2 ?? 3;`
    2. ok: `let x = (1 && 2) ?? 3;`
#### 13 - Loops
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
#### 15 - Functions
* globale Variablen werden von lokalen überdeckt.
* Parameter werden als Copy übergeben
* Default Values
    * kann auch Call der Funktion sein: `function showMessage(from, text = anotherFunction()) { ... }`
    * man kann auch in der Funktion überprüfen, ob param `=== undefined` ist bzw. `param = param || 'leer'` benuzten oder `??`
* empty return = returnt `undefinded`
* wenn man längere Expression return will => Klammern benutzen:
```js
return (
  some + long + expression
  + or +
  whatever * f(a) + f(b)
  )
```
* Eine Funktion = Eine Aktion
+ sehr kurze Funktionen haben oft Prefix wie z.B Funktionen in `jQuery` beginen mit `$`, in `Lodash` mit `_`
* interessantes Bsp mit JUMP -> ist aber BAD PRACTISE
```js
function showPrimes(n) {
  nextPrime: for (let i = 2; i < n; i++) {

    for (let j = 2; j < i; j++) {
      if (i % j == 0) continue nextPrime;
    }

    alert( i ); // a prime
  }
}
```
* bessere Lösung
```js
function showPrimes(n) {

  for (let i = 2; i < n; i++) {
    if (!isPrime(i)) continue;

    alert(i);  // a prime
  }
}

function isPrime(n) {
  for (let i = 2; i < n; i++) {
    if ( n % i == 0) return false;
  }
  return true;
}
```
#### 16 - Function Expressions
* Syntax 1:
```js
function funcName(){

}
```
* Syntax 2: (alternative Schreibweis zum Deklarieren von Funktionen)
```js
let funcName = function(){

};

funcName2 = funcName;
//Call 1
funcName // // = wird nur der Inhalt der Funk returnt, da ja Variable ist
console.log(funcName); 
funcName(); // wird wirklich ausgeführt
```
* braucht Semikolon am Ende, da Wert-Zuweisung. Also wird der Variablen der Name der Funkt zugewiesen.
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
    * Bsp:
    ```js
    function sum(a, b) {
        return a + b;
    }
    ```
+ Function Expression = Funktion deklariert als Expression
    * eigentliche Funktion wird erstellt, wenn Function Expression von Interpreter erreicht wird. => wenn Functional Expression nach dem Funktionsaufruf steht => Error
    * Bsp:
    ```js
    let sum = function(a, b) {
        return a + b;
    };
    ```
#### 17 - Arrow Functions, the Basics
* Arrow Funktions eigentlich küzere Schreibweise für Fuction Expressions:
```js
let func = (arg1, arg2, ...argN) => { 
    expression
}
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
* wenn nur ein Param übergeben wird, kann man `()` wegelassen. ABER bei keiner Übergabe von Param muss man leere `()` schreiben.