import enum
import inspect


class MemberNum(enum.Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    f = 1


print(MemberNum.a == MemberNum.b)

for ele in MemberNum:
    print('{:15}-->{}'.format(ele.name, ele.value))


def is_enum(data):
    return isinstance(data, MemberNum)


for k, v in inspect.getmembers(MemberNum, is_enum):
    tmp = "MemberNum." + k
    print(eval(tmp).value)


class MemberNum2(enum.IntEnum):
    a = 1
    b = 2
    c = 3
    d = 4


print(MemberNum2.a < MemberNum2.b)


@enum.unique
class MemberNum3(enum.Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    # f = 1
