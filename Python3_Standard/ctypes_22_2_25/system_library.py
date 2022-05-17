# -*- coding:utf-8 -*-
import sys
import time
import random
import ctypes as cs
from ctypes import cdll

if sys.platform == 'win32':
    libc = cdll.msvcrt
else:
    libc = cdll.LoadLibrary('libc.so.6')

# libc.printf(cs.c_wchar_p("hello"))
# None 作为空指针
print(libc.time(None))
print(cs.c_int(42))
cw = cs.c_wchar_p("hello")
print(cw, cw.value)
p = cs.create_string_buffer(b"buch", 10)
print(p)
print(p.raw)
libc.printf(b"S %s", b'hello')
