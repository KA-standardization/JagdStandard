import itertools

r = itertools.islice(itertools.count(), 5)

d1, d2 = itertools.tee(r)
print('d1--', list(d1))
print('d2--', list(d2))
