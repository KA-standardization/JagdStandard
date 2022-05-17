import inspect
from pprint import pprint

import inspect_example

for name, data in inspect.getmembers(inspect_example):
    if name.startswith('__'):
        continue
    print('{}: {!r}'.format(name, data))

print('=' * 88)

for name, data in inspect.getmembers(inspect_example, inspect.isclass):
    print('{} : {!r}'.format(name, data))

print('=' * 88)
pprint(inspect.getmembers(inspect_example.A), width=65)
print('=' * 88)
pprint(inspect.getmembers(inspect_example.A, inspect.isfunction), width=50)
print('=' * 88)
pprint(inspect.getmembers(inspect_example.B, inspect.isfunction), width=70)
print('=' * 88)
# 检查实力
a = inspect_example.A(name='Fisher')
pprint(inspect.getmembers(a, inspect.ismethod))
print('=' * 88)
print(inspect_example.B.__doc__)
print(inspect.getdoc(inspect_example.B))
print('=' * 88)
print(inspect.getcomments(inspect_example.B.do_something))
print(inspect.getcomments(inspect_example))
print('=' * 88)
# IOError
print(inspect.getsource(inspect_example.A))
print('=' * 88)
print(inspect.getsource(inspect_example.A.get_name))
print('='*88)
pprint(inspect.getsourcelines(inspect_example.A.get_name))

