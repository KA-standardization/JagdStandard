package main

import (
	"fmt"
	"net/url"
)

func main(){
	a:=url.QueryEscape("http://mp.weixin.qq.com/s?__biz=MzkzMDIyODc1OA==&amp;mid=2247486912&amp;idx=5&amp;sn=1b166ba8ecb911a7f8d1988bd8eafcd8&amp;chksm=c27c32b9f50bbbaf65d57654e37bae25d9f6cd1b4355c457fb4e47fcda9d027a0430e641ccc7#rd")
	fmt.Print(a)
}
