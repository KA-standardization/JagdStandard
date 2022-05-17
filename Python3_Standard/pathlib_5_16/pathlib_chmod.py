import os
import stat
import pathlib

f = pathlib.Path('path_chmod.txt')
if f.exists():
    f.unlink()

f.write_text('contents')

existing_permissions = stat.S_IMODE(f.stat().st_mode)
print('Before {:o}'.format(existing_permissions))

if not (existing_permissions & os.X_OK):
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    new_permissions = existing_permissions ^ stat.S_IXUSR

f.chmod(new_permissions)
after_permissions = stat.S_IMODE(f.stat().st_mode)
print(after_permissions)
