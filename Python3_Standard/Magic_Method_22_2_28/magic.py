# -*- coding:utf-8 -*-
import math

dict_a = {"a": 11, "b": 22, "c": 33}
# dunder method
print("mm: dict_a['a']-->{}, tatsache: dict_a.__getitem__('a'))-->{}".format(dict_a['a'], dict_a.__getitem__('a')))

list_a = [1, 2, 3, 4, 5]
for elem in list_a:
    print("list_a: {}".format(elem))

for elem in list_a.__iter__():
    print("list_a.__iter__(): {}".format(elem))

print("mm: repr(list_a)-->{}, tatsache: list_a.__repr__()-->{}".format(repr(list_a), list_a.__repr__()))


########################################################################################################################
class Vector(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        print(abs(self))
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


v = Vector(0, 0)
print(v.__bool__())
