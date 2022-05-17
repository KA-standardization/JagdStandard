import functools


@functools.singledispatch
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))


@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int {}'.format(arg))


@myfunc.register(list)
def myfunc_list(arg):
    for item in arg:
        print('list {}'.format(item))


@myfunc.register(float)
def myfunc_float(arg):
    print('float {}'.format(arg))


myfunc('abcde')
myfunc(123)
myfunc(2.3)
myfunc([1, 2, 3])
