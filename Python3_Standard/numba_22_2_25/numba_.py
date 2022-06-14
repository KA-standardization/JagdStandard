import time
from numba import jit, int32, int64


# pip install numpy
# pip install llvmlite

@jit(int64())
def foo():
    total = 0
    for i in range(100000000):
        total += i + 11
    for i in range(100000000):
        total -= i
    return total


def bar():
    total = 0
    for i in range(100000000):
        total += i + 11
    for i in range(100000000):
        total -= i
    return total


if __name__ == '__main__':
    start = time.time()
    total = foo()
    end = time.time()
    print("jit-end {}, {}".format(end - start, total))

    start = time.time()
    total = bar()
    end = time.time()
    print("py-end {}, {}".format(end - start, total))
