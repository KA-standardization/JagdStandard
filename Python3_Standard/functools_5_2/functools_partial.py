import functools


def myfunc(a, b=2):
    print('called myfunc with', (a, b))


def show_details(name, f, is_partial=False):
    print('{}'.format(name))
    print('object', f)
    if not is_partial:
        print('__name__', f.__name__)
    if is_partial:
        print('     func', f.func)
        print('     args', f.args)
        print('     keywords', f.keywords)
        print('     __doc__', f.__doc__)
    return


show_details('myfunc', myfunc)
myfunc('a', 3)
print('=' * 50)

p1 = functools.partial(myfunc, b=4)
show_details('p1', p1, True)
p1('pass a')
p1('bbb', b=5)
print('=' * 50)

p2 = functools.partial(myfunc, 'de a', b=32)
show_details('p2', p2, True)
p2()
p2(b='o b')
print('=' * 88)
p1('1')
