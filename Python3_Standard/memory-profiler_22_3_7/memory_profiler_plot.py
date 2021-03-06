# -*- coding: utf-8 -*-
# @Time : 2022/3/7 17:03 
# @Author : Fisher
"""
Plot memory usage of a numeric computation using numpy and scipy
"""
import pylab as pl
import numpy as np
from memory_profiler import memory_usage
from scipy import linalg

if __name__ == '__main__':
    X = np.random.randn(1000, 1000)

    mem = memory_usage((linalg.qr, (X,)))
    x = np.linspace(0, len(mem) * .1, len(mem))

    p = pl.fill_between(x, mem)

    pl.xlabel('time')
    pl.ylabel('Memory consumption (in MB)')
    pl.show()
