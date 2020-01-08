#include <stdio.h>
#include <stdlib.h>
#include <string.h>


const double sell = 100;
const double buy = 10;
const double hold = 50;


char* checkStock(double currentValue, char* advise);
void giveAdvise(char advise[]);


int main(void){
    char advise[10];
    char* pAdvise;

    pAdvise = checkStock(45, advise);
    giveAdvise(advise);

    pAdvise = checkStock(150,advise);
    giveAdvise(advise);


    return EXIT_SUCCESS;
}

char* checkStock(double currentValue, char advise[]){
    if(currentValue > sell){
        strcpy(advise, "sell");
    }
    else if(currentValue<sell && currentValue>hold){
        strcpy(advise, "hold");
    }
    else{
       strcpy(advise, "buy");
    }
    return advise;
}

void giveAdvise(char advise[]){
    switch (advise[0])
    {
        case 's': 
            printf("Sell \n");
            break;
        case 'h':
            printf("Hold \n");
            break;
        case 'b':
            printf("Buy \n");
            break;
        default:
            printf("No Advise \n");
            break;
    }
}
