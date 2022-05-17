import abc


class Base(abc.ABC):

    @property
    @abc.abstractmethod
    def value(self):
        return 'base 1'

    @value.setter
    @abc.abstractmethod
    def value(self, new_value):
        return


class ReadImplementation(Base):

    @property
    def value(self):
        return 'Read only'


class ReadWriteImplementation(Base):
    _value = 'Default value'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


r = ReadImplementation()
print(r.value)
try:
    r.value = 'madeln'
except Exception as err:
    print(err)

rw = ReadWriteImplementation()
print(rw.value)

rw.value = 'hegel'
print(rw.value)
