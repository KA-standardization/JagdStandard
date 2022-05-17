import collections

a = {'a': 'A', 'b': 'B'}
b = {'a': 1, 'c': 'C'}
m = collections.ChainMap(a, b)

print(m['a'])
print(m['b'])
print(m['c'])

for k, v in m.items():
    print(k, '-->', v)

print(m.maps)
m.maps = list(reversed(m.maps))

print(m['a'])
print(b['a'])
m['a'] = 100
print(m['a'])
print(b['a'])

c = {'e': 'E'}
m2 = m.new_child(c)

for k, v in m2.items():
    print(k, '-->', v)

print('==================')
print(b['c'])
m2['c'] = 101
print(b['c'])
