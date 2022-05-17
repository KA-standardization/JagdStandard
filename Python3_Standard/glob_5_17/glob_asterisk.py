import glob
import pathlib

# p = pathlib.Path('dir')
# if not p.exists():
#     p.mkdir()
# f = pathlib.Path('dir/file.txt')
# if not f.exists():
#     f.touch()

for name in sorted(glob.glob('../../python3_standard/*')):
    print(name)

print('=' * 88)
for name in sorted(glob.glob('../../python3_standard/array_4_25/*')):
    print(name)

print('=' * 88)
for name in sorted(glob.glob('../../python3_standard/*/*')):
    print(name)

print('=' * 88)
for name in sorted(glob.glob('../../python3_standard/a?ray*/*')):
    print(name)

print('=' * 88)
for name in sorted(glob.glob('../../python3_standard/*[0-9]')):
    print(name)

print('=' * 88)
specials = '?*['
for char in specials:
    pattern = '../../python3/*' + glob.escape(char) + '.txt'
    for name in sorted(glob.glob(pattern)):
        print(name)
