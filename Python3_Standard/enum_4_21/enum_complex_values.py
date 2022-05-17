import enum


class DictEnum(enum.Enum):
    a = {
        'v1': 1,
        'v2': ['a', 'b']
    }
    b = {
        'v1': 2,
        'v2': ['c']
    }
    c = {
        'v1': 3,
        'v2': ['a']
    }

    def __init__(self, vals):
        self.v1 = vals['v1']
        self.v2 = vals['v2']

    def can_transition(self, new_state):
        return new_state.name in self.v2


print(DictEnum.a)
print(DictEnum.a.value)
print('============')
print(DictEnum.a.v2)
print(DictEnum.a.can_transition(DictEnum.b))
print(DictEnum.b.name)
print(type(DictEnum.a.v2))
