from linked_list import LinkedList


class Queue(object):

    def __init__(self):
        '''
        链表
        '''
        self.list_ = LinkedList()

    def size(self):
        '''
        :return:
        '''
        return self.list_.size()

    def is_empty(self):
        '''
        :return:
        '''
        return self.list_.is_empty()

    def clear(self):
        '''
        :return:
        '''
        self.list_.clear()

    def en_queue(self, element):
        '''
        :param element: 队尾添加元素
        :return:
        '''
        self.list_.add(element)

    def de_queue(self):
        '''
        :return:
        '''
        return self.list_.remove(0)

    def front(self):
        '''
        :return: 队头
        '''
        return self.list_.get(0)


if __name__ == '__main__':
    q = Queue()
    q.en_queue(11)
    q.en_queue(12)
    q.en_queue(113)
    q.en_queue(114)
    q.en_queue(115)
    q.en_queue(116)
    q.en_queue(117)
    q.en_queue(118)
    q.en_queue(119)
    q.en_queue(110)
    print(q.is_empty())
    print(q.de_queue())
    print(q.front())
