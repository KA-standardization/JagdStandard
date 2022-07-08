# Tools

> https://www.cygwin.com/
>
> Windows操作系统提供Linux风格的命令

### file

> file通过检查文件中某些特定字段来确认文件类型

> file执行的幻数检查由幻数文件所包含的规则控制
>
> > 位置 
> >
> > /usr/share/file/magic 
> >
> > /usr/share/misc/magic  # CentOS 3.10.0-1160.el7.x86_64
> >
> > /etc/magic

### PE Tools

> http://petools.org.ru/petools.shtml
>
> PE Tools: 是一组用于分析Windows系统中正在运行的进程和可执行文件的工具

> 二进制文件模糊技术

### PEID

> PEiD: 用于识别构建某一特定Windows PE二进制文件所使用的编译器,确定用于模糊Windows PE二进制文件工具
>
> http://petools.org.ru/petools.shtml
>
> https://zhuanlan.zhihu.com/p/430834295

### nm

> nm: 列举目标文件中的符号

| 符号 | 描述(大写字母表示全局符号,小写字母表示局部符号)              |
| ---- | ------------------------------------------------------------ |
| U    | 未定义符号,通常为外部符号引用                                |
| T    | 在文本部分定义的符号,通常为函数名称                          |
| t    | 在文本部分定义的局部符号,在C程序中,这个符号通常等同于一个静态函数 |
| D    | 已初始化的数据值                                             |
| C    | 未初始化的数据值                                             |

```
$nm test.so
0000000000201030 B __bss_start
0000000000201030 b completed.6355
                 w __cxa_finalize@@GLIBC_2.2.5
00000000000005c0 t deregister_tm_clones
0000000000000630 t __do_global_dtors_aux
0000000000200e00 t __do_global_dtors_aux_fini_array_entry
0000000000200e10 d __dso_handle
0000000000200e18 d _DYNAMIC
0000000000201030 D _edata
0000000000201038 B _end
00000000000006f4 T _fini
00000000000006a5 T foo
0000000000000670 t frame_dummy
0000000000200df8 t __frame_dummy_init_array_entry
0000000000000780 r __FRAME_END__
0000000000201000 d _GLOBAL_OFFSET_TABLE_
                 w __gmon_start__
0000000000000700 r __GNU_EH_FRAME_HDR
0000000000000558 T _init
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
0000000000200e08 d __JCR_END__
0000000000200e08 d __JCR_LIST__
                 w _Jv_RegisterClasses
00000000000005f0 t register_tm_clones
                 U sqrt
0000000000201030 d __TMC_END__
```

### ldd(list dynamic dependencies)

> 列举任何可执行文件所需的动态库

```
$ldd main
linux-vdso.so.1 =>  (0x00007ffed579e000)
libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f38b2194000)
libc.so.6 => /lib64/libc.so.6 (0x00007f38b1dc6000)
/lib64/ld-linux-x86-64.so.2 (0x00007f38b23b0000)
```

### objdump

> 显示与目标有关的信息

```
  -a, --archive-headers    Display archive header information
  -f, --file-headers       Display the contents of the overall file header
  -p, --private-headers    Display object format specific file header contents
  -P, --private=OPT,OPT... Display object format specific contents
  -h, --[section-]headers  Display the contents of the section headers
  -x, --all-headers        Display the contents of all headers
  -d, --disassemble        Display assembler contents of executable sections
  -D, --disassemble-all    Display assembler contents of all sections
  -S, --source             Intermix source code with disassembly
  -s, --full-contents      Display the full contents of all sections requested
  -g, --debugging          Display debug information in object file
  -e, --debugging-tags     Display debug information using ctags style
  -G, --stabs              Display (in raw form) any STABS info in the file
  -W[lLiaprmfFsoRt] or
  --dwarf[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,
          =frames-interp,=str,=loc,=Ranges,=pubtypes,
          =gdb_index,=trace_info,=trace_abbrev,=trace_aranges,
          =addr,=cu_index]
                           Display DWARF info in the file
  -t, --syms               Display the contents of the symbol table(s)
  -T, --dynamic-syms       Display the contents of the dynamic symbol table
  -r, --reloc              Display the relocation entries in the file
  -R, --dynamic-reloc      Display the dynamic relocation entries in the file
  @<file>                  Read options from <file>
  -v, --version            Display this program's version number
  -i, --info               List object formats and architectures supported
  -H, --help               Display this information
```

| arg                                                          | decs                                                |                                      |
| ------------------------------------------------------------ | --------------------------------------------------- | ------------------------------------ |
| -a, --archive-header                                         | Display archive header information                  | 显示存档头信息                       |
| -f, --file-headers                                           | Display the contents of the overall file header     | 显示整个文件头的内容                 |
| -p, --private-header                                         | Display object format specific file header contents | 显示对象格式特定的文件头内容         |
| -P, --private=OPT,OP                                         | Display object format specific contents             | 显示对象格式特定的内容               |
| -h, --[section-]head                                         | Display the contents of the section headers         | 显示节标题的内容                     |
| -x, --all-headers                                            | Display the contents of all headers                 | 显示所有标题的内容                   |
| -d, --disassemble                                            | Display assembler contents of executable sections   | 显示可执行部分的汇编程序内容         |
| -D, --disassemble-al                                         | Display assembler contents of all sections          | 显示所有部分的汇编器内容             |
| -S, --source                                                 | Intermix source code with disassembly               | 将源代码与反汇编混合                 |
| -s, --full-contents                                          | Display the full contents of all sections requested | 显示请求的所有部分的全部内容         |
| -g, --debugging                                              | Display debug information in object file            | 在目标文件中显示调试信息             |
| -e, --debugging-tags                                         | Display debug information using ctags style         | 使用ctag样式显示调试信息             |
| -G, --stabs                                                  | Display (in raw form) any STABS info in the file    | 显示(以原始形式)任何stab信息在文件中 |
| -W[lLiaprmfFsoRt]                                            | Display DWARF info in the file                      | 在文件中显示DWARF信息                |
| --dwarf[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,          =frames-interp,=str,=loc,=Ranges,=pubtypes,=gdb_index,=trace_info,=trace_abbrev,=trace_aranges, =addr,=cu_index] | Display DWARF info in the file                      | 在文件中显示DWARF信息                |
| -t, --syms                                                   | Display the contents of the symbol table(s)         | 显示符号表的内容                     |
| -T, --dynamic-syms                                           | Display the contents of the dynamic symbol table    | 显示动态符号表的内容                 |
| -r, --reloc                                                  | Display the relocation entries in the file          | 显示文件中的重定位项                 |
| -R, --dynamic-reloc                                          | Display the dynamic relocation entries in the file  | 显示文件中的动态重定位项             |
| @<file>                                                      | Read options from <file>                            | 从文件读取选项                       |
| -i, --info                                                   | List object formats and architectures supported     | 列出所支持的对象格式和体系结构       |

### dumpbin

> https://docs.microsoft.com/zh-cn/cpp/build/reference/dumpbin-options?view=msvc-170
>
> dumpbin: 可从PE二进制文件的各个部分提取信息,包括符号,导入的函数名,导出的函数名和反汇编代码

### c++filt

> yum install gcc-c++ libstdc++-devel
>
> name mangling: 为名称完全相同的函数生成唯一名称的过程,通常一个目标文件中不能有两个名称相同的函数,为了支持重载,编译器将描述函数参数类型的信息合并到函数的原始名称中,从而为重载函数生成唯一的函数名称
>
> 将每个输入的名称看成是改编后的名称(mangled name),并设法确定用于生成该名称的编译器

```
[root@localhost Documents]# nm test|grep foo
00000000004009bb t _GLOBAL__sub_I__Z3foov
00000000004008cf T _Z3fooi
0000000000400905 T _Z3fooiPc
00000000004008ad T _Z3foov
[root@localhost Documents]# nm test|grep foo|c++filt
00000000004009bb t _GLOBAL__sub_I__Z3foov
00000000004008cf T foo(int)
0000000000400905 T foo(int, char*)
00000000004008ad T foo()
```

### strings

> strings专门用于提取文件中字符串内容,通常,使用该工具不会受到文件格式的限制, 默认设置至少包含4个字符的7位ASCII序列

```
# 强制strings 扫描整个文件
strings -a test
# 显示所发现的每一个字符串的文件偏移量信息 --radix={o,d,x}
strings -t x test
# 搜索更广泛的字符(16位Unicode字符) --encoding={s,S,b,l,B,L}
strings -e s test
```

### ndisasm

> https://www.nasm.us/
>
> > https://zhuanlan.zhihu.com/p/107186324 
>
> https://github.com/gdabah/distorm
>
> > pip install distorm3 
> >
> > \#include \<Python\>: python3-devel 
> >
> > yasm: http://www.tortall.net/projects/yasm/releases/

# IDA

### 1.入门

> Edit->Segments->Rebase Program: 修改IDA镜像的基址
>
> 使用二进制加载器的情形包括: 分析从网络数据包或日志文件中提取出来的ROM镜像和破解程序负载

> id0: 是一个二叉树形式的数据库
>
> id1: 包含描述每个程序字节的标记
>
> id2: 
>
> nam: 包含与IDA的Names窗口中显示的给定程序位置有关的索引信息	
>
> til: 用于存储与一个给定数据库的本地类型定义有关的信息

> 在有条件跳转位置终止的基本块可能会生成两种流
>
> > yes: 执行分支, 默认为绿色
> >
> > no: 不执行分支, 默认为红色
>
> 只有一个后继块的基本块, 默认为蓝色, 指向下一个即将执行的块

> 给每一行添加行前缀,Options-->General-->Disassembly, 给每一个反汇编行添加虚拟地址
>
> 通常虚拟地址以[区域名称]:[虚拟地址]

> names窗口
>
> IDA给某个位置命名时,他会使用该位置的虚拟地址和一个表示该位置的类型的前缀进行命名

| 规则      | desc                         |
| --------- | ---------------------------- |
| sub_xxx   | 地址xxx处的子例程(函数,方法) |
| loc_xxx   | 地址xxx处的一个指令          |
| byte_xxx  | 位置xxx处的8位数据           |
| word_xxx  | 位置xxx处的16位数据          |
| dword_xxx | 位置xxx处的32位数据          |
| unk_xxx   | 位置xxx处的大小未知的数据    |

### 2.编译程序

#### 栈帧(激活记录)

> Stack frame: 程序运行时栈中分配的内存块, 专门用于特定函数调用

#### 调用函数的详细步骤

> 1. 调用方将被调用函数所需的任何参数放入到该函数所采用的调用约定指定的位置(如果参数被放到运行时栈上, 该操作可能导致程序的栈指针发生改变)
>
> 2. 调用方将控制权转交给被调用的函数, 这个过程常由x86CALL或MIPS JAL等指令执行, 然后, 返回地址被保存到程序栈或CPU寄存器中.
>
> 3. 如有必要, 被调用的函数会配置一个栈指针(帧指针是一个指向栈帧位置的寄存器, 通常栈帧内的变量根据它们与帧指针所指向的位置的相对距离来引用), 并保存调用方希望保持不变的任何寄存器值.
>
> 4. 被调用的函数为它可能需要的任何局部变量分配空间,通常通过调整程序栈指针在运行时栈上保留的空间来完成这一任务.
>
> 5. 被调用的函数执行其操作,可能生成一个结果,在执行操作的过程中,被调用的函数可能会访问调用函数传递给它的参数, 如果函数返回一个结果, 此结果通常被放置到一个特定的寄存器中, 或者放置到函数返回后调用方可立即访问的寄存器中.
>
> 6. 函数完成其操作后, 任何为局部变量保留的栈空间将被释放. 通常逆向执行第4部中的操作,即可完成这个任务.
>
> 7. 如果某个寄存器的值还为调用方保存第3步, 那么将其恢复到原始值, 这包括恢复调用方的帧指针寄存器.
>
> 8. 被调用的函数将控制权返还给调用方,实现这一操作的主要指令包括x86 RET和MIPS JR, 根据所使用的调用约定, 这一操作可能还会从程序栈中清除一个或多个参数
>
> 9. 调用方一旦重新获得控制权,它可能需要删除程序栈中的参数,这时可能需要对栈进行调整, 以将程序栈指针恢复到第1步以前的值
>
>    第3步,第4步通常在进入函数时执行, 它们共同称为该函数的序言, 同样第6步到第8步一般在函数结束时执行,它们共同构成该函数的尾声. 第5步则代表函数的主体, 它们是调用一个函数时执行的全部操作.

#### 调用约定

> cdecl: 调用方按从右到左的顺序将函数参数放入栈中, 在被调用的函数完成其操作时, 调用方负责从栈中清除参数(从右到左在栈中放入参数的一个结果是, 如果函数被调用, 最左边(第一个)参数将始终位于栈顶, 无论函数有多少参数, 我们都可轻易的找到第一个参数)
>
> stdcall: 调用方按从右到左的顺序将函数参数放入栈中, 被调用的函数负责删除栈中的函数参数(对参数数量固定的函数使用)
>
> fastcall: 是stdcall的一个变体,它向CPU寄存器最多传递两个参数(前两个参数分别位于ECX和EDX寄存器中), 剩余的其他参数则以stdcall约定的方式从右到左放入栈上, 在返回其调用方法时, fastcall函数负责从栈中删除参数.
>
> thiscall: (C++类中的非静态成员函数与标准函数不同, 它们需要使用this指针, 该指针指向用于调用函数的对象, 用于调用函数的对象的地址必须由调用方提供, 它在调用非静态成员函数时作为参数提供)它将this传递到ECX寄存器中, 并且和stdcall中一样, 它要求非静态成员函数清除栈中的参数, GNU g++编译器将this看成是任何非静态成员函数的第一个隐含参数, 而在所有其他方面与cdecl约定相同(在调用非静态成员函数之前, this被放置到栈顶)

### 3.导航

> 跳转地址: 
>
> > Jump-->Jump to Address G
> >
> > Jump-->Jump to Next Position Ctrl Enter
> >
> > Jump-->Jump to Previous Position Esc

