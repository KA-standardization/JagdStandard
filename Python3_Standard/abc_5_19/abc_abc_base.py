import abc


class PluginBase2(abc.ABC):

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
