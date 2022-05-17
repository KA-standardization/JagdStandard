import abc


class InterfaceList(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        self._NOT_FOUND = -1

    @abc.abstractmethod
    def clear(self):
        '''
        :return:
        '''

    @abc.abstractmethod
    def size(self):
        '''
        :return:
        '''

    @abc.abstractmethod
    def is_empty(self):
        '''
        :return:
        '''

    @abc.abstractmethod
    def contains(self, element):
        '''
        :param element:
        :return:
        '''

    @abc.abstractmethod
    def add(self, element):
        '''
        :param element:
        :return:
        '''

    @abc.abstractmethod
    def insert(self, index, element):
        '''
        :param index:
        :param element:
        :return:
        '''

    @abc.abstractmethod
    def get(self, index):
        '''
        :param index:
        :return:
        '''

    @abc.abstractmethod
    def set(self, index, element):
        '''
        :param index:
        :param element:
        :return:
        '''

    @abc.abstractmethod
    def remove(self, index):
        '''
        :param index:
        :return:
        '''

    @abc.abstractmethod
    def index_of(self, element):
        '''
        :param element:
        :return:
        '''
