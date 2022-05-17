import requests
from requests.auth import AuthBase


class PizzaAuth(AuthBase):
    def __init__(self, name):
        self.name = name

    def __call__(self, request):
        request.headers['X-Pizza'] = self.name
        return request


r = requests.get('http://pizzabin.org/admin', auth=PizzaAuth('jagd'))
print(r)
print(r.text)
