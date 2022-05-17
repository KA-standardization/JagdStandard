import abc


class Base(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def factory(cls, *args):
        return cls()

    @staticmethod
    @abc.abstractmethod
    def const_behavior():
        return 'drill'


class Impeleteation(Base):

    def do_some(self):
        print('do some')

    @classmethod
    def factory(cls, *args):
        obj = cls(*args)
        obj.do_some()
        return obj

    @staticmethod
    def const_behavior():
        return 'nothing is true'


i = Impeleteation()

i.factory()
Impeleteation.factory()

print(i.const_behavior())
