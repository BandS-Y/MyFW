import abc


class Writer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write_message(self):
        pass


class ConcreteWriter(Writer):
    def write_message(self, message):
        print(message)


class WriterDecorator(Writer, metaclass=abc.ABCMeta):
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def write_message(self):
        pass


class CheckLengthDecorator(WriterDecorator):
    def write_message(self, message):
        print('checking message length')
        self._component.write_message(message)


class CompressDecorator(WriterDecorator):
    def write_message(self, message):
        print('compressing message')
        self._component.write_message(message)
        print('check compressed length')


concrete_writer = ConcreteWriter()
# concrete_writer.write_message('writing message')
check_length_decorator = CheckLengthDecorator(concrete_writer)
compress_decorator = CompressDecorator(check_length_decorator)
compress_decorator.write_message('writing message')
