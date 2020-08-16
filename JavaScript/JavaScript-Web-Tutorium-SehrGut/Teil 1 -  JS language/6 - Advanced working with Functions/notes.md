# 1 - Advanced working with functions

## 1 - Recursion and stack

### Recursion traversals

* Bsp: Gehälter der Abteilung mit Unterabteilungen berechnen

```js
let company = { // the same object, compressed for brevity
    sales: [
        {name: 'John', salary: 1000},
        {name: 'Alice', salary: 1600}
    ],
    development: {
        sites: [
            {name: 'Peter', salary: 2000},
            {name: 'Alex', salary: 1800 }
        ],
        internals: [
            {name: 'Jack', salary: 1300}
        ]
    }
};

// The function to do the job
function sumSalaries(department) {
    if (Array.isArray(department)) { // case (1)
        return department.reduce((prev, current) => prev + current.salary, 0); // sum the array
    }
    else { // case (2)
        let sum = 0;
        for (let subdep of Object.values(department)) {
            sum += sumSalaries(subdep); // recursively call for subdepartments, sum the results
    }
    return sum;
  }
}

alert(sumSalaries(company)); // 7700
```

### Linked List

```js
let list = {
  value: 1,
  next: {
    value: 2,
    next: {
      value: 3,
      next: {
        value: 4,
        next: null
      }
    }
  }
};

// ==

let list = { value: 1 };
list.next = { value: 2 };
list.next.next = { value: 3 };
list.next.next.next = { value: 4 };
list.next.next.next.next = null;
```

## 2 - Rest parameters and spread syntax

### Rest Param

```js
function sum(a, b) {
  return a + b;
}

alert( sum(1, 2, 3, 4, 5) );
```

* Funktion kann mit mehreren Params aufgerufen werden ohne Error (excessive Arguments)
* `function funktName(...arrayName)` - werden alle Params in Array `arrayName` abgelegt.
* `function f(arg1, ...rest, arg2)` - Error, da `arg2` wird undefined, da alle restlichen Params in `rest` abgelegt werden.

### `arguments`

* ist spezielles Array, der alle übergebenen Params enthält, war früher anstelle von `...rest` benutzt. Ist nicht Iterable. Bei Arrow-Funktions enthält es Params der außeren Funkt, da ja deren Kontext genommen wird

### Spread Syntax

* Array bei param Übergabe auspacken. Usefull, wenn Funktion einzelne Werte erwartet
* damit kann man auch Arrays mergen: `let merged = [0, ...arr, 2, ...arr2];`
* Obj. muss aber Iterable sein

```js
let arr1 = [1, -2, 3, 4];
let arr2 = [8, 3, -8, 1];

alert( Math.max(...arr1, ...arr2) );
```

* damit kann man auch Arrays kopieren: `let arrCopy = [...arr];`
* damit kann auch Obj. kopieren:

```js
let obj = { a: 1, b: 2, c: 3 };
let objCopy = { ...obj };
```

## 3 - Variable scope, closure

## 4 - The old var

## 5 - Global object

## 6 - Function object, NFE

## 7 - The "new Function" syntax

## 8 - Scheduling: setTimeout and setInterval

## 9 - Decorators and forwarding, call/apply

## 10 - Function binding

## 11 - Arrow functions revisited