# -*- coding:utf-8 -*-
import sys
import time
import random
from ctypes import cdll

if sys.platform == 'win32':
    libc = cdll.msvcrt
else:
    libc = cdll.LoadLibrary('libc.so.6')

start = time.clock()
r = [random.randrange(1, 100) for _ in range(100000)]
print("py-->{}".format(time.clock() - start))
# print(r)

start = time.clock()
r2 = [(libc.rand()) for _ in range(100000)]
print("c-->{}".format(time.clock() - start))
# print(r2)
