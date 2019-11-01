from django.http import HttpResponse

# Create your views here.
from pymemcache import Client
# from djmemcache.client import Client
from django.core.cache import cache

def index(request):
    #Py
    # client = Client(('localhost', 11211))
    # client.set('some_key', 'some_value')
    # result = client.get('some_key')
    #
    # print(result)
    cache.set('some_key', 'some_value')
    val = cache.get('some_key')
    print(val)

    return HttpResponse('abc')
