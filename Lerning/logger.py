import abc


class Writer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write_message(self, message):
        pass


class WriterDecorator(Writer, metaclass=abc.ABCMeta):
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def write_message(self, message):
        pass


class CheckLengthDecorator(WriterDecorator):
    def write_message(self, message):
        print('checking message length')
        res = self._component.write_message(self, message)
        return res


class CompressDecorator(WriterDecorator):
    def write_message(self, message):
        print('compressing message')
        res = self._component.write_message(message)
        print('check compressed length')
        return res


@CompressDecorator
@CheckLengthDecorator
class ConcreteWriter(Writer):
    def write_message(self, message):
        # print(f'вывожу сообщение: {message}')
        return f'вывожу сообщение: {message}'


concrete_writer = ConcreteWriter

print(concrete_writer.write_message('writing message'))


# check_length_decorator = CheckLengthDecorator(concrete_writer)
# compress_decorator = CompressDecorator(check_length_decorator)
# compress_decorator.write_message('writing message')
