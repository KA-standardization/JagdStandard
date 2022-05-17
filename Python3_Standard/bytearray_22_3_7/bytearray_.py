# -*- coding: utf-8 -*-
# @Time : 2022/3/7 18:17 
# @Author : Fisher


# 利用这一技术，很容易预先分配一个缓冲区（就像在C语言中一样，以减少对malloc()的调用次数）并在需要时进行填充。
ba = bytearray(8)
print(ba)
with open('./test', 'rb') as s:
    s.readinto(ba)
print(ba)

# 使用memoryview甚至可以在内存区域的任何点放入数据。
ba_at_last = memoryview(ba)[7:]
with open('./test2', 'rb') as s2:
    s2.readinto(ba_at_last)
print(ba)
print(ba.decode())
