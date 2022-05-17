# import weakref
#
#
# class A:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __call__(self, func):
#         return func(self.a, self.b)
#
#     def __del__(self):
#         print('DEL: args {self.a} {self.b}'.format(self=self))
#
#
# def foo(a, b):
#     print(a + b)
#
#
# a = A(10, 20)
# # a(foo)
#
# r = weakref.ref(a)
# r()(foo)
# del a
# print(r())


# r = weakref.proxy(a)
# r(foo)

# print(callable(a))
#
# a = 11111
# b = 12111
#
# '''
# 10 1011 0110 0111
# 10 1111 0100 1111
# 10 1111 0110 1111
# '''
#
# c = b | a
# print(c)
#
# k = 22
# j = 0x7
#
# '''
# 1 0110
# 0 0111
# 0 0110
# '''
#
# l = k & j
# print(l)
import random


def foo():
    i = random.randint(5, 10)
    i += 1
    print(i)
    return i


while (foo() < 10):
    pass
# process chain process fan




