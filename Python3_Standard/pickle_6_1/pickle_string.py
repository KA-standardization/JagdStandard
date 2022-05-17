import pickle
import pprint

data = [{'a': 'A', 'b': 2, 'c': 3.0}]
pprint.pprint(data)
data_string = pickle.dumps(data)
print('PICKLE: {!r}'.format(data_string))

print('=' * 88)

data2 = pickle.loads(data_string)
pprint.pprint(data2)
