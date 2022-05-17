import shelve
import pprint

with shelve.open('test_shelve.db', writeback=True) as s:
    print(s['key1'])
    s['key1']['new'] = '被抛入到自由之中,存在以某种方式源自将来'

with shelve.open('test_shelve.db', flag='r') as s1:
    pprint.pprint(s1['key1'])
    print(list(s1.items()))
