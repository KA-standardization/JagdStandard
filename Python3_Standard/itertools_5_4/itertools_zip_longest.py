import itertools

for i in zip([1, 2, 3], [4, 5, 6, 7]):
    print(i, end=' ')

print()
print('=' * 88)
for j in itertools.zip_longest([1, 2, 3], [4, 5, 6, 7], fillvalue='Fisher'):
    print(j, end=' ')
