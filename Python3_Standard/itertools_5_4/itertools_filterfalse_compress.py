import itertools


def should_drop(x):
    print('xx--> {}'.format(x))
    return x < 1


for i in filter(should_drop, [-1, -2, 0, 1, 2, -3]):
    print(i)

print('=' * 88)
for i in itertools.filterfalse(should_drop, [-1, -2, 0, 1, 2, -3]):
    print(i)

print('=' * 88)
data = range(1, 10)
flag = itertools.cycle([True, False, False])

for i in itertools.compress(data, flag):
    print(i)
