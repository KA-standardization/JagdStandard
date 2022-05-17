from interface_list import InterfaceList


class AbstractList(InterfaceList):
    _size = 0
    _NOT_FOUND = -1

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def contains(self, element):
        return self.index_of(element) != self._NOT_FOUND

    def add(self, element):
        self.insert(self._size, element)

    def out_of_bounds(self, index):
        raise IndexError('Index: {}, Size: {}'.format(index, self._size))

    def range_check(self, index):
        if index < 0 or index >= self._size: self.out_of_bounds(index)

    def range_check_for_add(self, index):
        if index < 0 or index > self._size: self.out_of_bounds(index)
