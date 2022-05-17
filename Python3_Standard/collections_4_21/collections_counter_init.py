import collections

print(collections.Counter([1, 2, 3, 3, 3, 2, 1, 1, 1]))

c1 = collections.Counter([1, 2, 3, 4])
c2 = collections.Counter([1, 2, 5])

print(c1 + c2)
print(c1 - c2)
print(c1 & c2)
print(c1 | c2)
cc = c1 - c2
for k, v in cc.items():
    print(k, v)
