import collections

a = {1: 1, 2: 2, 3: 3}
d = collections.OrderedDict(a)

print(d)
for k, v in d.items():
    print(k, v)

d.move_to_end(1)
print(d)
d.move_to_end(3, last=False)
print(d)
