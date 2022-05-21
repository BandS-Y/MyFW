from pprint import pprint

def app(environ, start_responce):
    # выводим содержание передаваемых запросов, то что присылает сервер
    # pprint(environ)
    # выводим содержание запроса на сервер
    # pprint(environ['wsgi.input'].read())
    start_responce('200 OK', [('Content-Type', 'text/html')])
    return [b'test page']