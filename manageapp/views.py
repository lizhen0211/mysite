from django.db import connection
from django.http import HttpResponse

# Create your views here.
from manageapp.models import Person, OpinionPoll, Response, Book, APersonA
from django.contrib.auth.models import User

def index(request):
    # print(Person.people.all())
    # print(OpinionPoll.objects.all())
    # print(OpinionPoll.objects.with_counts())
    # print(Response.objects.filter(response__contains='asdddd'))
    # print(Response.objects.filter(person_name='personName0'))
    # print(Book.objects.all())
    # print(Book.dahl_objects.all())
    print(APersonA.people.all())
    print(APersonA.authors.all())
    print(APersonA.editors.all())

    print(connection.queries)

    print(User.objects.all())
    return HttpResponse('abc')
