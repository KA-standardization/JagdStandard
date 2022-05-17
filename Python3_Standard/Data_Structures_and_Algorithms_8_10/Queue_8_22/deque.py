from linked_list import LinkedList


class Deque(object):

    def __init__(self):
        self.list_ = LinkedList()

    def size(self):
        return self.list_.size()

    def is_empty(self):
        return self.list_.is_empty()

    def clear(self):
        self.list_.clear()

    def en_queue_front(self, element):
        self.list_.add(element)

    def en_queue_rear(self, element):
        self.list_.insert(0, element)

    def de_queue_front(self, element):
        return self.list_.remove(0)

    def de_queue_rear(self, element):
        return self.list_.remove(self.list_.size() - 1)

    def front(self):
        return self.list_.get(0)

    def rear(self):
        return self.list_.get(self.list_.size() - 1)

    def print_list(self):
        print(self.list_)


if __name__ == '__main__':
    dq = Deque()
    dq.en_queue_front(11)
    dq.en_queue_front(12)
    dq.en_queue_front(13)
    dq.en_queue_front(14)
    dq.en_queue_rear(15)
    dq.en_queue_rear(16)
    dq.print_list()
    print(dq.front())
    print(dq.rear())

