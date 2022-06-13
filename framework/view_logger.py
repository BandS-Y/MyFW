from abc import ABC, abstractmethod
from framework.response import Response
from framework.view import View
import time


class ViewLogger(View, ABC):
    def __init__(self, view):
        self.view = view

    @abstractmethod
    def get(self, request, *args, **kwargs) -> Response:
        pass

    @abstractmethod
    def post(self, request, *args, **kwargs) -> Response:
        pass


class Logger(ViewLogger):

    def get(self, request, *args, **kwargs) -> Response:
        print('GET logger')
        start = time.time()
        ret = self.view.get(self, request, *args, **kwargs)
        end = time.time()
        print(f'Время выполнения представления: {self.view.__name__} {round(end-start, 4)} секунд')
        return ret

    def post(self, request, *args, **kwargs) -> Response:
        print('POST logger')
        start = time.time()
        ret = self.view.get(self, request, *args, **kwargs)
        end = time.time()
        print(f'Время выполнения представления: {self.view.__name__} {round(end-start, 4)} секунд')
        return ret
