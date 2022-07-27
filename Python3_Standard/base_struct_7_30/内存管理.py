"""
https://www.evanjones.ca/python-memory.html
https://www.evanjones.ca/python-memory-part2.html
https://www.evanjones.ca/python-memory-part3.html

https://www.evanjones.ca/memoryallocator/
"""

"""
Python 的内存分配器，称为 pymalloc，由 Vladimir Marangozov 编写，最初是 Python 2.1 和 2.2 的实验性功能，在 2.3 中默认启用之前。
Python 使用了很多经常被创建和销毁的小对象，并且为每个对象调用malloc()and会带来很大的开销。free()为了避免这种情况，
pymalloc 以 256 kB 的块分配内存，称为 arenas。arena 被划分为 4 kB 的池，这些池又被细分为固定大小的块
"""