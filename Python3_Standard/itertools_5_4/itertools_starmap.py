import itertools


def mult_2(x):
    return x * 2


for i in map(mult_2, range(5)):
    print(i)


def multiply(x, y):
    return (x, y, x * y)


# *iterables
for i in map(multiply, range(5), range(6, 11)):
    print('{}*{}={}'.format(*i))

print('=' * 88)
values = [(2, 3, 4), (5, 6, 7), (7, 8, 9)]
# iterables
for i in itertools.starmap(lambda x, y, z: (x, y, z, x * y + z), values):
    print('{}*{}+{}={}'.format(*i))
