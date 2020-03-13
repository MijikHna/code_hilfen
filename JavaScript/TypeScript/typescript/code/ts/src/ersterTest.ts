import { ErsteClass } from './ersteClass'

function test01() {
    console.log("Test");

    const ersteClass: ErsteClass = new ErsteClass('test', 150);
    ersteClass.printTest("Lalal");
}

test01()

