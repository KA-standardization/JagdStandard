import pathlib

p = pathlib.Path(__file__)
print(p.owner())
print(p.group())
