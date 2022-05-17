import pathlib

p = pathlib.Path('example_link')
p.symlink_to('index.rst')
# 'index.rst' -> 'example_link'
print(p.resolve().name)
