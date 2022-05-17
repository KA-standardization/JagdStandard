import io
import contextlib
import sys


def misbehaving_function(a):
    sys.stdout.write('{}'.format(a))
    print()
    sys.stderr.write('{}'.format(a))


capture = io.StringIO()

with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
    misbehaving_function(5)

print(capture.getvalue())
