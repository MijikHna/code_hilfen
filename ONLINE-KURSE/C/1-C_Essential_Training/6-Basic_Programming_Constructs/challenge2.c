//Koch- und Friertemperaturen in Celcius,, Fahrenheit und Kelvin berechnen

#include <stdio.h>
#include <stdlib.h>

const int celcious0 = 0;
const int celcious100 = 100;

int main(void){
    const int celcious0 = 0;
    const int celcious100 = 100;
    double fahrenheit0;
    double fahrenheit100;
    double kelvin0;
    double kelvin100;

    fahrenheit0 = celcious0 * (9/5) + 32;
    fahrenheit100 = celcious100 *(9/5) + 32;
    kelvin0 = celcious0 + 273;
    kelvin100 = celcious100 + 273;

    printf("Friertemperatur: Fahrenheit - %.0lf; Kelvin - %lf \n", fahrenheit0, kelvin0);
    printf("Kochtemperatur: Fahrenheit - %.0lf; Kelvin - %lf \n", fahrenheit100, kelvin100);



}