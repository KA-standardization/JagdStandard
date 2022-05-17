package main

import (
	"fmt"
	"io"
	"os"
)

var g *int

func f() {
	/*
		x从f中逃逸
		x一定使用堆空间，尽管它被声明为局部变量，它会在f函数返回后还可以从g变量访问
	*/
	var x int
	x = 1
	g = &x
}

func b() {
	/*
		当函数返回时，变量*y变得不可访问，可回收
		编译器可以安全的在栈上分配*y
	*/
	y := new(int)
	*y = 1
}

func main() {
	//类型断言
	var w io.Writer
	w = os.Stdout
	a,b := w.(*os.File)
	fmt.Println(*a)
	fmt.Println(b)
}
