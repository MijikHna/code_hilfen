package main

import (
	"C"
	"fmt"
)

func Hello() {
	fmt.Println("Hello from go")
}

func Sum(a int, b int) int {
	return a + b
}

func main() { }