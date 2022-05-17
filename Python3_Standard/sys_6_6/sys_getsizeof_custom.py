import sys


class Jagd:

    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        return

    def __sizeof__(self):
        return object.__sizeof__(self) + sum(sys.getsizeof(v) for v in self.__dict__.values())


jagd = Jagd()
print(sys.getsizeof(jagd))
