from array_list import ArrayList


class Stack:

    # __init__也是方法，变量声明写在__init__里那么就是局部变量，只在该方法内有效。除非使用self.变量名声明，此时表示该变量是本对象特有的属性。
    # 而变量声明直接写在类中表示该变量是一个类变量，被所有对象共享，类似于C++、Java等语言的静态变量
    def __init__(self):
        self._list = ArrayList(10)

    def clear(self):
        self._list.clear()

    def size(self):
        return self._list.size()

    def is_empty(self):
        return self._list.is_empty()

    def push(self, element):
        self._list.add(element)

    def pop(self):
        return self._list.remove(self._list.size() - 1)

    def top(self):
        return self._list.get(self._list.size() - 1)


if __name__ == '__main__':
    s = Stack()
    s.push(11)
    s.push(22)
    s.push(33)
    s.push(44)
    print(s.top())
    print(s.size())
    s2 = Stack()
    s2.push(120)
    print(s2.top())
    print(s2.size())
    s.push(150)
    print(s.size())
