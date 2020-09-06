#### 1 - Variablen Gültigkeit
* man sollte `let` benutzen z.B
```js
for (let i = 0; i < arr.length; i++) {}

//besser, da Zugrif auf length von Array nur ein Mal
let length = arr.length;
for (let i = 0; i < length; i++) {}
```
#### 2 - For-Varianten
* schnellste Ausführung ist mit `for`
* weitere For-Versionen
    1. `for...of`
    2. `forEach`
    3. `while`
    4. `map` und `filter`

#### 3 - DOM-Element Aufrufe verringern
* jedes man wenn man auf DOM-Element mit `querySelector` zugreift, muss on JS ein Object aufgebaut werden
```js
// Funktion - setText(element, textContent): Promise -> return Promise darüber,dass Text gesettet wurde
const setText = (element, textContent) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      element.textContent = textContent;
      resolve();
    }, 3000)
  })
}

// Funktion async, die setText drei Mal aufruft, dabei wird DOM-Element nur einmal in foo gespeichert
(async () => {
  const foo = document.querySelector('#foo');
  await setText(foo, 'foo');
  await setText(foo, 'bar');
  await setText(foo, 'baz');
})();
```

#### 4 - keine Variablen verwenden, die eigentlich nicht gebraucht werden
* Bsp:
```html
<div id='foo'>
  <p>

  </p>
</div>
```
* 
```js
// BAD EXAMPLE
const foo = document.querySelector('#foo');
const p = foo.querySelector('p');
p.textContent = 'foo';

// GOOD EXAMPLE
document.querySelector('#foo p').textContent = 'foo';
```
#### 5 - JS am Ende laden
3 Optionen:
1. am ende von `<body>`
2. mit `defer`-Attr von `<script>`
3. oder einen Script laden der dann weitere Scripte ladet:
```js
window.onload = () => {
  const element = document.createElement("script");
  element.src = "https://code.jquery.com/jquery-1.12.4.min.js";
  document.body.appendChild(element);
};
```
