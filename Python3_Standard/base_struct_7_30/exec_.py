# x = 1
# exec("x=2", globals())
# print(x)

def foo():
    x = 1
    print("g-->", globals())
    print("l-->", locals())
    exec("x=2")
    print(x)


foo()
