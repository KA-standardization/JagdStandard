package main

import (
	"fmt"
	"math"
)

type Point struct {
	X float64
	Y float64
}

/*
	方法的声明和普通函数的声明类似，只是在函数名字前多了一个参数，
	这个参数把这个方法绑定到参数对应的类型上
	包级别的函数Foo
	类型方法Bar

	同一个包下的任何类型都可以声明方法，只要不是指针类型和接口类型
	type P *int
	func (P) f(){} 编译错误，不允许本身是指针的类型进行方法声明
	命名类型与指向他们的指针*Ptr是唯一可以出现在接受者声明处的类型
	方法的名字是(*Point).func

	如果接收者p是Point类型的变量，但方法要求一个*Point
	我们可以简写： p.func()实际上编译器会对变量进行&p的隐式转换（只有变量才允许这么做，Point{1,2}.func()错误，不能获得Point类型字面量的地址）
*/
// 包级别的函数Foo
func Foo(p, q Point) float64 {
	return math.Hypot(q.X-p.X, q.Y-p.Y)
}

// 类型方法Bar
func (p Point) Bar(q Point) float64 {
	return math.Hypot(q.X-p.X, q.Y-p.Y)
}

func main() {
	q := Point{10, 12}
	p := Point{2, 4}
	fmt.Println(Foo(q, p))
	fmt.Println(p.Bar(q))
}
