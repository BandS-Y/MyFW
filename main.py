from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response
from framework.template import render


class About(View):

    # def __init__(self):
    #     super().__init__()

    def get(self, request, *args, **kwargs):
        body = render('authors.html', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
        return Response(body=body)

    def post(self, request, *args, **kwargs):

        return Response(status='201 Created', body="it's About post ask", headers={'About': '123'})


class MainPage(View):

    def get(self, request, *args, **kwargs):
        body = render('mainpage.html')
        return Response(body=body)

    def post(self, request, *args, **kwargs):
        return Response(status='201 Created', body="it's MainPage post ask", headers={'MainPage': '123'})


class Contacts(View):

    def get(self, request, *args, **kwargs):
        body = render('contacts.html')
        return Response(body=body)

    def post(self, request, *args, **kwargs):
        return Response(status='201 Created', body="it's contacts post ask", headers={'MainPage': '123'})

class NotFound404(View):

    def get(self, request, *args, **kwargs):
        body = render('404.html')
        return Response(body=body)

    def post(self, request, *args, **kwargs):
        return Response(status='404 WHAT', body="404 PAGE Not Found", headers={'404 WHAT': '123'})


urls = [
    Url('/mainpage', MainPage),
    Url('/about', About),
    Url('/contacts', Contacts)
]

app = Framework(urls)
