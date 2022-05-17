# -*- coding:utf-8 -*-
# gcc -shared -o test.so -fPIC test.c
import time
import ctypes

f = ctypes.CDLL('./test.so').foo

start = time.clock()
num_c = [x for x in range(1000000) if f(x)]
print("c-->{}".format(time.clock() - start))
print(num_c)
