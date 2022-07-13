def foo(x: int):
    import numpy as np
    a = x

    def bar():
        pass

    return bar


c = foo.__code__

print(c.co_code)
print(c.co_name)
print(c.co_flags)
print(c.co_argcount)
print(c.co_stacksize)
print(c.co_varnames)
print(c.co_names)

print(c.co_consts)

