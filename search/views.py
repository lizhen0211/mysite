from django.http import HttpResponse

# Create your views here.
from pymemcache import Client
# from djmemcache.client import Client
# from django.core.cache import cache

def index(request):
    client = Client(('localhost', 11211))
    client.set('some_key', 'some_value')
    result = client.get('some_key')

    print(result)

    return HttpResponse('abc')
