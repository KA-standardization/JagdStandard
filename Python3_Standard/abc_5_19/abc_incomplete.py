import abc
from abc_base import PluginBase
from abc_abc_base import PluginBase2


@PluginBase.register
class Incomplete1:

    def save(self, output, data):
        return output.writer(data)


@PluginBase2.register
class Incomplete2:

    def save(self, output, data):
        return output.write(data)


class Incomplete3(PluginBase):

    def save(self, output, data):
        return output.writer(data)


class Incomplete4(PluginBase2):

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print(issubclass(Incomplete2, PluginBase2))
    print(isinstance(Incomplete2(), PluginBase2))
    print('=' * 88)
    print(issubclass(Incomplete1, PluginBase))
    print(isinstance(Incomplete1(), PluginBase))
    print('=' * 88)
    print(issubclass(Incomplete3, PluginBase))
    try:
        print(isinstance(Incomplete3(), PluginBase))
    except TypeError as err:
        print(err)
    print('=' * 88)
    print(issubclass(Incomplete4, PluginBase2))
    try:
        print(isinstance(Incomplete4(), PluginBase2))
    except TypeError as err:
        print(err)
