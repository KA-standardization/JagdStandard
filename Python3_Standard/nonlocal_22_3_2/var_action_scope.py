b = 3


def foo(a):
    print("foo a-->", a)
    print("foo b-->", b)


foo(11)
########################################################################################################################
"""
可事实是，Python 编译函数的定义体时，它判断b是局部变量，因为在函数中给它赋值了。 
生成的字节码证实了这种判断，Python会尝试从本地环境获取b。后面调用f2(3)时， 
f2的定义体会获取并打印局部变量a的值，但是尝试获取局部变量b的值时，发现b没有绑定值。
b2 = 3


def foo2(a):
    print(a)
    print(b2)
    b2 = 9


foo2(11)
"""
########################################################################################################################
b3 = 3


def foo3(a):
    global b3
    print("foo3 a-->", a)
    print("foo3 b-->", b3)
    b3 = 9


foo3(11)
foo3(11)
########################################################################################################################
"""
只有涉及嵌套函数时才有闭包问题。
闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体中定义的非全局变量。函数是不是匿名的没有关系，
关键是它能访问定义体之外定义的非全局变量。
    

"""
"""
闭包
    s = []

    def avg_(val):
        s.append(val)
        t = sum(s)
        return t / len(s)

    return avg_
闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定。 
注意，只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量。
"""


# 调用make_averager 时，返回一个averager函数对象。每次调用averager时，它会把参数添加到系列值中，然后计算当前平均值，
def make_avg():
    # 在avg_函数中，s是自由变量（free variable）。这是一个技术术语，指未在本地作用域中绑定的变量，
    s = []

    def avg_(val):
        s.append(val)
        t = sum(s)
        return t / len(s)

    return avg_


avg = make_avg()
print(avg(10))
print(avg(11))
print(avg(12))

# Python在 __code__ 属性（表示编译后的函数定义体）中保存局部变量和自由变量的名称，
print(avg.__code__.co_freevars)
print(avg.__code__.co_varnames)
# s的绑定在返回的avg_函数的__closure__属性中。avg.__closure__中的各个元素对应于avg.__code__.co_freevars中的一个名称。
# 这些元素是cell对象，有个cell_contents属性，保存着真正的值。
# closure 闭包 cell 单元格
print(avg.__closure__[0].cell_contents)
########################################################################################################################
"""
1.当count是数字或任何不可变类型时，count+=1语句的作用其实与count=count+1一样。因此，我们在averager的定义体中为count赋值了， 
这会把count变成局部变量。total变量也受这个问题影响。
2.但是对数字、字符串、元组等不可变类型来说，只能读取，不能更新。如果尝试重新绑定，例如count=count+1，其实会隐式创建局部变量count。
这样，count就不是自由变量了，因此不会保存在闭包中。
def make_avg():
    c = 0
    t = 0

    def avg_(val):
        c += 1
        t += val
        return t / c

    return avg_
"""


def make_avg2():
    c = 0
    t = 0

    def avg_(val):
        nonlocal c, t
        c += 1
        t += val
        return t / c

    return avg_


avg2 = make_avg2()
print(avg2(10))
print(avg2(11))
print(avg2.__code__.co_freevars)
print(avg2.__closure__[0].cell_contents)
print(avg2.__closure__[1].cell_contents)
