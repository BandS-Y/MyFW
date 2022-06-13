from abc import ABC, abstractmethod
from framework.response import Response
from framework.view import View


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
        print(f'что приходит в request {request} \n  в args {args} \n в kwargs {kwargs}')
        self.view.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        print('POST logger')
        self.view.post(self, request, *args, **kwargs)
