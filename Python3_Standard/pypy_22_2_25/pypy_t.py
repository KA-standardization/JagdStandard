import time

"""
    普通版python编译器: 预处理并转换源代码,然后组合并链接库函数
    JIT编译: 源代码编译是在运行时进行的
        一: 1.首先源代码被翻译成一种中间语言代码,字节码
            2.有了字节码后,开始把它编译并翻译成机器码,但是按需翻译,JIT编译器特性之一就是,只编译需要运行的那部分代码,不是一次全编译
        二: JIT编译器与解释型语言在字节码被解释而不是被编译时的根本差异
            JIT编译器还会缓存已编译的代码
"""


#     pypy -m ensurepip pypy -mpip install xxx
def foo():
    t = 0
    for i in range(100000000):
        t += 1
    print(t)


if __name__ == '__main__':
    start = time.clock()
    foo()
    print("time-->{}".format(time.clock() - start))
