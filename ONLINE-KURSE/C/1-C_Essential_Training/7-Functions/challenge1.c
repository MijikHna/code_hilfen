#include <stdio.h>
#include <stdlib.h>

#include "c1file.h"

extern float amount;
extern float accountBalance;

int main(void){

    int transactionCounter = 0;

    initializeAccount();
    getBalance();
    askCustomer();
    updateAccount(amount);
    getBalance();
    askCustomer();
    updateAccount(amount);
    addGift(5.0);
    getBalance();
    askCustomer();
    updateAccount(amount);
    addGift(2.0);
    getBalance();
    thankYou();


    return EXIT_SUCCESS;
}