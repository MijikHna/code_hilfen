### TS 3.5 - Features
#### Compile Geschwindigkeit
1. mit `--incremental` kann man weitere Compilirungen beschleunigen, da gecachet wird

#### Hilfsttyp Omit
* mit Typ `Omit` kann man neue Typen definieren, indem man Eigenschaften rausnimmt
```ts
type Person = {
    name: string;
    age: number;
    address: string;
};

type NewPerson = Omit<Person "address">
// ==
type NewPerson = {
    name: string;
    age: number;
}
```
#### Verbesserung bei zusammengesetzten Typen
* früher konnte man im zusammengesetzten Typ den Typ des Attribute im Vergleich zu Original-Typ ändern
```ts
type Person = {
    name: string;
    age: number;    
};

type Address = {
    address: string;
}

const person: Person | Address = {
    name: 'Joe',
    age: 1,
    address: true // JETZT ERROR
};
```
#### Flag - allowUmdGlobalAccess
* mit `--allowUmdGlobalAccess` kann man jetzt auf globale UMD-s referencieren

#### Clevere Überprüfung des Typs mit Zusammensetzung
```ts
type Foo = { done: boolean, value: string }
type Bar =
    | { done: false, value: string }
    | { done: true, value: string };

declare let source: Foo;
declare let target: Bar;

target = source;
```
* früher `done` wäre literaler Typ, jetzt ist es boolean Typ

#### Typ herausfiltern aus ComposeConstructor:
```ts
// ComposeConstructor
function composeConstructors<T, U, V>(
    F: new (x: T) => U, G: new (y: U) => V): (x: T) => V {    
    return x => new G(new F(x))
}

// Klassen für den 
class Foo<T> {    
    value: T;
    constructor(value: T) {
        this.value = value;
    }
}

class Bar<U> {    
    value: U;
    constructor(value: U) {
        this.value = value;
    }
}

let f = composeConstructors(Foo, Bar);
let a = f('foo');
```
* früher hätte für `Bar<Foo<string>>` `Bar<{}>` ausgegeben