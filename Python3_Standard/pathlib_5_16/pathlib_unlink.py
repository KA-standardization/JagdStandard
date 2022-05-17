import pathlib

p = pathlib.Path('touched')
if not p.exists():
    p.touch()

p.unlink()


