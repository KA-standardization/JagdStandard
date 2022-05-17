import abc


class Base(abc.ABC):

    @property
    @abc.abstractmethod
    def value(self):
        return 'hello world'

    @property
    @abc.abstractmethod
    def constant(self):
        return 'hello world2'


class Implementation(Base):

    @property
    def value(self):
        return 'subclass hello world'

    constant = 'subclass hello world2'


i = Implementation()

print(i.value)
print(i.constant)
