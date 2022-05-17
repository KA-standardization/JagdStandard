'''
https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
0 1 2 3 4 5 6 7
0 1 1 2 3 5 8 13
'''


def fib_1(n):
    if n <= 1:
        return n
    return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n):
    if n < 1:
        return n

    num_1 = 0
    num_2 = 1
    for i in range(n - 1):
        num_tmp = num_1 + num_2
        num_1 = num_2
        num_2 = num_tmp
    return num_2


if __name__ == '__main__':
    import time
    n = 64
    start_time = time.time()
    # print(fib_1(n))
    print(fib_2(n))
    end_time = time.time()
    print(end_time - start_time)

