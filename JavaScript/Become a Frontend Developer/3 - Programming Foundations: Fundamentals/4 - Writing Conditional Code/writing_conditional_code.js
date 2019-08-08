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