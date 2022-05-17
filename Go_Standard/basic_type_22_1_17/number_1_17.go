package main

import "fmt"

/*
	整数： 4种
		  int8 int16 int32 int64
	无符号整数： 4种
    	  uint8 uint16 uint32 uint64
	int/uint: 跟硬件和编译器有关 32位或64位
	同义词：
		  rune<-->int32: 用于指明一个值是Unicode码点（code point）
		  byte<-->uint8: 用于强调一个值是原始数据，而非量值
	uintptr: 存放指针

	int, uint, uintptr都有别于其大小明确的相似类型的类型

	有符号整数以补码表示，保留最高位为符号位， n位数字的取值范围是-2**(n-1)~2**(n-1)-1
	无符号整数由全部位构成其非负值 0~2**(n)-1
*/

/*
	两种大小的浮点数
		float32 float64
		math.MaxFloat32给出了float32的最大值约为3.4e38
		math.MaxFloat64 1.8e308
	10进制下float32的有效数字大约是6位，float64的有效数字大约是15位
*/

/*
	复数两种 complex64 complex128
*/

/*
	go 二元操作符运算优先级
	* 	/	 %	 <<	 >>	 &	 &^（位清空 AND NOT z=x&^y: 若y的某位是1，则z的对应位等于0，否则它就等于x的对应位）
	+ 	-	 |	 ^
	== 	!= 	 < 	 <=  > 	 >=
	&&
	||

	取模运算%仅能用于整数，取模余数的正负号总是与被除数一致（-5%3和-5%-3都等于2）
	/的行为取决于操作数是否为整型，整数相除，商会舍弃小数部分
	x<<n x*2**n n必须是无符号型
	x>>n x/2**n 向下取整
*/
func main() {
	var x uint8 = 1<<1 | 1<<5
	var y uint8 = 1<<1 | 1<<2

	fmt.Printf("%08b\n", x)
	fmt.Printf("%08b\n", y)
	// x&y交集 x|y并集 x^y对称差 x&^y差集
	s := []string{"a", "b", "c"}
	for i:=len(s)-1;i>=0;i--{
		fmt.Println(s[i])
	}
	o:=0666
	fmt.Printf("%d %[1]o %#[1]o\n",o) // 副词[1]告知Printf重复使用第一个操作数 副词#告知Printf输出相应的前缀0，0x,0X
	// %c输出文字字符 %q输出带有单引号 浮点数%g能自动保持足够的精度 %e有指数 %f无指数

	var xx complex128 = complex(1,2)
	var yy complex128 = complex(3,4)
	fmt.Println(xx*yy)
	fmt.Println(real(xx*yy)) // 内置函数real提取复数的实部
	fmt.Println(imag(xx*yy)) // 内置函数imag提取复数的虚部
}
