import shelve

with shelve.open('test_shelve.db') as s:
    s['key2'] = {
        'a': 'A',
        'b': 'B',
        'c': [1, 2, 3]
    }

with shelve.open('test_shelve.db') as s1:
    existing = s1['key1']

print(existing)
