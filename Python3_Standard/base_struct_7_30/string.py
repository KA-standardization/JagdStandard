var = "hello"
print('www'+var)
print("www",var)
'''
\(在行尾时) 	续行符
\\ 	反斜杠符号
\' 	单引号
\" 	双引号
\a 	响铃
\b 	退格(Backspace)
\000 	空
\n 	换行
\v 	纵向制表符
\t 	横向制表符
\r 	回车
\f 	换页
\oyy 	八进制数，yy 代表的字符，例如：\o12 代表换行，其中 o 是字母，不是数字 0。
\xyy 	十六进制数，yy代表的字符，例如：\x0a代表换行
\other 	其它的字符以普通格式输出
'''
''' 字符串格式化 先用格式替代再传值
%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
%g	 %f和%e的简写
%G	 %f 和 %E 的简写
%p	 用十六进制数格式化变量的地址

格式化操作符辅助指令:
*	定义宽度或者小数点精度
-	用做左对齐
+	在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	显示的数字前面填充'0'而不是默认的空格
%	'%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''
'''
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
'''
str = '''
        这是个字符窜
        还是个字符串
        又是个
'''
print(str)
''' Python 的字符串常用内建函数
capitalize()    将字符串的第一个字符转换为大写
center(width, fillchar)      返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
count(str, beg= 0,end=len(string))  返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
bytes.decode(encoding="utf-8", errors="strict")     Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
encode(encoding='UTF-8',errors='strict')    以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
endswith(suffix, beg=0, end=len(string))    检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
expandtabs(tabsize=8)   把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
find(str, beg=0, end=len(string))   检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
index(str, beg=0, end=len(string))      跟find()方法一样，只不过如果str不在字符串中会报一个异常.
join(seq)   以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
len(string) 返回字符串长度
ljust(width[, fillchar])    返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
lower()     转换字符串中所有大写字符为小写.
lstrip()    截掉字符串左边的空格或指定字符。
maketrans() 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
max(str)    返回字符串 str 中最大的字母。
min(str)    返回字符串 str 中最小的字母。
replace(old, new [, max])   把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
rfind(str, beg=0,end=len(string))   类似于 find()函数，不过是从右边开始查找.
rindex( str, beg=0, end=len(string))    类似于 index()，不过是从右边开始.
rjust(width,[, fillchar])   返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
rstrip()    删除字符串字符串末尾的空格.
title() 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
translate(table, deletechars="")    根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
upper() 转换字符串中的小写字母为大写
zfill (width)   返回长度为 width 的字符串，原字符串右对齐，前面填充0

split(str="", num=string.count(str))    num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
splitlines([keepends])  按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
startswith(substr, beg=0,end=len(string))   检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
strip([chars])  在字符串上执行 lstrip()和 rstrip()
swapcase()  将字符串中大写转换为小写，小写转换为大写
isdecimal() 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
isalnum()   如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
isalpha()   如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
isdigit()   如果字符串只包含数字则返回 True 否则返回 False..
islower()   如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
isnumeric() 如果字符串中只包含数字字符，则返回 True，否则返回 False
isspace()   如果字符串中只包含空白，则返回 True，否则返回 False.
istitle()   如果字符串是标题化的(见 title())则返回 True，否则返回 False
isupper()   如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

'''

