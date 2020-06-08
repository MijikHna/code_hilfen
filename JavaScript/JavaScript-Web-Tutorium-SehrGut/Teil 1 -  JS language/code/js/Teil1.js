/* 2 - JavaScript Fundamentals */
//4 -  Variablen
variablen = (john) => {
    let admin;
    let name;
    if (john !== undefined) {
        admin = john;
    } else {
        admin = 'John';
    }
    name = admin;
    alert("Name: " + name);
}

// 5 - Data types
dataTypesEmbeddedExpressionInString = () => {
    let name = "John";

    // embed a variable
    alert(`Hello, ${name}!`); // Hello, John!

    // embed an expression
    alert(`the result is ${1 + 2}`); // the result is 3
}

dataTypesTypeOf = () => {
    console.log(typeof undefined); // "undefined"
    console.log(typeof 0); // "number"
    console.log(typeof 10n); // "bigint"
    console.log(typeof true); // "boolean"
    console.log(typeof "foo"); // "string"
    console.log(typeof Symbol("id")); // "symbol"
    console.log(typeof Math); // "object"  (1)
    console.log(typeof null); // "object"  (2)
    console.log(typeof alert); // "function"  (3)
}
// 10 - Conditional Operators
conditionalOperatorsTask2 = () => {
    result = prompt("What is the \"official \" name of JavaScript");
    if (result === "ECMAScript") {
        console.log("Antwort GUT");
    } else {
        console.log("Antowort Schlecht");
    }
}

// 15 - Funktion Expressions
// Function Declarations
function funcSum1(a, b) {
    console.log("funcSum1: " + (a + b));
}

let funcSum2 = function (a, b) {
    console.log("funcSum2: " + (a + b));
}

let funcSum1Kopie = funcSum1;
let funcSum2Kopie = funcSum2;

/* 3 - Code Quality */
// 1 - Chrome Debugger
function testDebugger() {
    console.log("vor debugger-command");
    debugger;
    console.log("vor debugger-command");

}

/* 4 - Objects: the basics */
// 5 - Object to primitive conversion
let functionConvertToPrimitives = () => {
    let user = {
        name: 'kirill',
        age: 30
    };

    let user1 = user;
    let user2 = user;

    console.log(user1 + user2);
    console.log(5 + user1);
    console.log(user1 - user2);
    console.log(5 - user1);
}

// 6 - Constructor, operator "new"
function functionConstructor() {
    function User(name = "Musterman") {
        this.name = name;
        this.isAdmin = false;

        this.toString = function () {
            // return "Name: " + this.name + "isAdmin: " + this.isAdmin;
            return `Name: "${this.name}" isAdmin: ${this.isAdmin}`;
        };
    }

    let user = new User('Kirill');
    /* user.toString() {
        return `Name: "${this.name}" isAdmin: + ${this.isAdmin}`;
    } */
    console.log(user);
    console.log(user.toString());
}