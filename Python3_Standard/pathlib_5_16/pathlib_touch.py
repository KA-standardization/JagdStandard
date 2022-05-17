import time
import pathlib

p = pathlib.Path('touched')
if p.exists():
    print('exists')
else:
    p.touch()

start = p.stat()

p.touch()
end = p.stat()

print(time.ctime(start.st_mtime))
print(time.ctime(end.st_mtime))
