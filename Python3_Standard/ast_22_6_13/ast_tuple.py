import ast
import json


# s = ("abc", 123, "true")
# # s2 = str(s)
# s2 = repr(s)
# s3 = ast.literal_eval(s2)
# print(type(s3), s3)

def foo():
    print("foo()")


def bar():
    print("bar")


def default():
    print("default")


register = {
    'foo': foo.__code__.co_name,
    'bar': bar.__code__.co_name,
}

if __name__ == '__main__':
    # print(register.__repr__())
    #
    # print(foo.__code__.co_name)
    # repr_register = repr(register)
    repr_register = json.dumps(register)


    def m(key):
        funcs = ast.literal_eval(repr_register)
        # ast.literal_eval(funcs.get(key))
        eval(funcs.get(key))()


    m('foo')

