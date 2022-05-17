import itertools

for i in zip(range(5), itertools.cycle(['1', '2'])):
    print(i)

print('=' * 88)
for i in zip(itertools.count(), itertools.repeat('abc', 5)):
    print(i)

print('=' * 88)
for i in map(lambda x, y: (x, y, x * y), itertools.repeat(2), range(5)):
    print(i)
