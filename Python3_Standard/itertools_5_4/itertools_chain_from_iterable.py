import itertools

a = [1, 2, 3]
b = [4, 5, 6]
d = [1, 4, 5]
c = itertools.chain(a, b, d)
print(list(c))

a1 = {'1': 1, '2': 2}
b1 = {'3': 3}
c1 = itertools.chain(a1.items(), b1.items())
print(list(c1))


def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c', 'd']


for i in itertools.chain(make_iterables_to_chain()):
    print(i)

for i in itertools.chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')
