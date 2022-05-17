import ctypes


class DynamicArray:
    '''
    动态数组:
        开辟、销毁内存空间的次数相对较少，但可能造成内存空间浪费（可以通过缩容解决）
    '''

    def __init__(self):
        '''
        _size: 数组元素个数
        _capacity: 初始数组容量
        array: 初始化数组
        '''
        self._size = 0
        self._capacity = 10
        self._NOT_FOUND = -1
        self._array = self._make_array(self._capacity)

    def _make_array(self, c):
        '''
        :return: 连续内存
        '''
        return (c * ctypes.py_object)()

    def clear(self):
        '''
        :return:
        '''
        self._size = 0
        for i in range(self._size):
            self._array[i] = None

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

    def set(self, index, element):
        '''
        :param index:
        :param element:
        :return:
        '''
        self.range_check(index)
        tmp_old = self._array[index]
        self._array[index] = element
        return tmp_old

    def add(self, element):
        '''
        :param element:
        :return:
        '''
        self.insert(self._size, element)

    def insert(self, index, element):
        '''
        :param index:
        :param element:
        :return:
        '''
        self.range_check_for_add(index)
        self.ensure_capacity(self._size + 1)
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = element
        self._size += 1

    def get(self, index):
        '''
        :param index:
        :return:
        '''
        self.range_check(index)
        return self._array[index]

    def contains(self, element):
        '''
        :param element:
        :return:
        '''
        return self.index_of(element) != self._NOT_FOUND

    def remove(self, index):
        '''
        :param index:
        :return:
        '''
        self.range_check(index)
        old = self._array[index]
        for i in range(index + 1, self._size):
            self._array[i - 1] = self._array[i]
        self._size -= 1
        self._array[self._size] = None
        return old

    def index_of(self, element):
        '''
        :param element:
        :return:
        '''
        if element == None:
            for i in range(self._size):
                if self._array[i] == None:
                    return i
        else:
            for i in range(self._size):
                if element.__eq__(self._array[i]):
                    return i
        return self._NOT_FOUND

    def ensure_capacity(self, capacity):
        '''
        :param capacity:
        :return:
        '''
        old_capacity = len(self._array)
        if old_capacity >= capacity:
            return

        new_capacity = old_capacity + (old_capacity >> 1)
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        print('{} capacity--> {}'.format(old_capacity, new_capacity))

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

    def __str__(self):
        tmp_list = []
        for i in range(self._size):
            tmp_list.append(self._array[i])
        return "size: {}".format(self._size) + repr(tmp_list)

    def __repr__(self):
        self.__str__()


if __name__ == '__main__':
    d = DynamicArray()
    d.add(3)
    d.add(2)
    d.add(4)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    d.add(3)
    print(d.index_of(3))
    print(d)
