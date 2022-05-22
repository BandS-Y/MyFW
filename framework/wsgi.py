from pprint import pprint

from framework.view import View
from framework.request import Request


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        print('init Framework: ', end='')
        view = self._get_view(request)
        print(self._get_response(request, view))
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'test page']

    def _get_view(self, request: Request):
        path = request.path
        url_return = None
        print('_get_view: ', end='')
        print(path, self.urls)
        for url in self.urls:
            print(url.path)
            if url.path == path:
                url_return = url.view
        print(f'Return url: {url_return}')
        return url_return

    def _get_response(self, request: Request, view: View):
        print('_get_response: ', end='')
        print(view, request.method)
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        else:
            return 'Method is not exist'

# def app(environ, start_response):
#     # выводим содержание передаваемых запросов, то что присылает сервер
#     pprint(environ)
#     # выводим содержание запроса на сервер
#     pprint(environ['wsgi.input'].read())
#
#     request = Request(environ)
#     print(request.method)
#     print(request.path)
#     print(request.headers)
#     print(request.query)
#
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'test page']
