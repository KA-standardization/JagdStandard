import functools


class MyObj:

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'MyObj {}'.format(self.val)


def compare_obj(a, b):
    """
    Old-style compare function
    :param a:
    :param b:
    :return:
    """
    print('comparing {} and {}'.format(a, b))
    if a.val < b.val:
        return -1

    elif a.val > b.val:
        return 1

    return 0


get_key = functools.cmp_to_key(compare_obj)


def get_key_wrapper(o):
    """
    :param o:
    :return:
    """
    new_key = get_key(o)
    print('key_wrapper {} --> {!r}'.format(o, new_key))
    return new_key


objs = [MyObj(x) for x in range(5, 0, -1)]

for o in sorted(objs, key=get_key_wrapper):
    print(o)
