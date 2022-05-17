# -*- coding: utf-8 -*-
# 在Python中可以使用实现了缓冲区协议的对象。PEP 3118 https://www.python.org/dev/peps/pep-3118/dev/peps/pep-3118/）
# 定义了缓冲区协议，其中解释了用于为不同数据类型（如字符串类型）提供该协议的C API。


# s = b"特别是，建议取消 API 的字符缓冲区部分，并重新设计多段部分，同时允许共享跨步内存。此外，新的缓冲区接口将允许共享内存的任何多维性质以及内存包含的数据格式"
s = b"abcdefg"

# 实现了缓冲区协议的对象,可以使用其memoryview类的构建函数去构造一个新的memoryview对象,它引用原始的对象内存
view = memoryview(s)
print(view[0])
limited = view[1:3]
print(limited)
print(bytes(limited))
"""
TypeError: cannot modify read-only memory
view[-1] = 46
print(view[-1])
"""
