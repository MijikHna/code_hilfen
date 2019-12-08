#include <stdlib.h>
#include <stdio.h>

void countRecursivly(int small, int big);

int counter = 0;

int main(void){

    int small;
    int big;

    printf("Small: ");
    scanf("%d", &small);
    puts("");
    printf("Big: ");
    scanf("%d", &big);
    puts("-----------");

    countRecursivly(small, big);

    puts("-----------");
    return EXIT_SUCCESS;
}

void countRecursivly(int small, int big){
    if(small < big){
        printf("Small = %d\n", small);
        countRecursivly(small+1, big);
        counter++;
    }
    printf("Counter = %d \n", counter);
}