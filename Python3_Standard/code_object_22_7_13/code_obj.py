import inspect

l = []


def foo(x: int, y=2, z=1, /, *args, **kwargs):
    import ctypes as cc
    a = 1

    def bar():
        nonlocal a
        a += 1

    return x + 1


c = foo.__code__
print(inspect.CO_COROUTINE)
print("co_flags: CO_* 标志的位图", c.co_flags)
print("co_name: 定义此代码对象的名称", c.co_name)
print("co_nlocals: 局部变量的数量", c.co_nlocals)
print("co_code: 字符串形式的原始字节码", c.co_code)
print("co_stacksize: 需要虚拟机堆栈空间", c.co_stacksize)
print("co_varnames: 参数名和局部变量的元组", c.co_varnames)
print("co_lnotab: 编码的行号到字节码索引的映射", c.co_lnotab)
print("co_filename: 创建此代码对象的文件的名称", c.co_filename)
print("co_names: 除参数和函数局部变量之外的名称元组", c.co_names)
print("co_posonlyargcount: 仅限位置参数的数量", c.co_posonlyargcount)
print("co_firstlineno: 第一行在Python源代码中的行号", c.co_firstlineno)
print("co_cellvars: 单元变量名称的元组(通过包含作用域引用)", c.co_cellvars)
print("co_argcount: 参数数量（不包括仅关键字参数、* 或 ** 参数）", c.co_argcount)
print("co_kwonlyargcount: 仅限关键字参数的数量（不包括 ** 参数）", c.co_kwonlyargcount)


def make_avg():
    # 在avg_函数中，s是自由变量（free variable）。这是一个技术术语，指未在本地作用域中绑定的变量，
    s = []

    def avg_(val):
        s.append(val)
        t = sum(s)
        return t / len(s)

    return avg_


avg = make_avg()
print("co_freevars: 自由变量的名字组成的元组（通过函数闭包引用）", avg.__code__.co_freevars)
avg(11)
avg(12)
print(avg.__closure__[0].cell_contents)
