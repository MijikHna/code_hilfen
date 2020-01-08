//Convert centimetrs to feet and inches

#include <stdlib.h>
#include <stdio.h>

/* Proramm bekommt die Hoehe in cm
* 1) Hoehe in feet und inches ausgeben
* 2)     
*/

int main(void){

    double cm;
    int feet;
    double inch;

    printf("Height: ");
    scanf("%lf", &cm);

    //feet = (double) cm / 30.48;
    //inch = (cm -feet * 30.48) / 2.54;

    inch = cm / 2.54;
    feet = inch / 12;
    inch = inch - (feet * 12);

    printf("Height: %d feet, %lf inches", feet, inch);

    //

    return EXIT_SUCCESS;
}