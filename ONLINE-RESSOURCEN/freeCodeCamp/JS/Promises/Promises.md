### Intro
+ Promise = für asynchrone Operationen
* zum besseren Verständnis Artikel über JS Callbacks lesen: https://www.freecodecamp.org/news/javascript-callback-functions-what-are-callbacks-in-js-and-how-to-use-them/
* Promise in JS ähnlich wie im echten Leben: sagt dass es in Zukunft etwas macht. Also wenn man Promise in JS definiert => und dieses Promise wird erfüllt wenn Zeit kommt, oder gar nicht.

### Promises in JS
* ist ein Object, der drei States haben kann:
    1. Pending: Initate State
    2. Resolved: Promise erfüllt
    3. Rejected: Promise failed
* Ablauf:
    1. `Pending`
    2. if `Resolved` wird `then()` ausgeführt
    3. if `Rejected` wird `catch()` aussgeführt 
    4. nach `then()` und `catch()` geht wieder in `Pending`
* Bsp: Wenn man Daten vom Server requested hat. Resolved, wenn man Daten bekommen hat, Rejected, wenn keine Daten erhalten hat
* Wenn es mehrere Requests sind. Nach dem ersten Promise (resolved oder rejected), wird neues Prozess gestartet. 
### Unterschied zwischen Callback und Promise
* es wird Callback and Promise attached. => chaining
* Callback-Funktionen werden für asyncrone Operationen verwendet.
* in manchen Situationen reicht Callback aber nicht aus. z.B wenn mehrere `async` Operationen ausgeführt werden sollen. Wenn man nur Callbacks nutzt => landet man in Situation "Callback hell". Bsp:
```js
firstRequest(function(response) {  
    secondRequest(response, function(nextResponse) {    
        thirdRequest(nextResponse, function(finalResponse) {     
            console.log('Final response: ' + finalResponse);    
        }, failureCallback);  
    }, failureCallback);
}, failureCallback);
```
* das gleiche mit Promises:
```js
firstRequest()
    .then(function(response) {
        return secondRequest(response);
    }).then(function(nextResponse) {  
        return thirdRequest(nextResponse);
    }).then(function(finalResponse) {  
        console.log('Final response: ' + finalResponse);
    }).catch(failureCallback);
```
+ hier werden mehrere CallBack gechained

### Promise erstellen
```js
//const myPromise = new Promise(); //Promise mit Promise Construktor erstellen

const myPromise = new Promise((resolve, reject) => {  
    let condition;  
    
    if(condition is met) {    
        resolve('Promise is resolved successfully.');  
    } else {    
        reject('Promise is rejected');  
    }
}); //Promise braucht zwei Parameter resolve und reject; Wenn condition ist erfüllt => Promise ist resolved, sonst rejected
```
+ wenn Promise ist erfüllt, wird mit dem Promise etwas gemacht: `then()`
* wenn man Promise rejected wird => wird `catch()` ausgeführt.
```js
myPromise.then((message) => {
    console.log(message);
}).catch((message) => {
    console.log(message);
});
```