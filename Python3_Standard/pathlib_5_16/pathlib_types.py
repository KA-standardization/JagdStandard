import os
import pathlib
import itertools

root = pathlib.Path('../text_files')

if root.exists():
    for f in root.iterdir():
        f.unlink()
else:
    root.mkdir()

(root / 'file').write_text('nothing is love', encoding='utf-8')
(root / 'symlink').symlink_to('file')
os.mkfifo(str(root / 'fifo'))

to_scan = itertools.chain(root.iterdir(), [pathlib.Path('/dev/disk0'), pathlib.Path('/dev/console')])

hfmt = '{:18s}' + (' {:>5}' * 6)
print(hfmt.format('Name', 'File', 'Dir', 'Link', 'FIFO', 'Block', 'Character'))
print()

fmt = '{:20s}  ' + ('{!r:>5} ' * 6)

for f in to_scan:
    print(fmt.format(str(f), f.is_file(), f.is_dir(), f.is_symlink(), f.is_fifo(), f.is_block_device(),
                     f.is_char_device()))

