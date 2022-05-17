"""
1装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。
2装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象。

严格来说，装饰器只是语法糖。如前所示，装饰器可以像常规的可调用对象那样调用，其参数是另一个函数。
有时，这样做更方便，尤其是做元编程（在运行时改变程序的行为）时。
"""


def foo(func):
    def inner():
        print("run inner")

    return inner


@foo
def bar():
    print("run bar")


# 发现 bar 现在是 inner 的引用
bar()
########################################################################################################################
"""
装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。这通常是在导入时（即Python加载模块时），
"""
registry = []

"""
register装饰器原封不动地返回被装饰的函数，但是这种技术并非没有用处。 
很多 PythonWeb框架使用这样的装饰器把函数添加到某种中央注册处，例如把URL模式映射到生成HTTP响应的函数上的注册处。 
这种注册装饰器可能会也可能不会修改被装饰的函数。
"""


def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def main():
    print("registry-->{}".format(registry))
    registry[0]()


"""
register在模块中其他函数之前运行（两次）。调用register时，传给它的参数是被装饰的函数，例如 <function f1 at 0x000001DAA3DB9378>。 
加载模块后，registry中有两个被装饰函数的引用：
"""
main()


