package main

import (
	"crypto/sha256"
	"fmt"
)

/*
	数组是具有固定长度且拥有零个或者多个相同数据类型元素的序列
*/
type C int

const (
	USD C = iota
	EUR
	RMB
)

func array() {
	var a [3]int = [3]int{100, 101, 102}
	for i, v := range a {
		fmt.Printf("%d--%d\n", i, v)
	}
	// 一个新数组中的元素初始值为元素类型的零值
	var r [3]int = [3]int{12, 13}
	fmt.Println(r[2])
	// ...出现在数组长度的位置，那么数组的长度由初始化数组的元素个数决定
	q := [...]int{1, 2, 3}
	fmt.Printf("%T\n", q) //%T 类型
	symbol := [...]string{USD: "a", EUR: "B", RMB: "c"}
	fmt.Println(symbol[RMB])
	// 定义一个拥有100元素的数组
	r2 := [...]int{99: 0}
	for i, v := range r2 {
		fmt.Printf("%d--%d\n", i, v)
	}
}

func crypto() {
	// 固定长度256位摘要信息[32]byte
	c := sha256.Sum256([]byte("x"))
	c2 := sha256.Sum256([]byte("X"))
	fmt.Printf("%x\n%x\n%t\n", c, c2, c == c2)
}

func slice() {
	/*
		slice表示一个拥有相同类型元素的可变长度的序列
		slice通常写成[]T，T是其中元素的类型
		slice包含指向数组元素的指针
		无法比较
	*/
	// 先创建有固定长度的数组，在创建指向数组的slice
	var s []int =[]int{1,2,3,4,5}
	fmt.Println(s)
	// append 扩容缩容slice
	s=append(s, 122)
	fmt.Println(len(s))
	fmt.Println(cap(s))
}

func main() {
	array()
	crypto()
	slice()
}
