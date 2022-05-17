package main

import "fmt"

func map_() {
	/*
		map是散列表的引用
			键拥有相同的类型
			值拥有相同的类型
	*/
	args := make(map[string]int)
	args["a"] = 11
	args["b"] = 12
	for k, v := range args {
		fmt.Printf("%s--%d\n", k, v)
	}
	args2 := map[string]int{
		"a": 11,
		"b": 12,
	}
	for k, v := range args2 {
		fmt.Printf("%s--%d\n", k, v)
	} 
	// 空map
	emptyMap := map[string]int{}
	fmt.Printf("%T\n", emptyMap)
	delete(args,"a")
}

func main() {
	map_()
}
