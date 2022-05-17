import collections

Foo = collections.namedtuple('bar', ['x', 'y'])
print(Foo(1, 2))
print(Foo(3, 4).x)
print(list(Foo(5, 6)))
"""
用 namedtuple 构建的类的实例所消耗的内存跟元组是一样的， 因为字段名都被存在对应的类里面。 
这个实例跟普通的对象实例比起来也要小一些， 因为 Python 不会用 __dict__ 来存放这些实例的属性。
"""
C = collections.namedtuple('C', 'name age infos')
lili = C('Lee', 28, ("A", "B", "C"))
print(lili)
"""
具名元组还有一些自己专有的属性。 示例 2-10 中就展示了几个最有用的：_fields 类属性、 类方法 _make( iterable) 和实例方法 _asdict()。
"""
print(C._fields)
xm = ('Xi', 33, ("D", "F", "G"))
x = C._make(xm)
print(x)
for k, v in x._asdict().items():
    print("key: {}, val: {}".format(k, v))
