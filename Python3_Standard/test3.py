# -*- coding: utf-8 -*-
# @Time : 2022/3/9 12:38 
# @Author : Fisher

def foo():
    print('111111111')
    print('222222222')
    yield {"a": 11}
    print('333333333')
    print('444444444')


if __name__ == '__main__':
    f = foo()
    next(f)
    try:
        next(f)
    except:
        pass
