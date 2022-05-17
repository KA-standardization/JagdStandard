import abc
import io


class ABCWithConcrete(abc.ABC):

    @abc.abstractmethod
    def foo(self, input):
        print('base class read')
        return input.read()


class ConcreteOverride(ABCWithConcrete):

    def foo(self, input):
        base_data = super(ConcreteOverride, self).foo(input)
        print('subclass read')
        response = sorted(base_data.splitlines())
        return response


input = io.StringIO('''line 0
line 1
line 2
line 3
''')

reader = ConcreteOverride()
print(reader.foo(input))
