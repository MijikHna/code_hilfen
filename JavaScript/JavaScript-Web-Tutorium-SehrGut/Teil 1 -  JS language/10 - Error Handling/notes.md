### 1 - Error Handling "try...catch"
* Syntax:
```try{

}
catch (err){

}
```
* wenn Exception in `setTimeout()` passiert => wird nicht gecatchet, da die eigentliche Funktion nach dem passieren des try-catch-Blocks ausgeführt wird. => um diese zu catchen muss try-catch innerhalb der Funktion sein:
```js
setTimeout(function() {
  try {
    noSuchVariable; // try..catch handles the error!
  } catch {
    alert( "error is caught here!" );
  }
}, 1000);
```
#### Error Object
* bei Exception wird Error Obj mit Details erstellt:
    1. `name`
    2. `message`
    3. `stack`
* `catch {}` wenn man mit Error nihts machen will
+ mit `throw Err_Obj` Erro werfen z.B
    * `let error = new Error(message);`  
    * `let error = new SyntaxError(message);`
    * `let error = new ReferenceError(message);`
    * `let error = new TypeError(message);`

#### Rethrowing
* Bsp
```js
function lala(){
    let json = '{ "age": 30 }'; // incomplete data
    try {

    let user = JSON.parse(json);

    if (!user.name) {
        throw new SyntaxError("Incomplete data: no name");
    }

    blabla(); // unexpected error

    alert( user.name );

    } catch(e) {

        if (e instanceof SyntaxError) {
            alert( "JSON Error: " + e.message );
        } else {
            throw e; // rethrow (*) => wird dann von äußeren Catch verarbeitet
        }
    }
}

try {
    lala();
}
catch(e){
    //..
}
```
* `finally{...}` wird immer ausgeführt, auch wenn in try oder catch `return` gab. (wird eigentlich genau vor return ausgeführt)
* Variablen die in den Scopes von `try`, `catch` oder `finally` definiert sind, sind nur da sicher => besser vor `try` definieren
+ man kann auch `try-finally` verwenden, wenn man mit Error nichts machen will, sondern nur aufräumen will.
#### Global Catch
* wenn Environment (Node.js oder Browser) etwas mit Error machen sollen (catchen), die keinen eigenen try-catch haben:
    1. Node.js: `process.on("uncaughtException")`
    2. Browser: `window.onerror=function(message, url, line, col, error){...}`
    * weiter lesen
### 2 - Custom errors, extending Error
* `throw Obj` kann beliebiges Obj haben (muss nicht unbedingt von Error abstammen)
* Bsp: eigene Exception:
```js
class ValidationError extends Error {
  constructor(message) {
    super(message); // (1)
    this.name = "ValidationError"; // (2) den Namen des Error überschreiben
  }
}

function test() {
  throw new ValidationError("Whoops!");
}

try {
  test();
} catch(err) {
  alert(err.message); 
  alert(err.name); // ValidationError
  alert(err.stack); // a list of nested calls with line numbers for each
}
```
```js
catch (err) {
  if (err instanceof ValidationError) {
    alert("Invalid data: " + err.message);
  } else if (err instanceof SyntaxError) {
    alert("JSON Syntax Error: " + err.message);
  } else {
    throw err;
  }
}
```
* ValidationError (eigene Excepition), Build-In Exception und alle weteiren übergibt weiter.
#### Further inheritance
* Bsp. für Inheritance und Weitergabe von Exceptions