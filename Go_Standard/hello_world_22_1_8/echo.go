package main

import (
	"fmt"
	"os"
	"strings"
)

// := 短变量声明 根据初始化的值给予合适类型

func main() {
	var s, tmp string
	fmt.Println(os.Args[0])
	for i := 1; i < len(os.Args); i++ {
		s += tmp + os.Args[i]
		tmp = " "
	}
	fmt.Println(s)
}
/*
s := ""
var s string
var s = ""
var s string = ""
*/
func echo2() {
	s, tmp := "", ""
	// range产生 pair 不需要索引值 索引赋予临时变量 _(空标识符) 然后忽略
	for _, arg := range os.Args[1:] {
		s += tmp + arg
		tmp = " "
	}
	fmt.Println(s)
}

func echo3(){
	fmt.Println(strings.Join(os.Args[1:]," "))
}
