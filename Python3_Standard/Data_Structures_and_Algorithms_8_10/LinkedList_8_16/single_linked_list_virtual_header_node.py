from abc_list_ import AbstractList


class SingleLinkedListVirtualHeader(AbstractList):
    '''
    增加虚拟头节点(不存储数据):
        让代码更加精简，统一所有节点的处理逻辑
    '''

    class Node(object):

        def __init__(self, element, next):
            self.element = element
            self.next = next

    first = Node(None, None)

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

        prev = self.first if index == 0 else self.node(index - 1)
        prev.next = self.Node(element, prev.next)
        self._size += 1

    def remove(self, index):
        '''
        :param index:
        :return:
        '''
        self.range_check(index)

        prev = self.first if index == 0 else self.node(index - 1)
        node_ = prev.next
        self._size -= 1
        return node_.element

    def index_of(self, element):
        '''
        :param element:
        :return:
        '''
        if element == None:
            node_ = self.first
            for i in range(self._size):
                if node_.element == None:
                    return i
                node_ = node_.next
        else:
            node_ = self.first
            for i in range(self._size):
                if element.__eq__(node_.element):
                    return i
                node_ = node_.next
        return self._NOT_FOUND

    def node(self, index):
        '''
        :param index:
        :return:
        '''
        self.range_check(index)

        node_ = self.first.next
        for i in range(index):
            node_ = node_.next
        return node_

    def __str__(self):
        tmp_list = []
        node_ = self.first.next
        for i in range(self._size):
            tmp_list.append(node_.element)
            node_ = node_.next
        return "size: {}".format(self._size) + repr(tmp_list)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    sl = SingleLinkedListVirtualHeader()
    sl.add(11)
    sl.add(22)
    sl.add(33)
    sl.insert(1, 66)
    print(sl)
