from collections import abc

dict_ = {1: 11, 2: 22}
print(isinstance(dict_, abc.Iterable))
print(isinstance(dict_, abc.Mapping))
print(isinstance(dict_, abc.Sequence))
print(isinstance(dict_, abc.MutableMapping))
print(isinstance(dict_, abc.AsyncGenerator))


def async_():
    yield 100
    yield 200


print(isinstance(async_, abc.AsyncGenerator))
print(isinstance(async_, abc.Hashable))
