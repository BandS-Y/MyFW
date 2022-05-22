from framework.wsgi import Framework
from framework.url import Url
from framework.view import View


class FirstView(View):

    # def __init__(self):
    #     super().__init__()

    def get(self, request):
        return "it's get ask"

    def post(self, request):
        return "it's post ask"


urls = [
    Url('/mainpage', FirstView),
    Url('/about', FirstView)
]

app = Framework(urls)
