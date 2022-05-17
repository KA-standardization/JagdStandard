import dbm
import shelve

with shelve.open('test_shelve.db', flag='r') as s:
    print(s['key1'])
    try:
        s['key1'] = 'new'
    except dbm.error as err:
        print('ERROR {}'.format(err))
