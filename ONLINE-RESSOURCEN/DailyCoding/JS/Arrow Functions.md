#### Wann sind Arrow Functions gut
1. z.B bei `map()` von Arrays
```js
const words = ['hello', 'WORLD', 'Whatever'];
const downcasedWords = words.map(word => word.toLowerCase());
```
2. bei `forEach()` von Arrays
```js
this.examples.forEach(example => {
  this.runExample(example);
});
```
3. z.B bei `then()` bei Promise-s
```js
this.doSomethingAsync().then((result) => {
  this.storeResult(result);
});
```
#### Wann sind Arrow Functions schlecht
1. als Methode der Klasse
2. wenn viele Arrow Function verkettet werden
3. bei Funktionen, die `this` dynamisch binden sollen