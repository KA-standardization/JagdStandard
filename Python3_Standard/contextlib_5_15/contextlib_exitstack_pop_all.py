import contextlib


class Tracker:
    def __init__(self, i):
        self.i = i

    def msg(self, s):
        print('{} ({}) {}'.format(self.__class__.__name__, self.i, s))

    def __enter__(self):
        self.msg('entering')


class HandleError(Tracker):
    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('handling exception {!r}'.format(exc_details[1]))
        self.msg('exiting {}'.format(received_exc))
        return received_exc


class PassError(Tracker):
    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('passError {!r}'.format(exc_details[1]))
        self.msg('exiting')
        return False


class ErrorOnExit(Tracker):
    def __exit__(self, *exc_details):
        self.msg('throwing error')
        raise RuntimeError('from {}'.format(self.i))


class ErrorOnEnter(Tracker):
    def __enter__(self):
        self.msg('throwing error on enter')
        raise RuntimeError('from {}'.format(self.i))

    def __exit__(self, *exc_details):
        self.msg('exiting')


def variable_stack(contexts):
    with contextlib.ExitStack() as stack:
        for c in contexts:
            stack.enter_context(c)

        return stack.pop_all().close
    return None


print('No errors===========')
cleaner = variable_stack([HandleError(1), HandleError(2)])
cleaner()

print('handled error=======')
try:
    cleaner = variable_stack([HandleError(1), ErrorOnEnter(2)])
except RuntimeError as e:
    print('caught error {}'.format(e))
else:
    if cleaner is not None:
        cleaner()
    else:
        print('no cleaner')

print('unhandled error=====')
try:
    cleaner=variable_stack([PassError(1),ErrorOnEnter(2)])
except RuntimeError as e:
    print('caught {}'.format(e))
else:
    if cleaner is not None:
        cleaner()
    else:
        print('no cleaner')