# -*- coding: utf-8 -*-
# @Time : 2022/3/7 11:27 
# @Author : Fisher
from memory_profiler import profile
"""
pip install memory-profiler
python -m memory_profiler memory_profiler_.py
第一列表示已分析代码的行号，第二列（Mem 使用情况）表示执行该行后 Python 解释器的内存使用情况。第三列（增量）表示当前行相对于最后一行的内存差异。最后一列（行内容）打印已分析的代码。
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    11   19.371 MiB   19.371 MiB           1   @profile
    12                                         def my_func():
    13   27.004 MiB    7.633 MiB           1       a = [1] * (10 ** 6)
    14  179.594 MiB  152.590 MiB           1       b = [2] * (2 * 10 ** 7)
    15   27.004 MiB -152.590 MiB           1       del b
    16   27.004 MiB    0.000 MiB           1       return a

python -m memory_profiler --pdb-mmem=100 memory_profiler_.py
一旦代码在修饰函数中使用超过 100 MB，将运行memory_profiler_.py并进入 pdb 调试器。
"""


# @profile
@profile(precision=8)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    my_func()
