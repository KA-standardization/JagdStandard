import functools


def show_details(name, f):
    "show_details"
    print('{}'.format(name))
    print(' object', f)
    print(' __name__', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('no __name__')

    print('__doc__ {}'.format(repr(f.__doc__)))


def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print('decorated:', (a, b))
        print('  ', end=' ')
        return f(a, b=b)

    return decorated


def myfunc(a, b=2):
    'myfunc  ><'
    print(' myfunc', (a, b))
    return


show_details('myfunc', myfunc)
myfunc('unwrapper default b')
myfunc('unwrapper,passing b', 3)
print('=' * 88)

wrapper_myfunc = simple_decorator(myfunc)
show_details('wrapper myfunc', wrapper_myfunc)
wrapper_myfunc()
wrapper_myfunc('args to wrapped', 4)
print('=' * 88)


@simple_decorator
def decorated_myfunc(a, b):
    '''
    decorated myfunc
    :param a:
    :param b:
    :return:
    '''
    myfunc(a, b)
    return

show_details('decorated myfunc', decorated_myfunc)
decorated_myfunc()
decorated_myfunc('args to decorated', 4)
