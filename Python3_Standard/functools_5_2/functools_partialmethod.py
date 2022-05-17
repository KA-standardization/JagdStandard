import functools


def standalone(self, a=1, b=2):
    "弗洛伊德"
    print('  called standalone with', (self, a, b))


class MyClass:
    "myclass  ><"

    def __init__(self):
        self.attr = 'instance attribute'

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)


m = MyClass()
print('standalone')
standalone(None)
print('=' * 88)

print('method as partialmethod')
m.method1()
print('=' * 88)

print('method as partial')
try:
    m.method2()
except TypeError as err:
    print('Error {}'.format(err))

print('=' * 88)

print('method as partial in m')
try:
    m.method2(m)
except TypeError as err:
    print('Error {}'.format(err))
