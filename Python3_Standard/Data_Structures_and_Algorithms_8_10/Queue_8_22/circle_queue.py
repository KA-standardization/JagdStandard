import ctypes


class CircleQueue(object):

    def __init__(self):
        self.front = 0
        self.size_ = 0
        self._capacity = 10
        self._NOT_FOUND = -1
        self._array = self._make_array(self._capacity)

    def _make_array(self, c):
        '''
        :return: 连续内存
        '''
        return (c * ctypes.py_object)()

    def size(self):
        return self.size_

    def is_empty(self):
        return self.size_ == 0

    def clrar(self):
        for i in range(self.size_):
            self._array[i] = None
        self.front = 0
        self.size_ = 0

    def en_queue(self, element):
        self.ensure_capacity(self.size_ + 1)
        self._array[self.index(self.size_)] = element
        self.size_ += 1

    def de_queue(self):
        front_element = self._array[self.front]
        self._array[self.front] = None
        self.front = self.index(1)
        self.size_ -= 1
        return front_element

    def front_queue(self):
        return self._array[self.front]

    def index(self, index):
        index += self.front
        print(len(self._array))
        return index - (len(self._array) if index >= len(self._array) else 0)

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
        for i in range(self.size_):
            new_array[i] = self._array[i]
        self._array = new_array
        print('{} capacity--> {}'.format(old_capacity, new_capacity))

    def __str__(self):
        tmp_list = []
        for i in range(self.size_):
            tmp_list.append(self._array[i])
        return "size: {}".format(self.size_) + repr(tmp_list)

    def __repr__(self):
        self.__str__()


if __name__ == '__main__':
    cq = CircleQueue()
    cq.en_queue(11)
    print(cq.front)
    cq.en_queue(12)
    cq.en_queue(13)
    cq.en_queue(14)
    cq.en_queue(15)
    cq.en_queue(16)
    print(cq.de_queue())
    print(cq.front)

    print(cq)
