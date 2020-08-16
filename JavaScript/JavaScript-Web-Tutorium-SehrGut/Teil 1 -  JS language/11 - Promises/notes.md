# Promises, async/await

## 1 - Introduction: callbacks

* Funktion, die etwas asynchron machen muss muss eine Callback-Funktion haben.
* Bsp: mit JS JS-Script laden und wenn dieser Script ist geladen die Funktionen aus diesem Script ausführen `script.onload=callback(script)`

### Callback in Callback

* z.B wenn man in Callback weiteren Script lädt

### Handling Errors

* wenn Callback Error ergibt => für Browser z.B `script.onerror = () => callback(new Error("Script Load error"))` + `loadScript('scirpt.js', function(error, script))` (<- Error-Frist Callback)
* Das ganze wird Problematisch, wenn man mehrere Nested Callbacks hat 

## 2 - Promise

* Konstruktor-Syntax für Promise `let promise = new Promise(function(resolve, reject) {executor()});`
* `executor()` = Code der etwas macht = ein Ergebnis produziert. Wenn executor ein Ergenis liefert wird resolve() oder reject() ausgeführt
* Promise States:
    1. pending
    2. resolved => aufgerufen: `resolve(ergebnis)`
    3. reject => aufgerufen => `reject(error)`
* also executro() bekommt zwei Callback-Funkt (sind schon von JS-Engine vordefiniert)
* Aufrufe von resolve() bzw. reject() switched auch den State von Promise zum entsprechenden Zustand.
  * also bei Fehler im executor() wird reject() aufgerufen

### Consumers: then, catch, finally

* ~ Verbindung zwishcen executor() und consuming Funktion, die entweder das Ergebnis oder Error bekommt.
* Man kann Consumer-Funktion registrieren/subscriben mit:
  1. then() -> Syntax

  ```js
  promise.then(
      function(result){...}
      function(error){...}
  )
  ```

  * Bsp:

  ```js
  let promise = new Promise(function(resolve, reject)  {
  setTimeout(() => resolve("done!"), 1000);
  });  
  promise.then(
  result => alert(result), 
  error => alert(error) 
  );
  ```

  2. `catch()` - wenn man sich nur für Error interessiert: (use null as the first argument: `.then(null, errorHandlingFunction)`. Or we can use `.catch(errorHandlingFunction)`, which is exactly the same:)
  3. `finally()`: wird bei beiden resolved und rejected ausgeführt
    * Also wenn Promise ist pedning, .then()/catch()/finally()-"Handler" warten auf das Ende des Promises

### Bsp:

* siehe <https://javascript.info/promise-basics#loadscript>

## 3 - Promise chaining

* Problem: mehrere Sequencen, die nach einander ausgeführt werden sollen
* Bsp: hier wird jedes `result` an weiteres `then` weitergegeben. `promise.then` returt wieder einen Promise

```js
new Promise(function(resolve, reject) {

  setTimeout(() => resolve(1), 1000); // (*)

}).then(function(result) { // (**)

  alert(result); // 1
  return result * 2;

}).then(function(result) { // (***)

  alert(result); // 2
  return result * 2;

}).then(function(result) {

  alert(result); // 4
  return result * 2;

});
```

### Return promises

* Handler, der in `then(handler)` benutzt wird,kann auch Promise erstellen und returnen

```js
new Promise(function(resolve, reject) {

  setTimeout(() => resolve(1), 1000);

}).then(function(result) {

  alert(result); // 1

  return new Promise((resolve, reject) => { // (*)
    setTimeout(() => resolve(result * 2), 1000);
  });

}).then(function(result) { // (**)

  alert(result); // 2

  return new Promise((resolve, reject) => {
    setTimeout(() => resolve(result * 2), 1000);
  });

}).then(function(result) {

  alert(result); // 4

});
```

### Bsp: Scripts nacheinander laden

```js
loadScript("/article/promise-chaining/one.js")
  .then(function(script) {
    return loadScript("/article/promise-chaining/two.js");
  })
  .then(function(script) {
    return loadScript("/article/promise-chaining/three.js");
  })
  .then(function(script) {
    one();
    two();
    three();
  });

//verkürzte Variante
loadScript("/article/promise-chaining/one.js")
  .then(script => loadScript("/article/promise-chaining/two.js"))
  .then(script => loadScript("/article/promise-chaining/three.js"))
  .then(script => {
    // scripts are loaded, we can use functions declared there
    one();
    two();
    three();
  });

// schlecht da kein Chaining und wird unlesbar
loadScript("/article/promise-chaining/one.js").then(script1 => {
  loadScript("/article/promise-chaining/two.js").then(script2 => {
    loadScript("/article/promise-chaining/three.js").then(script3 => {
      // this function has access to variables script1, script2 and script3
      one();
      two();
      three();
    });
  });
});
```

* eigentlich wird kein Promise sondern `Thenable`-Obj returnt, der auch `then()` implementiert

### Bsp: mit fetch()

* oft werden Promises in Frontend benutzt, um Daten bei Server anzufragen.

```js
fetch('/article/promise-chaining/user.json') //fetch() liefert Daten dien dem Callback übergeben werden
  .then(function(response) {
    return response.json();
  })
  .then(function(user) {
    alert(user);
  });

// oder
// same as above, but response.json() parses the remote content as JSON
fetch('/article/promise-chaining/user.json')
  .then(response => response.json())
  .then(user => alert(user.name)); // iliakan, got user name

// Bsp: Datena aus Github holen
fetch('/article/promise-chaining/user.json')
  .then(response => response.json())
  .then(user => fetch(`https://api.github.com/users/${user.name}`))
  .then(response => response.json())
  .then(githubUser => {
    let img = document.createElement('img');
    img.src = githubUser.avatar_url;
    img.className = "promise-avatar-example";
    document.body.append(img);

    setTimeout(() => img.remove(), 3000); // (*)
  });

// erweiterte Bsp nach (*)
fetch('/article/promise-chaining/user.json')
  .then(response => response.json())
  .then(user => fetch(`https://api.github.com/users/${user.name}`))
  .then(response => response.json())
  .then(githubUser => new Promise(function(resolve, reject) { // (*)
    let img = document.createElement('img');
    img.src = githubUser.avatar_url;
    img.className = "promise-avatar-example";
    document.body.append(img);

    setTimeout(() => {
      img.remove();
      resolve(githubUser); // (**) -> hier wird Promise resolved und nur nach diesem Call wird nächstes then() aufgerufen
    }, 3000);
  }))
  // triggers after 3 seconds
  .then(githubUser => alert(`Finished showing ${githubUser.name}`));
```

* Good Practise: async Aktion sollte immer Promise returnen
* zum Schluss wird der Code in reusable Funktionen unterteilt

```js
function loadJson(url) {
  return fetch(url)
    .then(response => response.json());
}

function loadGithubUser(name) {
  return fetch(`https://api.github.com/users/${name}`)
    .then(response => response.json());
}

function showAvatar(githubUser) {
  return new Promise(function(resolve, reject) {
    let img = document.createElement('img');
    img.src = githubUser.avatar_url;
    img.className = "promise-avatar-example";
    document.body.append(img);

    setTimeout(() => {
      img.remove();
      resolve(githubUser);
    }, 3000);
  });
}

loadJson('/article/promise-chaining/user.json')
  .then(user => loadGithubUser(user.name))
  .then(showAvatar)
  .then(githubUser => alert(`Finished showing ${githubUser.name}`));
  // ...

```

## 4 - Error Handling with Promises

* Promise Chains sind auch gut für Error-Handling
  1. wenn Promise wird rejected, es wird zum Reject-Handler (`catch()`) gesprungen
  2. da `catch()` nach allen `then()`-s steht kann er Errors bei Chaining abfagen

    ```js
    fetch('https://no-such-server.blabla') // rejects, da falche URL
        .then(response => response.json())
        .catch(err => alert(err))
  
    // zu 2.

    fetch('/article/promise-chaining/user.json')
    .then(response => response.json())
    .then(user => fetch(`https://api.github.com/users/${user.name}`))
    .then(response => response.json())
    .then(githubUser => new Promise((resolve, reject) => {
        let img = document.createElement('img');
        img.src = githubUser.avatar_url;
        img.className = "promise-avatar-example";
        document.body.append(img);

        setTimeout(() => {
        img.remove();
        resolve(githubUser);
        }, 3000);
    }))
    .catch(error => alert(error.message));
    ```

### Implicit try...catch

* Code des Promise-Executors und Promise-Handlers hat wird in unsichtbarem `try-catch()` ausgeführt z.B

```js
new Promise((resolve, reject) => {
  throw new Error("Whoops!");
}).catch(alert);

// funktioniert genauso wie:
new Promise((resolve, reject) => {
  reject(new Error("Whoops!"));
}).catch(alert);
```

* Executor = was innerhalb von `new Promise((resolve, reject) => {//Executor})` ist
* Handler = was innerhalb von `then((resutl) => {/Handler})` ist
* auch wenn Handler Error wirft wird er von `catch()` abgefangen

```js
new Promise((resolve, reject) => {
  resolve("ok");
}).then((result) => {
  throw new Error("Whoops!"); // rejects the promise
}).catch(alert); 
```

### Rethrowing

* in `catch()` oder in `then()` kann man die Errors rethrowen

```js
// the execution: catch -> then, da catch-Block normal bzw. bis zum Ende ausgeführt wird, wird dann then ausgeführt
new Promise((resolve, reject) => {

  throw new Error("Whoops!");

}).catch(function(error) {

  alert("The error is handled, continue normally");

}).then(() => alert("Next successful handler runs"));


// the execution: catch -> catch
new Promise((resolve, reject) => {

  throw new Error("Whoops!");

}).catch(function(error) { // (*)

  if (error instanceof URIError) {
    // handle it
  } else {
    alert("Can't handle such error");

    throw error; // throwing this or another error jumps to the next catch
  }

}).then(function() {
    /* doesn't run here */
    }).catch(error => { // (**)

  alert(`The unknown error has occurred: ${error}`);

});
```

### Unhandled Rejections

* passiert eigentlich das gleiche was bei einer Exception passierten würde, wenn man für Promise keinen catch-Block macht

## 5 - Promise API

* es gibt 5 statische Methoden bei `Promise`

### `Promise.all`

* Syntax: `let promise = Promise.all([...promises...]);` - bekommt einen Array oder Iterable von Promises und returnt neuen Promise, der aufgelöst wird wenn alle inneren Promises aufgelöst wurden, wobei die returns der einzelnen Promises in einen Array gepackt werden, dabei der Index des return Array hängt von dem Index im übergegebenen Promise-Array
  * Wenn einer der Promises rejected wird => werden alle rejected
  * die inneren Promises werden zwar weiter ausgeführt deren returns werden aber ignoriert

```js
Promise.all([
  new Promise(resolve => setTimeout(() => resolve(1), 3000)), // 1
  new Promise(resolve => setTimeout(() => resolve(2), 2000)), // 2
  new Promise(resolve => setTimeout(() => resolve(3), 1000))  // 3
]).then(alert); // [1,2,3]

//Bsp:
let urls = [
  'https://api.github.com/users/lala1',
  'https://api.github.com/users/lala2',
  'https://api.github.com/users/lala3'
];

// map every url to the promise of the fetch
let requests = urls.map(url => fetch(url));

// Promise.all waits until all jobs are resolved
Promise.all(requests)
  .then(responses => responses.forEach(
    response => alert(`${response.url}: ${response.status}`)
  ));

// man kann auch keinen Promise in den Promise-Array mit angegeben
Promise.all([
  new Promise((resolve, reject) => {
    setTimeout(() => resolve(1), 1000)
  }),
  2,
  3
]).then(alert); // 1, 2, 3
```

### `Promise.allSettled`

* wartet bis alle Promises ausgeführt werden egal ob resolved oder rejected werden, returntes Array hat dann folgendes Muster
    1. `{status:"fulfilled", value:result}`
    2. `{status:"rejected", reason:error}`
  * wenn manche Browser kein Promise.allSettled unterstützen muss man es polyfillen

```js
Promise.allSettled(urls.map(url => fetch(url)))
  .then(results => { // (*)
    results.forEach((result, num) => {
      if (result.status == "fulfilled") {
        alert(`${urls[num]}: ${result.value.status}`);
      }
      if (result.status == "rejected") {
        alert(`${urls[num]}: ${result.reason}`);
      }
    });
  });
```

### `Promise.race`

* wartet bis erste Promise gelöst wird und returnt diesen

```js
Promise.race([
  new Promise((resolve, reject) => setTimeout(() => resolve(1), 1000)),
  new Promise((resolve, reject) => setTimeout(() => reject(new Error("Whoops!")), 2000)),
  new Promise((resolve, reject) => setTimeout(() => resolve(3), 3000))
]).then(alert);
```

### Promise.resolve/reject

#### `Promise.resolve`

* Eigentlich: `let promise = new Promise(resolve => resolve(value));`
* kaum benutzt, das schon in `async/await` realisiert.

```js

let cache = new Map();

function loadCached(url) {
  if (cache.has(url)) {
    return Promise.resolve(cache.get(url)); // (*)
  }

  return fetch(url)
    .then(response => response.text())
    .then(text => {
      cache.set(url,text);
      return text;
    });
}
```

### `Promise.reject`

* Eigentlich: `let promise = new Promise((resolve,reject) => reject(value));`

## 6 - Promisification

* eigentlich Transormation: Funktion die Callback erwartet in Funktion, die Promise returnt
* oft benötigt, da of Lib-Funktionen Callback-Funktionen sind.

```js
function loadScript(src, callback) {
  let script = document.createElement('script');
  script.src = src;

  script.onload = () => callback(null, script);
  script.onerror = () => callback(new Error(`Script load error for ${src}`));

  document.head.append(script);
}

// Promisification von der obigen Funktion:
let loadScriptPromise = function(src) {
  return new Promise((resolve, reject) => {
    loadScript(src, (err, script) => {
      if (err) reject(err)
      else resolve(script);
    });
  })
}
```

* in der Praxis muss man oft viele Funktionen promisifizieren => kann man Wrapper-Funkt dafür erstellen z.B sowas:

```js 
function promisify(f, manyArgs = false) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      function callback(err, ...results) { // our custom callback for f
        if (err) {
          reject(err);
        } else {
          // resolve with all callback results if manyArgs is specified
          resolve(manyArgs ? results : results[0]);
        }
      }

      args.push(callback);

      f.call(this, ...args);
    });
  };
};

// usage:
f = promisify(f, true);
f(...).then(arrayOfResults => ..., err => ...)
```

* weiter Info dazu: https://github.com/digitaldesignlabs/es6-promisify

## 7 - Microtasks

* PromiseJobs müssen erst eingerichtet werden => werden oft eigentlich nach dem normalen Code ausgeführt.
* wenn man Promise aufruft werden sie aufgerufen und den Rest mach Node.JS-Umgebung.
* alle PromiseJobs werden erst gequeued
* wenn man unbedingt will das der Code nach dem Promise ausgeführt wird => diesen in `then()` packen

```js
//alert() wird zuerst ausgeführt
let promise = Promise.resolve();
promise.then(() => alert("promise done!"));
alert("code finished");

// alert() nach Promise ausführen
Promise.resolve()
  .then(() => alert("promise done!"))
  .then(() => alert("code finished"));
```

### Unhandled rejectoin (nicht so ganz verstanden)

## 8 -Async/await

* angeheme Syntax um mit Promises zu arbeiten
* `async` => Funktion wird Promise returnen => man kann dann kann man `then()` anwenden

```js
async function f() {
  return 1;
}

f().then(alert);
```

* `await` arbeitet innerhalb von `async`
* `await` => macht, dass JS wartet, bis Promise aufgelöst wird

```js
async function f() {

  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("done!"), 1000)
  });

  let result = await promise; // wait until the promise resolves (*)

  alert(result); // "done!"
}

f();
```

* bessere Schreibweise für `promise.then()` => `.then()` mit `await` ersetzen
* muss auch kein Promise sein sondert Thenable. Also:

```js
class Thenable {
  constructor(num) {
    this.num = num;
  }
  then(resolve, reject) {
    alert(resolve);
    // resolve with this.num*2 after 1000ms
    setTimeout(() => resolve(this.num * 2), 1000); // (*)
  }
};

async function f() {
  // waits for 1 second, then result becomes 2
  let result = await new Thenable(1);
  alert(result);
}

f();
```

* also `then()` ruft `resolve` oder `reject` aufgerufen und `await` wartet bis `then()` beendet wird.

### Async class methods

```js
class Waiter {
  async wait() {
    return await Promise.resolve(1);
  }
}

new Waiter()
  .wait()
  .then(alert); // 1
```

### Error handling

* wenn Promise rejected => gleich als ob `throw` geworfen wird.

```js
async function f() {
  await Promise.reject(new Error("Whoops!"));
}

// ==
async function f() {
  throw new Error("Whoops!");
}

// man kann dann diese Exception in try-catch abfangen
async function f() {

  try {
    let response = await fetch('http://no-such-url');
  } catch(err) {
    alert(err); // TypeError: failed to fetch
  }
}

f();

```

* wenn man async/await benutzt => wird man selten `then()`, da `await` es schon behadelt. Statt `.catch()` `try..catch` benutzen.

* wenn man beim außen kein `async` benutzt => kann man auch kein `await` benutzen => muss man `.then/.catch` benutzen