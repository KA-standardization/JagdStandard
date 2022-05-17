import math as mh


def fib(n):
    c = mh.sqrt(5)
    return int((mh.pow((1 + c) / 2, n) - mh.pow((1 - c) / 2, n)) / c)


if __name__ == '__main__':
    print(fib(64))
