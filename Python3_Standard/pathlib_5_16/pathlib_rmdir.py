import pathlib

p = pathlib.Path('example_dir')
if not p.exists():
    p.mkdir()

p.rmdir()
