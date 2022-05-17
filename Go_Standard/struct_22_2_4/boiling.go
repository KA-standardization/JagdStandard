package main

import "fmt"

/*
var		变量
const	常量
type	类型
func	函数
*/
/*
var	变量是存储值的地方
var name type = expression
类型和表达式可以省略一个，但不能都省略
		省略表达式：初始值对应于类型的零值
					数字=0
					布尔=false
					字符=""
					接口和引用类型(slice ptr map chan func)=nil
短变量声明
name := expression
name的类型由表达式的类型决定
短声明最少声明一个新变量
{
f,err:=os.Open(file)
f,err:=os.Create(outfile) 编译失败，没有新的变量
}
*/
/*
ptr 指针的值是一个变量的地址，使用指针，可以在无需知道变量名的情况下，间接读取或更新变量的值
例：
	var x int，表达式&x(x的地址)获取一个指向整型变量的指针，它的类型是整型指针(*int)
	x:=1
	p:=&x
	fmt.Println(*p) //表达式*p，获取变量的值
	*p=2 //x=2,*p代表一个变量，所以它可以出现在赋值操作符的左边
&取地址操作符
指针类型的零值=nil,ptr!=nil,结果为true说明ptr指向一个变量
指针可以比较大小，当且仅当两个指针指向同一个变量或者两者都是nil时才相等
*/
func ptr() *int {
	/*
		函数返回局部变量的地址是非常安全的
		通过调用函数产生的局部变量v即使在调用返回后依然存在
		ptr() == ptr() 每次调用都会返回不同的值
	*/
	v := 1
	return &v
}
func ptr2(p *int) int {
	/*
		指针包含变量的地址，所以传递一个指针参数给函数，能够让函数更新间接传递的变量值
	*/
	*p++
	return *p
}
/*
new
表达式new(Type)，创建一个未命名的Type类型的变量，初始化为Type类型的零值，并返回其地址（地址类型为*Type）
	return new(int) //*int类型
		等价于
	var tmp int
	return &tmp //*int类型
*/

func main() {
	// func ptr
	fmt.Println(ptr() == ptr())
	fmt.Println(*ptr() == *ptr())
	// func ptr2
	v := 1
	ptr2(&v)
	fmt.Println(ptr2(&v))
}
