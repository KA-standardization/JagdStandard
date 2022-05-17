import collections


def default_fill():
    return '456'


c = {'a': 1, 'b': 2}
d = collections.defaultdict(default_fill, c)
print(d)
print(d['a'])
print(d['b'])
print(d['c'])
