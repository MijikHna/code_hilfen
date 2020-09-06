Dieses Tutorial ist Teil von 4-std JS Bootcamp https://jsbootcamp.io/course

### Bsp:
+ Clone einer Bloggin Site. Man möchte, dass jeder User verschiedene Posts liken kann.
1. wenn User auf Like-Button clickt, wird es inkremented
```js
// global scope
let likeCount = 0;

function handleLikePost() {
  // function scope
  likeCount = likeCount + 1;
}

handleLikePost();
console.log("like count:", likeCount); // like count: 1
```
* Problem dabei, dass likeCount eine globale Var ist, und kann versehentlich überall im Code geändert werden. Lösung:
```js
function handleLikePost() {
  let likeCount = 0;
  likeCount += 1;
  console.log("like count:", likeCount);
}

handleLikePost(); // like count: 1
console.log("like count:", likeCount); 
```
* Problem: likeCount wird jedes Mal auf 0 gesetzt. Hier kommt Closure ins Spiel (schrittweise Aufbau):
1. Funktion in anderer Funktion definieren
```js
function handleLikePost() {
  let likeCount = 0;
  likeCount += 1;
  function() {

  }
}

handleLikePost();
```
2. `likeCount` inkrement in diese Funktion verscieben + Namen der Funktion (hier wird den Namen vergeben zur besseren Übersicht, meistens bleibt es anonyme Funktion)
```js
function handleLikePost() {
  let likeCount = 0;
  function addLike() {
    likeCount += 1;
  }
}
```
* hier wird `likeCount` immer noch bem Betreten zerstört, wenn man `handleLikePost()` aufruft.
3. `likeCount` returnen in der nested Funkt. `addLike()`
```js
function handleLikePost() {
  let likeCount = 0;
  return function addLike() {
    likeCount += 1;
    return likeCount;
  };
  // addLike();
}

handleLikePost();
```
* ??? Unsurprisingly, we get the `addLike` function logged. Why? Because we're returning it, after all.
4. `handleLike()` einer Variablen zuweisen
```js
function handleLikePost() {
  let likeCount = 0;
  return function addLike() {
    likeCount += 1;
    return likeCount;
  };
}

const like = handleLikePost();

console.log(like()); // 1
console.log(like()); // 2
console.log(like()); // 3
```
### Wie funktioniert es
1. `handleLikePost()` wird ausgeführt. Dabei erstellt sie die Instance der inneren Funk. `addlike()`. Diese Funktion schließt `likeCount` ein, da im gleichen Scope
2. Man hat die Funktion `addLike` outside des Scopes aufgerufen, in dem es definiert wurde, indem die innere Funkt `addLike()` returned wurde aus der äußeren Funkt `handleLikePost()` und die Reference auf diese Funktion wurde dann in Var. `like` gespeichert.
3. Man würde erwarten, dass wenn `like()` ausgeführt wurde, würde GC alles deleten nach der Ausführung.
4. wegen **Closure**. Da es noch einen Verweis der inneren Funkt `addLike() in Var. `like()` gibt, ist auch countLike in diesen Scope eingeschlossen (Closure) 

* Also Closures halten die lokalen Var am Leben.
* Closures sind keine Snapshots

### Bsp 2 - User erlauben mehrere Likes für ein Post zu geben
1. Param, der angibt, wie viel Likes
```js
function handleLikePost(step) {
  let likeCount = 0;
  return function addLike() {
    likeCount += step;
    // likeCount += 1;
    return likeCount;
  };
}

const like = handleLikePost(1);
const doubleLike = handleLikePost(2);

like(); // 1
like(); // 2

doubleLike(); // 2 (the count is still being preserved!)
doubleLike(); // 4
```
+ da `like` and `doubleLike` zwei verschiedene Scopes aufmachen. Also keine Snapshots
+ Also Closure hält lokale Variablen am Leben aus Funkt., die eigentlich zerstört wurden.

### zwei Kriterien, wann etwas Closure sein sollte
1. Eigenschaft von JS-Funkt. (nur Funkt.)
2. Feststellen, ob Closure ist => Funktion in anderem Scope ausführen, in dem es definiert wurde.
* man sollte sich mit Closure auskenne, da sie erlauben Werte zu "merken". 
