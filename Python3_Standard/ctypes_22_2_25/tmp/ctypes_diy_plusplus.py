# -*- coding:utf-8 -*-
# g++ -shared -o test2.so -fPIC test2.cpp
import time
import ctypes

f = ctypes.CDLL('./test2.so').lambda_mutable

start = time.clock()
print(f())
print("c艹-->{}".format(time.clock() - start))
