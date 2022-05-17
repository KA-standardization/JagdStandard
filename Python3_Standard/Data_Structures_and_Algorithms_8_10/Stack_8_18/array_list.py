import ctypes

from abc_list import AbstractList


class ArrayList(AbstractList):
    _DEFAULE_CAPACITY = 10

    def __init__(self, capacity):
        self._capacity = capacity if capacity > self._DEFAULE_CAPACITY else self._DEFAULE_CAPACITY
        self._array = self._make_array(self._DEFAULE_CAPACITY)

    def _make_array(self, c):
        '''
        :return: 连续内存
        '''
        return (c * ctypes.py_object)()

    def ensure_capacity(self, capacity):
        old_capacity = len(self._array)
        if old_capacity >= capacity: return
        new_capacity = old_capacity + (old_capacity >> 1)
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        print('{} 扩容: {}'.format(old_capacity, new_capacity))

    def clear(self):
        for i in range(self._size):
            self._array[i] = None

        self._size = 0

    def get(self, index):
        self.range_check(index)
        return self._array[index]

    def set(self, index, element):
        self.range_check(index)
        old = self._array[index]
        self._array[index] = element
        return old

    def insert(self, index, element):
        self.range_check_for_add(index)
        self.ensure_capacity(self._size + 1)
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = element
        self._size += 1

    def remove(self, index):
        self.range_check(index)
        old = self._array[index]
        for i in range(index + 1, self._size):
            self._array[i - 1] = self._array[i]

        self._size -= 1
        self._array[self._size] = None
        return old

    def index_of(self, element):
        if element is None:
            for i in range(self._size):
                if self._array[i] is None: return i
        else:
            for i in range(self._size):
                if element.__eq__(self._array[i]): return i
        return self._NOT_FOUND

    def __str__(self):
        tmp_list = []
        for i in range(self._size):
            tmp_list.append(self._array[i])
        return "size: {}".format(self._size) + repr(tmp_list)

    def __repr__(self):
        pass


if __name__ == '__main__':
    al = ArrayList(5)
    al.add(11)
    al.add(22)
    al.add(33)
    al.add(44)
    al.add(None)
    al.add(22)
    al.add(22)
    print(al)
    print(al.index_of(None))
    print(al.clear())
    print(al)
    al.insert(0, 100)
    print(al)
