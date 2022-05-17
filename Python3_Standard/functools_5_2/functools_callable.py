import functools


class MyClass:
    "修辞立其诚"

    a = 11
    b = 12

    def __call__(self, e, f=6, *args, **kwargs):
        print('  called object with', (self, e, f))
        return self.a


def show_details(name, f):
    print('{}'.format(name))
    print('object', f)
    print('__name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('no __name__')
    print('__doc__', repr(f.__doc__))
    return


m = MyClass()
show_details('instance', m)
m('e haha')
print('=' * 88)

p = functools.partial(m, e='default for e', f=8)
functools.update_wrapper(p, m)
show_details('instance wrapper', p)
print(p.__call__())
p()
