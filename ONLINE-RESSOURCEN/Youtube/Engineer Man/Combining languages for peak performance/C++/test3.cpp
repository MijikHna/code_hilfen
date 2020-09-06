#include <iostream>

// diese Funktionen existeiren als Prototypen in anderer Datei
extern "C"{
    void hello(void);
    int sum(int a, int b);
}

//extern void hello(void);
//extern int sum(int a, int b);

void hello(void){
    std::cout << "Hello from C++" << std::endl;
}

int sum(int a, int b){
    return a + b;
}