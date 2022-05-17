from abc_list_ import AbstractList


class CircleLinkedList(AbstractList):
    first = None
    last = None
    current = None

    class Node(object):
        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def reset(self):
        '''
        :return:
        '''
        self.current = self.first

    def next(self):
        '''
        :return:
        '''
        if self.current == None: return None
        self.current = self.current.next
        return self.current.element

    def delete(self):
        '''
        :return:
        '''
        if self.current == None: return None

        next_ = self.current.next
        element = self.remove_node(self.current)
        if self._size == 0:
            self.current = None
        else:
            self.current = next_
        return element

    def clear(self):
        '''
        :return:
        '''
        self._size = 0
        self.first = None
        self.last = None
        # self.current = None

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

        if index == self._size:
            old_last = self.last
            self.last = self.Node(element, old_last, self.first)
            if old_last == None:
                self.first = self.last
                self.first.next = self.first
                self.first.prev = self.first
            else:
                old_last.next = self.last
                self.first.prev = self.last
        else:
            next_ = self.node(index)
            prev = next_.prev
            node_ = self.Node(element, prev, next_)
            next_.prev = node_
            prev.next = node_

            # index=0
            if next_ == self.first: self.first = node_

        self._size += 1

    def remove(self, index):
        '''
        :param index:
        :return:
        '''
        self.range_check(index)
        return self.remove_node(self.node(index))

    def remove_node(self, node_):
        '''
        :param node_:
        :return:
        '''
        if self._size == 1:
            self.first = None
            self.last = None
            self.current = None
        else:
            prev = node_.prev
            next_ = node_.next
            prev.next = next_
            next_.prev = prev
            if node_ == self.first: self.first = next_
            if node_ == self.last: self.last = prev

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
                if node_.element == None: return i;
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

        if index < (self._size >> 1):
            node_ = self.first
            for i in range(index):
                node_ = node_.next
            return node_
        else:
            node_ = self.last
            for i in range(self._size - 1, index, -1):
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
    cll = CircleLinkedList()
    cll.add(11)
    cll.add(111)
    cll.add(112)
    cll.add(131)
    cll.add(114)
    cll.add(141)
    cll.add(115)
    cll.add(116)
    print(cll)
