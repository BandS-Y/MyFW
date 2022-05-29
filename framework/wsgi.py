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
        view = self._get_view(request)
        response = self._get_response(request, view)
        start_response(response.status, list(response.headers.items()))
        return [response.body.encode()]

    def _get_view(self, request: Request):
        # Убираем лишний слэш в пути
        if request.path[-1:] == '/':
            path = request.path[:-1]
        else:
            path = request.path

        for url in self.urls:
            if url.path == path:
                url_return = url.view
                return url_return
        url_return = main.NotFound404
        return url_return

    def _get_response(self, request: Request, view: View):
        print('_get_response: ', end='')
        print(view, request.method)
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        else:
            return Response(status='404 WHAT', body="Method bot found")
