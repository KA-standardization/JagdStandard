import functools
import inspect

from pprint import pprint


@functools.total_ordering
class MyObj:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print('__eq__ {} {}'.format(self.val, other.val))
        return self.val == other.val

    def __gt__(self, other):
        print('__gt__ {} {}'.format(self.val, other.val))
        return self.val > other.val


print('Method')
pprint(inspect.getmembers(MyObj, inspect.isfunction))

a = MyObj(1)
b = MyObj(2)

print('Comparisons')
for expr in ['a<b', 'a<=b', 'a==b', 'a>=b', 'a>b']:
    res = eval(expr)
    print('res of {} : {}'.format(expr, res))
