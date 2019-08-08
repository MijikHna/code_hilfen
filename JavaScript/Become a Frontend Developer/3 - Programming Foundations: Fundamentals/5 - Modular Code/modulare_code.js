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
