import functools


def do_reduce(a, b):
    print('do_reduce {} {}'.format(a, b))
    return a + b


data = range(1, 5)
print(data)
result = functools.reduce(do_reduce, data)
print('res {}'.format(result))

print('=' * 88)
data2 = range(5, 10)
print(data2)
res2 = functools.reduce(do_reduce, data2, 10)
print('res2 {}'.format(res2))
