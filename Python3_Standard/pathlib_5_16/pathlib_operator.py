import pathlib

usr = pathlib.PurePosixPath('python_codes')
print(usr)

usr_local = usr / 'local'
print(usr_local)

usr_share = usr / pathlib.PurePosixPath('share')
print(usr_share)

root = usr / '..'
print(root)

etc = root / '/etc/'
print(etc)

print('=' * 88)
usr_local = pathlib.Path('/usr/local')
print(usr_local)
share = usr_local / '..' / 'share'
print(share)
print(share.resolve())

print('=' * 88)
root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_local = root.joinpath(*subdirs)
print(usr_local)

print('=' * 88)
ind = pathlib.PurePosixPath('source/pathlib/index.rst')
print(ind)
py = ind.with_name('hello.py')
print(py)
pyc = py.with_suffix('.pyc')
print(pyc)
