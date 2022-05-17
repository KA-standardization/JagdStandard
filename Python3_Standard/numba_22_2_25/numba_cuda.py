import time
from numba import jit, int64
from numba import cuda


@cuda.jit
def foo(t):
    for i in range(100000000):
        t[i] = i + 10
    for i in range(100000000):
        t[i] = t[i] - i


def bar():
    total = 0
    for i in range(100000000):
        total += i + 10
    for i in range(100000000):
        total -= i
    return total


if __name__ == '__main__':
    t = 100000000
    g_t = cuda.device_array(t)
    start = time.time()
    foo[16, 128](g_t)
    end = time.time()
    cuda.synchronize()
    print("jit-end {}, {}".format(end - start, sum(g_t.copy_to_host())))
    cuda.close()

    start = time.time()
    total = bar()
    end = time.time()
    print("py-end {}, {}".format(end - start, total))
