import itertools
import pprint

a = ('a', 'b', 'c')
b = ('q', 'w', 'e')
c = list(itertools.product(itertools.chain(range(2, 11), a), b))
print(c)

for card in c:
    print('{:>2}{}'.format(*card), end=' ')
    if card[1] == b[-1]:
        print()

print('=' * 88)
print(list(itertools.product(range(3), repeat=2)))
