import sys

one = []
print(sys.getrefcount(one))
t = one
print(sys.getrefcount(one))
del t
print(sys.getrefcount(one))


# sys getrefcount 会维护对象本身的一个临时引用

class MyClass:
    pass


# 字节
objs = [[], (), {}, 'c', 'string', MyClass, MyClass()]
for obj in objs:
    print(type(obj).__name__, '   ', sys.getsizeof(obj))


