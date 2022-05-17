import itertools


def should_drop(x):
    print('xx--{}'.format(x))
    return x < 1


for i in itertools.dropwhile(should_drop, [-1, -2, 0, 1, 2, -3]):
    print(i)

print('=' * 88)
for i in itertools.takewhile(should_drop, [-1, -2, 0, 1, 2, -3]):
    print(i)
