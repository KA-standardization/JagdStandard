from memprof import *


@memprof
def foo():
    for i in range(100):
        print('aaaaa{}'.format(i))


if __name__ == '__main__':
    foo()
