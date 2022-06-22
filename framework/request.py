class Request:

    def __init__(self, environ):
        self.method = environ.get('REQUEST_METHOD').lower()
        self.path = environ.get('PATH_INFO')
        self.headers = self._get_headers(environ)
        self.query = self._get_query(environ.get('QUERY_STRING'))

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value
        return headers

    def _get_query(self, querys):
        query_params = {}
        print(querys)

        if not querys:
            return {}

        querys = querys.split('&')
        for query in querys:
            key, value = query.split('=')
            if query_params.get(key):
                query_params[key].append(value)
            else:
                query_params[key] = [value]
        print(query_params)
        return query_params


