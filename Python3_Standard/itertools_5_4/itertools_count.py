import itertools
import fractions

for i in zip(itertools.count(10), ['1', '2', '3', '4']):
    print(i)

print('=' * 88)
start = fractions.Fraction(1, 3)
step = fractions.Fraction(1, 3)
for i in zip(itertools.count(start, step), ['1', '2', '3']):
    print('{}: {}'.format(*i))
