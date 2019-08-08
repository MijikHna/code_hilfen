### 1 - Programming Basics:
#### 1- What is programming:
1. Programm ist Satz von Instruktionen
2. Statements in Programmiersprache = Instruktion
#### 2 - What is a programming language:
1. Drei Sachen verstehen beim Schreiben des SourceCodes:
    1. wo schreibt man diesen 
    2. Wie wird dieser in Maschinencode umgewandelt
    3. Wie wird dieser ausgeführt 
2. ← diese Drei sind Sprachabhängig
#### 3 - Writing surce code:
1. Source Code = plain text = keine Formatierung, kein rich text = formtatierter Text
2. Interpreter vs. Compiler vs. Intermediate
3. Java, C#, VB.Net, Python = Hybrid (Intermediate)

### 2 - Core Programming Syntax:
#### 1 - Why JavaScript
1. Java und JavaScript sind nicht verwandt
2. JavaScript läuft nur unter WebServer bzw. was Java-Interpreter hat
3. JS ist CaseSensitiv

#### X - Bsp zum Kapitel:
```html
<html>
	<head>
		<title>Simple Page</title>
	</head>
	<body>
		<p>This is a very simple HTML page</p>
        <script src="core_programming_syntax.js"></script>
	</body>
</html>
```
```javascript
//2 - Creating your first program in JavaScript
alert("Hello world");

//3 - Requesting input
var name = prompt("What is your name?"); //prompt speichert Eingabe in name + pausiert bis OK geklickt wird
alert("Hello, " + name);
```

### 3 - Variables and Data Types:
1. Introduction to variables and data types:
2. Understanding strong, weak and duck-typed languages
    1. JS ist weak typed Sparache
#### X - Beispiele:
```html
<html>
	<head>
		<title>Simple Page</title>
	</head>
	<body>
		<p>This is a very simple HTML page</p>
		<script src="variable_and_data_types.js"></script>
	</body>
</html>
```
```javascript
//Variablen namen sind _ und $ erlaubt
//1 - Introduction to variables and data types
var  year = 2019
year2 = 2019 // wird schauen, ob es schon diesen Variablennamen gibt, wenn nicht => wird erstellt

//3 - Working with numbers
var a;
a=5;
a=1000;
a=-500;
a=123.654;
alert(a)

var b=134;
var c="1234";

//4 - Using characters ans strings
var phase="This is a simple Quotes"
alert(phase.length);

//Working with operators
a=a+1;
a+=1;
a++;

//5 - Properly using white space
a ++;
var name = prompt("Waht is \nyour name?")
var message = "Hello";
alert(message + " " + name);

//6 - Adding comments to code for human understanding

//Kmmentare besser vor der Codezeile statt nach der Kommentarzeile

//numeric variables
var a = 5;
var b = 10;
var c = 20;

//bollean variables
var x = true;
var y = false;

//string variables
var name=prompt("What is your name?");
var message="Hello";

/*
mehrzeilige Kommentarzeile
*/

```

### 4 - Writing Conditional Code:
#### X - Beispiele
```html
<html>
	<head>
		<title>Simple Page</title>
	</head>
	<body>
		<p>This is a very simple HTML page</p>
		<script src="writing_conditional_code.js"></script>
	</body>
</html>
```
```javascript
//1- Building with the if statement
a = 10;
b = 5;

if( a > 10 ){
    alert("it's true 1");
}

if (a === 10){
    alert("it's true 2")
}

if (a < b ){
    alert("Yes, a is less then b");
}

if( a === b ){
    alert("Yes, a is equal to b");
}

//2 - Working with complex conditions
var balance=5000;

if ( balance >= 0 ){
    alert("The balance is positive");
    if( balance > 10000){
        alert("The balance is large!")
    }
}
else{
    alert("The balance is negative");
}
// 3 - Setting comparison operators

// === -> strict equality
var a = 123;
var b = "123";
 
if ( a == b ){
    alert("Yes, they ARE equal ==");
}

if( a === b ){
    alert("Yes, they ARE equal ===");    
}

//logical and/or
var c = 10;
var d = 10;
b=123;
if ( (a === b) && (c === d) ){
    alert("a equals b and c equal c");
}

//Using the switch statement:

//switches haben Fall through
var grade = "Premium";

switch( grade ){
    case "Regular":
        alert("It's $3,15");
        break;
    case "Premium":
        alert("It's $4,15");
        break;
    case "Diesel":
        alert("It's $5,15");
        break;
    default:
        alert("That's is not a valid grade");
}
```

### 5 - Modular Code:
#### X - Bspiele
```html
<html>
	<head>
		<title>Simple Page</title>
	</head>
	<body>
		<p>This is a very simple HTML page</p>
		<script src="modulare_code.js"></script>
	</body>
</html>
```
```javascript
// 1 - Breaking your code apart
function myFunction1 (){
    alert("This code is inside the function");
}

myFunction1();

//Funktionen können überall geschreiben werden
//<- alle Funktionen ganz oben definieren = good Practice
//JS-Interpreter scan erst die ganze JS-Datei

//2 - Creating and calling function

function myFunction2 (){
    var a = 10;
    var b= 20;
    var c = 30;
    var d = a + b + c;
    alert("The value of d is :" + d);
}

myFunction2();

//3 - Setting parameters and arguments:
function addTwoNumbers(a,b){
    var result = a + b;
    //alert(result);
    return result;
}

var x = addTwoNumbers(5, 10);
alert( addTwoNumbers(5,10) );

//4 - Understanding variable scope
function simpleFunction(){
    var x1 = 500;
    alert(x1);
}

simpleFunction();
alert(x1);

//5 - Splitting code into different files

```
### 6 - Iteration: Writing Loops:

### 7 - More About Strings:
 
### 8 - Collections:

### 9 - Programming Style:

### 10 - Input and Output:

### 11 - When Things Go Wrong:

### 12 - Introduction to Object Orientation:

### 13 - Advanced Topics:

### 14 - Exploring the Languages:
