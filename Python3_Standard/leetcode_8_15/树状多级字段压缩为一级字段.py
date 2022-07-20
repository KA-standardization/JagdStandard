# 给定任意dict数据，请实现方法提取数据字典，即将树状多级字段压缩为一级字段（格式：xx.yy.zz...)并提取其类型。
#
# 要求：
# 1. 可上网查资料，但不要直接粘贴
# 2. 代码结构清晰，执行结果正确
import re
import json


def solution(data: dict):
    # 在这⾥写代码，可自行添加更多方法
    all = dict()

    def foo(data: dict, pre_key=None):
        tmp = dict()
        if pre_key:
            for key in data.keys():
                tmp[pre_key + '.' + key] = type(data[key])
                if isinstance(data[key], dict):
                    foo(data[key], pre_key + '.' + key)
                elif type(data[key]) in (list, tuple):
                    for item in data[key]:
                        if type(item) == dict:
                            for k in item.keys():
                                tmp[pre_key + '.' + key + '.' + k] = type(item[k])
        else:
            for key in data.keys():
                tmp[key] = type(data[key])
                if isinstance(data[key], dict):
                    foo(data[key], key)
                elif type(data[key]) in (list, tuple):
                    for item in data[key]:
                        if type(item) == dict:
                            for k in item.keys():
                                tmp[key + '.' + k] = type(item[k])
        all.update(tmp)

    foo(data)
    a = {kk: re.findall(re.compile("'(.*)'"), str(vv))[0] for kk, vv in all.items()}
    return {kkk: a[kkk] for kkk in sorted(a)}


def main():
    # 测试数据1 - 较简单，方便测试
    test1 = {
        "a": 1,
        "b": {
            "c": "test"
        }
    }

    # 期望结果1
    result1 = {
        "a": "int",
        "b": "dict",
        "b.c": "str"
    }

    # 提取数据字典并校验结果
    ret1 = solution(test1)
    print('ret1 =', json.dumps(ret1, indent=4))
    assert ret1 == result1, 'test1结果不正确'

    # 测试数据2 - 略复杂，有数组嵌套
    # 假定数组内元素类型是相同的，不考虑不相同的情况
    test2 = {
        "x": {
            "x1": "aa",
            "x2": [11, 22],  # 注意元素为基本类型
            "x3": {
                "m": {
                    'n': 123
                },
            }
        },
        "y": [  # 注意元素为复杂类型
            {
                "p": 1,
                "q": 'aa',
            },
            {
                "p": 3,
                "q": "bb"
            }
        ],
        "z": True
    }

    # 期望结果2
    result2 = {
        "x": "dict",
        "x.x1": "str",
        "x.x2": "list",
        "x.x3": "dict",
        "x.x3.m": "dict",
        "x.x3.m.n": "int",
        "y": "list",
        "y.p": "int",
        "y.q": "str",
        "z": "bool"
    }

    # 提取数据字典并校验结果
    ret2 = solution(test2)
    print('ret2 =', json.dumps(ret2, indent=4))
    assert ret2 == result2, 'test2结果不正确'


if __name__ == "__main__":
    main()
    # test2 = {
    #     "x": {
    #         "x1": "aa",
    #         "x2": [11, 22],  # 注意元素为基本类型
    #         "x3": {
    #             "m": {
    #                 'n': 123
    #             },
    #         }
    #     },
    #     "y": [  # 注意元素为复杂类型
    #         {
    #             "p": 1,
    #             "q": 'aa',
    #         },
    #         {
    #             "p": 3,
    #             "q": "bb"
    #         }
    #     ],
    #     "z": True
    # }
    # all = dict()
    #
    #
    # def foo(data: dict, pre_key=None):
    #     tmp = dict()
    #     if pre_key:
    #         for key in data.keys():
    #             tmp[pre_key + '.' + key] = type(data[key])
    #             if isinstance(data[key], dict):
    #                 foo(data[key], pre_key + '.' + key)
    #             elif type(data[key]) in (list, tuple):
    #                 for item in data[key]:
    #                     if type(item) == dict:
    #                         for k in item.keys():
    #                             tmp[pre_key + '.' + key + '.' + k] = type(item[k])
    #     else:
    #         for key in data.keys():
    #             tmp[key] = type(data[key])
    #             if isinstance(data[key], dict):
    #                 foo(data[key], key)
    #             elif type(data[key]) in (list, tuple):
    #                 for item in data[key]:
    #                     if type(item) == dict:
    #                         print(11111)
    #                         for k in item.keys():
    #                             tmp[key + '.' + k] = type(item[k])
    #     all.update(tmp)
    #
    #
    # foo(test2)
    #
    # print(all)
    # a = {kk: re.findall(re.compile("'(.*)'"), str(vv))[0] for kk, vv in all.items()}
    # b = {kkk: a[kkk] for kkk in sorted(a)}
    # print(b)
