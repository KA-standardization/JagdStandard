import functools


def myfunc(a, b=2):
    print('called myfunc with', (a.b))


def show_details(name, f):
    print('{}: '.format(name))
    print('object', f)
    print('__name__', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('no __name__')
    print('__doc__ 1111', f.__doc__)
    print('__doc__ 2222', repr(f.__doc__))
    print()


show_details('myfunc', myfunc)

p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)

print('=' * 88)

print('Updating wrapper:')
print('  assign', functools.WRAPPER_ASSIGNMENTS)
print('  update', functools.WRAPPER_UPDATES)
print()

functools.update_wrapper(p1, myfunc)
show_details('updating wrapper', p1)
