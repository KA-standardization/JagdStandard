from abc_list_ import AbstractList


class SingleCircleLinkedList(AbstractList):
    first = None

    class Node(object):
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def clear(self):
        '''

        :return:
        '''
        self._size = 0
        self.first = None

    def get(self, index):
        '''

        :param index:
        :return:
        '''
        return self.node(index).element

    def set(self, index, element):
        '''

        :param index:
        :param element:
        :return:
        '''
        node_ = self.node(index)
        old = node_.element
        node_.element = element
        return old

    def insert(self, index, element):
        '''

        :param index:
        :param element:
        :return:
        '''
        self.range_check_for_add(index)

        if index == 0:
            new_first = self.Node(element, self.first)
            last = new_first if self._size == 0 else self.node(self._size - 1)
            last.next = new_first
            self.first = new_first
        else:
            prev = self.node(index - 1)
            prev.next = self.Node(element, prev.next)
        self._size += 1

    def remove(self, index):
        '''

        :param index:
        :return:
        '''
        self.range_check(index)

        node_ = self.first
        if index == 0:
            if self._size == 1:
                self.first = None
            else:
                last = self.node(self._size - 1)
                self.first = self.first.next
                last.next = self.first
        else:
            prev = self.node(index - 1)
            node_ = prev.next
            prev.next = node_.next

        self._size -= 1
        return node_.element

    def index_of(self, element):
        '''

        :param element:
        :return:
        '''
        node_ = self.first
        if element == None:
            for i in range(self._size):
                if node_.element == None: return i
                node_ = node_.next
        else:
            for i in range(self._size):
                if element.__eq__(node_.element): return i
                node_ = node_.next

        return self._NOT_FOUND

    def node(self, index):
        '''

        :param index:
        :return:
        '''
        self.range_check(index)
        node_ = self.first
        for i in range(index):
            node_ = node_.next
        return node_

    def __str__(self):
        tmp_list = []
        node_ = self.first
        for i in range(self._size):
            tmp_list.append(node_.element)
            node_ = node_.next
        return "size: {}".format(self._size) + repr(tmp_list)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    scll = SingleCircleLinkedList()
    scll.add(1)
    scll.add(12)
    scll.add(13)
    scll.add(14)
    scll.add(15)
    scll.add(16)
    scll.add(17)
    scll.add(18)
    print(scll)
    print(scll.get(1))
    scll.set(1, 1000)
    print(scll)
