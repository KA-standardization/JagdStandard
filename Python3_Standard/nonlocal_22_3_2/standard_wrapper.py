# -*- coding: utf-8 -*-
# @Time : 2022/3/3 13:43 
# @Author : Fisher
import html
import numbers
from collections import abc
from functools import singledispatch

"""
Python 内置了三个用于装饰方法的函数：property classmethod staticmethod。
"""
"""
functools.singledispatch装饰器可以把整体方案拆分成多个模块，甚至可以为你无法修改的类提供专门的函数。 
使用@singledispatch装饰的普通函数会变成泛函数（generic function）：根据第一个参数的类型，以不同方式执行相同操作的一组函数。
singledispatch创建一个自定义的htmlize.register装饰器，把多个函数绑在一起组成一个泛函数
"""


@singledispatch
def htmlize(elem):
    content = html.escape(repr(elem))
    return "<pre>{} </pre>".format(content)


@htmlize.register(str)
def a(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return "<pre>{} </pre>".format(content)


@htmlize.register(numbers.Integral)
def a(n):
    return "<pre>{} </pre>".format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def a(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'
