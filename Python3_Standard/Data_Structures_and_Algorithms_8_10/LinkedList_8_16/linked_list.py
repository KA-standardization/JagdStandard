from abc_list_ import AbstractList


class LinkedList(AbstractList):
    first = None
    last = None

    class Node(object):
        def __init__(self, element, prev, next):
            self.prev = prev
            self.next = next
            self.element = element

    def clear(self):
        '''
        :return:
        '''
        self._size = 0
        self.first = None
        self.last = None

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
            old = self.last
            self.last = self.Node(element, old, None)
            if old == None:
                self.first = self.last
            else:
                old.next = self.last
        else:
            next_ = self.node(index)
            prev = next_.prev
            node_ = self.Node(element, prev, next_)
            next_.prev = node_

            if prev == None:
                self.first = node_
            else:
                prev.next = node_

        self._size += 1

    def remove(self, index):
        '''
        :param index:
        :return:
        '''
        self.range_check(index)

        node_ = self.node(index)
        prev = node_.prev
        next_ = node_.next

        if prev == None:
            self.first = next_
        else:
            prev.next = next_

        if next_ == None:
            self.last = prev
        else:
            next_.prev = prev

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

        if index < (self._size >> 1):
            node_ = self.first
            for i in range(index):
                node_ = node_.next
            return node_
        else:
            node_ = self.last
            for i in range(self._size - 1, index, -1):
                node_ = node_.prev
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
    ll = LinkedList()
    ll.add(11)
    ll.add(22)
    ll.add(33)
    ll.add(44)
    ll.add(55)
    ll.add(66)
    print(ll)
    print(ll.get(2))
    print(ll.index_of(66))
