import pathlib

p = pathlib.PurePosixPath('/usr/local')
print(p.parts)

print(p.parent)
print(list(p.parents))
print('=' * 88)
p = pathlib.PurePosixPath('./source/pathlib/pathlib_name.py')
print(p)
print(p.name)
print(p.suffix)
print(p.stem)

print('=' * 88)
home = pathlib.Path.home()
print(home)
cwd = pathlib.Path.cwd()
print(cwd)

print('=' * 88)
p = pathlib.Path('..')
for f in p.iterdir():
    print(f)

print('=' * 88)
for f in p.glob('*.py'):
    print(f)

print('=' * 88)
for f in p.rglob('*ma*'):
    print(f)
