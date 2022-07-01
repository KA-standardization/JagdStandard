### 异常

> 不抛出任何异常

```c++
void func() throw(){
    
}
```

### 指针

```c++
int age = 1;
int length = 2;
// ref1不能修改指向,但是可以通过ref1间接修改所指向的变量
int & const ref1 =age;
ref1=30;
// ref2不能修改指向,不可以通过ref2间接修改所指向的变量
int const &ref2 =age;
// p1不能修改指向,但是可以利用p1间接修改所指向的变量
int * const p1 =&age;
*p1 =30;
// p2可以修改指向,不可以利用p2间接修改所指向的变量
int const *p2 =&age;
*p2=$length;
```

```mem
				mem_addr content
&age ebp-0Ch 	1122H
				1123H
				1124H		30
				1125H
				1126H
&p	ebp-18h		1127H
				1128H		ebp-0Ch
				1129H		1122H
				112AH
```

#### 数组指针

> []的优先级高于\*，所以ptr_arr是一个数组，其次括号内只有*，所以数组元素是指针。接着看外面，[5]说明指针指向5个元素的数组，数组元素类型是整型

```c++
#include <stdio.h>

int main(){
    int arr1[4][5]={0};
    int arr2[7][5]={0};
    int (*ptr_arr[])[5]={arr1,arr2};
    return 0;
}
```

```
// 指针数组,数组里面可以存放3个int *
int *arr1[3] ={p1,p2,p3};
// 用于指向数组的指针([] 优先级高于 *)
int (*arr2)[3];
```

### vcpkg

```
https://github.com/microsoft/vcpkg
$env:HTTP_PROXY="127.0.0.1:9090"
$env:HTTPS_PROXY="127.0.0.1:9090"

./vcpkg install openssl:x64-windows

Error: Building package opencl:x64-windows failed with: BUILD_FAILED

github --> openssl https://github.com/openssl/openssl download

 .\vcpkg.exe integrate install
```

### gcc

```
gcc -o xxxx xxxx.c -lmysqlclient -I /usr/include/mysql/
```



