import atexit

print(dir(atexit))


def foo(a):
    print(a, "exit")


x = 1
atexit.register(foo, x)

atexit.unregister(foo)


@atexit.register
def bar():
    print("exit")
