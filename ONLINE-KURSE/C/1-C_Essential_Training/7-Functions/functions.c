#include <stdlib.h>
#include <stdio.h>

//1 - Understanding functional programming
void assessRoomCapacitivies(void);
void estimateWaitingVisitors(void);
void prcessData(void);
void generateReport(void);

int room1, room2, room3;
int vistors1, vistors2, vistors3;
int totalAvailableSeats, totalWaitingVisitors;

//2 - Passing variables to functions
//3 - Returning data from functions
//4 - Working with recursion:
/*Gefahr: Da bei jedem *Funktionsaufruf Stack erhöht wird => *irgendwann kein Stack mehr. Moderne *Funktionen können schauen,ob eine *Funktion sich zu oft aufruf und das *Programm abwürgen.
*/
void numberSeriesStops(int k);
void recursivHalfStop(int k, double val);

int main(void){

    //1 - Understanding functional programming
    assessRoomCapacitivies();
    estimateWaitingVisitors();
    prcessData();
    generateReport();

    //2 - Passing variables to functions
    //3 - Returning data from functions
    //4 - Working with recursion
    puts("-------4---------");
    numberSeriesStops(1);
    recursivHalfStop(1, 1000.0);

    return EXIT_SUCCESS;
}

//1 - Understanding functional programming
void assessRoomCapacitivies(void){
    printf("enter seats left in room1:");
    scanf("%d", &room1);
    printf("enter seats left in room2:");
    scanf("%d", &room2);
    printf("enter seats left in room3:");
    scanf("%d", &room3);
}
void estimateWaitingVisitors(void){
    printf("enter number of visitors waiting for room 1:");
    scanf("%d", &vistors1);
    printf("enter number of visitors waiting for room 2:");
    scanf("%d", &vistors2);
    printf("enter number of visitors waiting for room 3:");
    scanf("%d", &vistors3);
}
void prcessData(void){
    totalAvailableSeats = room1 + room2 + room3;
    totalWaitingVisitors = vistors1 + vistors2 + vistors3;
}
void generateReport(void){
    printf("overall there are still seats available (1=yes, 0=no): %d\n", totalAvailableSeats>totalWaitingVisitors);
    printf("room 1 can accept more visitors(1=yes, 0=n0): %d \n", room1 > vistors1);
    printf("room 2 can accept more visitors(1=yes, 0=n0): %d \n", room2 > vistors2);
    printf("room 3 can accept more visitors(1=yes, 0=n0): %d \n", room3 > vistors3);
}

//2 - Passing variables to functions
//3 - Returning data from functions
//4 - Working with recursion
void numberSeriesStops(int k){
    printf("k bevor: %d \n", k);
    if( k < 10){
        numberSeriesStops(k+1);
    }
    printf("k after %d \n", k);
}
void recursivHalfStop(int k, double val){
    printf("k bevor: %d; val: %f\n", k, val);
    if( k < 10){
        recursivHalfStop(k+1, val/2.0);
    }
    printf("k after: %d; val: %f\n", k, val);
}