import ctypes

cLib1 = ctypes.cdll.LoadLibrary("./C/test.so")
cLib2 = ctypes.cdll.LoadLibrary("./C/test2.so")

cppLib1 = ctypes.cdll.LoadLibrary("./C++/test3.so")

goLib1 = ctypes.cdll.LoadLibrary("./GO/main.so")

'''
void hello(void){
    printf("Hello from C \n");
}
'''
cLib1.hello()

'''
int sum(int a, int b){
    return a + b;
}
'''
pyInt = cLib2.sum(10,5)
print("Das ist die Summe "+ str(pyInt)) 

cppLib1.hello()
print(cppLib1.sum(10, -5))

goLib1.Hello()
goLib1.Sum(10,12)