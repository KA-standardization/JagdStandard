import abc


class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        '''
        :param input:
        :return:
        '''

    @abc.abstractmethod
    def save(self, output, data):
        '''
        :param output:
        :param data:
        :return:
        '''
