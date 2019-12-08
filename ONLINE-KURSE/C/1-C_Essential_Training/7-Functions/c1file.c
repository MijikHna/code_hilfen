#include <stdio.h>
#include <stdlib.h>

#include "c1file.h"

void initializeAccount(){
    accountBalance = 0.0;
}
void getBalance(void){
    printf("\n Ther current balance is $%.2f \n", accountBalance);
}
void askCustomer(){
    printf("Next transaction please... \n");
    printf("Enter amount to credit (pos) or (neg)");
    scanf("%f", &amount);
}
void updateAccount(float amount){
    accountBalance += amount;
}
void addGift(float giftAmount){
    accountBalance += giftAmount;
    printf("Congratulation, A gift of $%.2f has been added", giftAmount);
}
void thankYou(){
    printf("------Thank you!!!-------");
}
