import abc
from abc_base import PluginBase
import abc_register
import abc_subclass


class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.writer(data)


if __name__ == '__main__':
    print(issubclass(SubclassImplementation, PluginBase))
    print(isinstance(SubclassImplementation(), PluginBase))

    for subclass in PluginBase.__subclasses__():
        print(subclass.__name__)
