#include <stdlib.h>
#include <stdio.h>

int main(void){
    //1 - Undertanding the use of arithmetic operators
    // +, - * / % ++ --
    int x = 5;
    int y = 7;

    int sum, diff, prod, divis, mod, incr, dec;

    sum = x + y;
    printf("Sum: %d \n", sum);

    //2 - Understanding the use of relationl operators
    //logical operators: ! == != > < >= <= && || 
    x = 3;
    y = 12;

    printf("if x = 3 and y = 12 then (x == y) is %d\n", (x == y));
    printf("if x = 3 and y = 12 then (x != y) is %d\n", (x != y));
    printf("if x = 3 and y = 12 then (x > y) is %d\n", (x > y));
    printf("if x = 3 and y = 12 then (x < y) is %d\n", (x < y));

    x = 1; y = 0;
    printf("if x = 1 and y = 0 then (x && y) is %d\n", (x && y));
    printf("if x = 1 and y = 0 then (x || y) is %d\n", (x || y));
    printf("if x = 1 and y = 0 then (!x) is %d\n", (!x));

    //3 - Making decisions using logical operators
    int weather = 1;
    int readiness = 0;
    int supermarket = 1;
    int minivan = 0;
    int wagon = 0;
    int mood = 1;
    int decision;

    decision = (weather && (readiness || supermarket) && (minivan || wagon) && mood);
    printf("Under these conditions the decision is: %d \n", decision);

    //4 - Performing bit-level calculations with bitwise operators
    //& | ^ ~ >> <<
    unsigned int x1 = 10;
    unsigned int y1 = 1;
    unsigned int result;

    result = x1 & y1;
    printf("x & y = %d \n", result);

    result = x1 | y1;
    printf("x | y = %d \n", result);

    result = x1 ^ y1;
    printf("x ^ y = %d \n", result);

    result = x1 >> 1;
    printf("x >> 1 = %d \n", result);

    result = x1 << 1;
    printf("x << 1 = %d \n", result);

    //5 - Using assignment operators in complex statements
    // = mehrere Ausdrücke in einem

    float r = 1.53;
    float s = 2.09;
    float t = -5.21;
    float result1;
    result1 = ((--r) < s)*t;
    printf("float Result = %f \n", result1);

    //6 - Implementing mathematical expressions

    //7 - Understanding the relationships between statements and expressions

    puts("-----------------------");
    return EXIT_SUCCESS;
}