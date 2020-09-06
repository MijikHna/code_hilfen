  
const ffi = require('ffi');

const c_lib1 = ffi.Library('./C/test.so', {
    // man muss als zusätzlicher Parameter angeben, den Namen der Funktion, + Typ der Parameter
    hello: ['void', []], //void = Return-Typ, [] = keine Parameter
});

const c_lib2 = ffi.Library('./C/test2.so', {
    // man muss als zusätzlicher Parameter angeben, den Namen der Funktion, + Typ der Parameter
    sum: ['int', ['int', 'int']] //return = int, [int, int]zwei Parameter int ,int
});

const cpp_lib = ffi.Library('./C++/test3.so', {
    hello: ['void', []],
    sum: ['int', ['int', 'int']]
});
/*
const go_lib = ffi.Library('./GO/test.so', {
    Hello: ['void', []],
    Sum: ['int', ['int', 'int']]
});
*/
console.log('\n\njavascript tests')

// c
c_lib1.hello()
console.log(c_lib2.sum(1, 2))

// cpp
cpp_lib.hello()
console.log(cpp_lib.sum(1, 2))

/*
// go
go_lib.Hello()
console.log(go_lib.Sum(1, 2))
*/