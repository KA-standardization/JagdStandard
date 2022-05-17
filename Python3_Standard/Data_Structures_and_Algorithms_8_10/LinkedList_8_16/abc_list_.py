from interface_list import InterfaceList


class AbstractList(InterfaceList):
    # _size = 0
    def __init__(self):
        self._size = 0

    def size(self):
        '''
        :return:
        '''
        return self._size

    def is_empty(self):
        '''
        :return:
        '''
        return self._size == 0

    def contains(self, element):
        '''
        :param element:
        :return:
        '''
        return self.index_of(element) != self._NOT_FOUND

    def add(self, element):
        '''
        :param element:
        :return:
        '''
        self.insert(self._size, element)

    def out_of_bounds(self, index):
        '''
        :param index:
        :return:
        '''
        raise IndexError('Index: {}, Size: {}'.format(index, self._size))

    def range_check(self, index):
        '''
        :param index:
        :return:
        '''
        if index < 0 or index >= self._size:
            self.out_of_bounds(index)

    def range_check_for_add(self, index):
        '''
        :param index:
        :return:
        '''
        if index < 0 or index > self._size:
            self.out_of_bounds(index)
