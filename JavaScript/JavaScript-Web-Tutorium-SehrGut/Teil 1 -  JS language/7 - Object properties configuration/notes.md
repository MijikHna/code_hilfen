### 1 - Properties flogs and descriptions
* Obj-Attr/Eigenschaften habe drei weitere Attribute:
    1. `writable` - wenn true => kann geändert werden
    2. `enumerable` - wenn true => wird in loops gelisted, sonst nicht
    3. `configurable` - wenn true => Attribut kann modifiziert werden
* per Default sind alle true 
* `let descriptor = Object.getOwnPropertyDescriptor(obj, propertyName);` Info über Obj-Eigenscahft bekommen; `proepertyName` = die Eigenschafte
```js
let user = {
  name: "John"
};

let descriptor = Object.getOwnPropertyDescriptor(user, 'name');

console.log(descriptor)
```
* `Object.defineProperty(user, "name", { value: "John"})` - definiet wetiere Obj-Eigenscahft/Attribut wenn es noch nicht existiert, wenn kein Wert angegeben wird, wird auf false gesetzt
#### Non-writable
```js
Object.defineProperty(user, "name", {
  writable: false
});
```
* die Obj-Eigenschaft kann nicht mher geändert werden.
#### Non-enumerble
+ wenn man z.B eigene `toString()` implementiert => wird sie zu `enumerable` => umkonfigurieren
```js
let user = {
  name: "John",
  toString() {
    return this.name;
  }
};

for (let key in user) alert(key); // name, toString

Object.defineProperty(user, "toString", {
  enumerable: false
});
```
#### Non-Configurable
* `configurable:false` - manchmal bei Build-In-Obj so eingestellt. z.b bei Math.PI (non-writable, non-enumerable, non-configurable)
* => man bekommt Error, wenn man versucht `Math.PI` zu ändern z.B `Math.PI=4`
* wenn man ein mal false gesetzt hat => kann nicht mehr zurück auf true setzen.
#### Object.defineProperties
* gleichzeitig mehrere Attribute setzen
```js
Object.defineProperties(user, {
  name: { value: "John", writable: false },
  surname: { value: "Smith", writable: false },
});
```
#### Object.getOwnPropertyDescriptors
* alle Obj-Att-Eigenschaften bekommen `Object.getOwnPropertyDescriptor(obj)`.
* zusammen mit `Object.defineProperties` kann man das zum Clonen verwenden.
* `let clone = Object.defineProperties({}, Object.getOwnPropertyDescriptors(obj));`
#### Weiter Funktio für Obj-Attr-Eigenschaften

### 2 - Property getters + setters
* es gibt zwei Typen von Obj-Eigenschaften
    1. Data 
    2. Accessors eigentlich Funktionen, die get/set ausführen
```js Bsp1
let obj = {
  get propName() {
    //...
  },

  set propName(value) {
    //...
  }
};
```
```js Bsp2
let user = {
  name: "John",
  surname: "Smith",

  get fullName() {
    return `${this.name} ${this.surname}`;
  }
};

console.log(user.fullName);
```
* eigentlich gibt es kein Attr. fullName; von außen sieht aber wie ein Attr. In diesem Beispiel wird `user.fullName="Lala"` nicht funktionieren, da kein `set` definiert ist
#### Accessor Decriptor:
* haben keinen Wert und keine `writable`
* haben:
    1. get
    2. set
    3. enumarable
    4. configurable
```js
let user = {
  name: "John",
  surname: "Smith"
};

Object.defineProperty(user, 'fullName', {
  get() {
    return `${this.name} ${this.surname}`;
  },

  set(value) {
    [this.name, this.surname] = value.split(" ");
  }
});
```
* Attribut kann nur Accessor oder nur Data sein
#### Smarter getter/setter
* als wrapper für echte Attribute. => Attribut bekommt dann `_` vor seinem richtigem Namen:
```js
let user = {
  get name() {
    return this._name;
  },

  set name(value) {
    //...
    this._name = value;
  }
};

user.name = "Pete";
```
* eigentlich `_name` ist auch public (wie in Python)
* weiteres interessantes Bsp: eigentlich age auf birthday ändern, dabei wird aber age als get umgeschrieben um den ganzen Code nicht umzuschreiben
```js
function User(name, birthday) {
  this.name = name;
  this.birthday = birthday;

  // age is calculated from the current date and birthday
  Object.defineProperty(this, "age", {
    get() {
      let todayYear = new Date().getFullYear();
      return todayYear - this.birthday.getFullYear();
    }
  });
}

let john = new User("John", new Date(1992, 6, 1));
```