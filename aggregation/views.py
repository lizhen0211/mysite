from django.db.models import Avg, Max, FloatField, DecimalField, Count, Q, Min
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.db import connection
from aggregation.models import Book, Publisher, Store


def index(request):
    # count = Book.objects.filter(publisher__name='publisher3').count()
    # print('---' + str(count))
    # print(Book.objects.all().aggregate(pri_avg=Avg('price')))
    # print(Book.objects.all().aggregate(Max('price')).get('price__max'))
    # print(Book.objects.aggregate(pri_dif=Max('price', output_field=FloatField()) - Avg('price')))

    # print(Publisher.objects.aggregate(num_books=Count('book')))
    # pub = Publisher.objects.annotate(num_books=Count('book'))
    # print(pub)
    # print(pub[1].num_books)

    # above_5 = Count('book', filter=Q(book__rating__gt=5))
    # below_5 = Count('book', filter=Q(book__rating__lte=2))
    # pubs = Publisher.objects.annotate(below_5=below_5).annotate(above_5=above_5)
    # print(pubs[0].above_5)
    # print(pubs[0].below_5)

    # pubOrderByNumBooks = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')[:3]
    # for pub in pubOrderByNumBooks:
    #     print(pub.num_books)

    # print(Book.objects.aggregate(Avg('price'), Max('price'), Min('price')))
    # # print(Book.objects.all().query)
    # print(connection.queries)

    # books = Book.objects.annotate(Count('authors'))
    # print(books[1])
    # print(books[1].authors__count)
    # print(connection.queries)

    # book = Book.objects.all()
    # print(book)
    # print(book.authors.count())

    # q = Book.objects.annotate(num_authors=Count('authors'))
    # print(q[0].num_authors)

    # book = Book.objects.first()
    # print(book.authors.count())
    # print(book.store_set.count())
    #
    # books = Book.objects.all()
    # for bo in books:
    #     print(bo.authors.all().__len__())
    #     print('----------')
    # for bo in books:
    #     print(bo.store_set.all().__len__())
    #     print('++++++')
    # books = Book.objects.annotate(Count('authors', distinct=True)).annotate(Count('store', distinct=True))
    # print(books[0].authors__count, books[0].store__count)
    #
    # q = Book.objects.annotate(Count('authors'))
    # print(q.__len__())
    # print(books[0].authors__count, books[1].store_set.count())

    # stores = Store.objects.all().annotate(Avg('books__price'))
    # print(stores)
    # for st in stores:
    #     print(st.books__price__avg)

    # 连接和聚合
    stores = Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
    for store in stores:
        print('max:' + str(store.min_price) + "," + 'min:' + str(store.max_price))
    print(connection.queries)
    return HttpResponse('abc')
