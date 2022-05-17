import pathlib

p = pathlib.Path('example_dir')

try:
    p.mkdir()
except FileExistsError as err:
    print(err)
