#include <stdio.h>
#include <stdlib.h>

int main (void){
    //2 - Declaring and using integer types
    puts("Memory size of each type\n");
    puts("------------------------\n");
    
    printf("Storage size of char: %lu byte\n", sizeof(char));
    printf("Storage size of unsigned char: %lu byte\n", sizeof(unsigned char));
    printf("Storage size of signed char: %lu byte\n", sizeof(signed char));
    printf("Storage size of int: %lu byte\n", sizeof(int));
    printf("Storage size of unsigned int: %lu byte\n", sizeof(unsigned int));
    printf("Storage size of short: %lu byte\n", sizeof(short));
    printf("Storage size of unsigned short: %lu byte\n", sizeof(unsigned short));
    printf("Storage size of long: %lu byte\n", sizeof(long));
    printf("Storage size of unsigned long: %lu byte\n", sizeof(unsigned long));
    printf("Storage size of void: %lu byte\n", sizeof(void));

    //3 - Declaring and using floating-points types
    puts("");
    printf("Storage size of float: %lu byte\n", sizeof(float));
    printf("Storage size of double: %lu byte\n", sizeof(double));
    printf("Storage size of long double: %lu byte\n", sizeof(long double));

    float floatNum;
    double doubleNum;
    long double longdoubleNum;

    floatNum = 2.0 / 3.0;
    doubleNum = 2.0 / 3.0;
    longdoubleNum = 2.0 / 3.0;

    puts("\nCompare precision at 4 decimal points:");
    printf("floatNum %1.4lf\n", floatNum);
    printf("doubleNum %1.4lf\n", doubleNum);
    printf("longdoubleNum %1.4Lf\n", longdoubleNum);

    puts("\nCompare precision at 10 decimal points:");
    printf("floatNum %1.10lf\n", floatNum);
    printf("doubleNum %1.10lf\n", doubleNum);
    printf("longdoubleNum %1.10lf\n", longdoubleNum);

    puts("\nCompare precision at 30 decimal points:");
    printf("floatNum %1.30lf\n", floatNum);
    printf("doubleNum %1.30lf\n", doubleNum);
    printf("longdoubleNum %1.30Lf\n", longdoubleNum);

    //4 - Using the void data type:

    //my Test:
    int myVar1 = 10;
    void* pMyVar1 = &myVar1;
    //printf("myVar1: %d \n", *(int) pMyVar1);

    //5 - Declaring and using Boolean types
    typedef int Bool;
    #define True 1
    #define False 0

    Bool myBoolVar = True;
    puts("");
    printf("Bool Var: %d", myBoolVar);
    puts("");
    return EXIT_SUCCESS;

}