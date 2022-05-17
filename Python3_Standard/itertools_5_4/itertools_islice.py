import itertools

for i in itertools.islice(range(100), 0, 100, 10):
    print(i, end=' ')

print()
print('=' * 88)
for j in itertools.islice(range(100), 5):
    print(j, end=' ')

print()
print('=' * 88)
a = [1, 2, 3, 4, 5, 6, 7, 8]

print(a[slice(0, 5, 2)])
