#include <stdio.h>
#include <stdlib.h>


int main(void){

    //1 - Understanding Strings
    puts("Hello World");

    char address[30] = "123 Some Street SomeCity, USA 12345";

    char name[40] = "FirstName MiddleName LastName";

    printf("Address: %s \n", address);
    printf("Name: %s \n", name);

    //2 - Using screen-based Input/Output
    char c;
    printf("How do you feel on a scale of 1-5?");
    c=getchar();
    
    printf("Enter name: ");
    scanf("%s", name);

    printf("Enter your address: ");
    scanf("%s", address);

    printf("Entered name: %s \n", name);
    printf("Entered address: %s \n", address);
    putchar(c);

    //Manipulating strings:
    #include <string.h>
    //strcmp(str1, str2)
    //strcpy(dest, src)
    //memcpy(dest, src, n);
    //strlen(str)
    char str1[20];
    char str2[20];

    puts("------1-------");
    strcpy(str1, "Anybody");
    strcpy(str2, "Anybody home");

    int len1 = strlen(str1);
    printf("Length of string1: %d\n", len1);
    int len2 = strlen(str2);
    printf("Length of string1: %d\n", len2);

    puts("------2-------");
    strcpy(str1, "your house");
    strcpy(str2, "my house");

    len1 = strlen(str1);
    printf("Length of string1: %d\n", len1);
    len2 = strlen(str2);
    printf("Length of string1: %d\n", len2);

    puts("------3-------");
    strcpy(str1, "our house");
    strcpy(str2, "our house");

    len1 = strlen(str1);
    printf("Length of string1: %d\n", len1);
    len2 = strlen(str2);
    printf("Length of string1: %d\n", len2);

}