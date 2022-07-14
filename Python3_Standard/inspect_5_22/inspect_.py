import inspect
import asyncio


def foo():
    pass


print(inspect.isfunction(foo))


def foo2():
    yield 1


print(inspect.isgeneratorfunction(foo2))

a = [1, 2, 3]
g = (i for i in a)
# 当该对象是一个生成器时返回``True``。
print(inspect.isgenerator(g))


class A:
    def __init__(self):
        pass


print(inspect.isclass(A))


class B:

    def boo(self):
        pass

    @classmethod
    def boo2(cls):
        pass

    @staticmethod
    def boo3():
        pass


b = B()
print(inspect.ismethod(b.boo))
print(inspect.ismethod(b.boo2))
print(inspect.ismethod(B.boo3))


async def foo3():
    await asyncio.sleep(1)


print(inspect.iscoroutinefunction(foo3))


class F:

    def __await__(self):
        pass


print(inspect.isawaitable(F()))


class FF:

    def __await__(self):
        pass


async def foo5():
    await FF()


ff = foo5()
# 当该对象是一个由 async def 函数创建的 协程 时返回``True``
print(inspect.iscoroutine(ff))
