from pprint import pprint

import main
from framework.view import View
from framework.request import Request
from framework.response import Response


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        print('init Framework: ', end='')
        view = self._get_view(request)
        response = self._get_response(request, view)
        # print(response.status, response.headers.items())
        start_response(response.status, list(response.headers.items()))
        return [response.body.encode()]

    def _get_view(self, request: Request):
        # Убираем лишний слэш в пути
        if request.path[-1:] == '/':
            path = request.path[:-1]
        else:
            path = request.path

        print('_get_view: ', end='')
        print(path, self.urls)
        for url in self.urls:
            print(url.path, path)
            if url.path == path:
                url_return = url.view
                print(f'Return url: {url_return}')
                return url_return
        url_return = main.NotFound404
        print(f'Return url: {url_return}')
        return url_return

    def _get_response(self, request: Request, view: View):
        print('_get_response: ', end='')
        print(view, request.method)
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        else:
            return Response(status='404 WHAT', body="Method bot found")
