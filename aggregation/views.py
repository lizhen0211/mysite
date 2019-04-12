from django.db.models import Avg, Max, FloatField, DecimalField, Count, Q, Min, Sum
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.db import connection
from aggregation.models import Book, Publisher, Store, Author


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
    # stores = Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
    # for store in stores:
    #     print('max:' + str(store.min_price) + "," + 'min:' + str(store.max_price))
    # print(connection.queries)

    # Following relationships backwards¶
    # publishers = Publisher.objects.annotate(Count('book'))
    # for pub in publishers:
    #     print(pub.book__count)

    # oldestPubdate = Publisher.objects.aggregate(oldest_pubdate=Min('book__pubdate'))
    # print(oldestPubdate)

    # authors = Author.objects.annotate(total_page=Sum('book__pages'))
    # for author in authors:
    #     # print(author.book_set.all(), author.book__count)
    #     for book in author.book_set.all():
    #         print(book.pages)
    #     print('-----------')
    # for au in authors:
    #     print(au.total_page)

    # 只有连接，没有groupby

    """
    SELECT AVG(aggregation_book.rating) AS average_rating FROM aggregation_author LEFT OUTER JOIN aggregation_book_authors ON (aggregation_author.id = aggregation_book_authors.author_id)
    LEFT OUTER JOIN aggregation_book ON (aggregation_book_authors.book_id = aggregation_book.id)
    """

    # bookRatings = Author.objects.aggregate(average_rating=Avg('book__rating'))
    # print('a', str(bookRatings))

    """
    SELECT aggregation_author.id, aggregation_author.name, aggregation_author.age, AVG(aggregation_book.rating) AS average_rating FROM aggregation_author LEFT OUTER JOIN aggregation_book_authors ON (aggregation_author.id = aggregation_book_authors.author_id) LEFT OUTER JOIN aggregation_book ON (aggregation_book_authors.book_id = aggregation_book.id)
    GROUP BY aggregation_author.id
    """
    # bookRatingsA = Author.objects.annotate(average_rating=Avg('book__rating'))
    # print(bookRatingsA)

    # result = 0
    # for b in bookRatingsA:
    #     if b.average_rating:
    #         result += b.average_rating
    #     print(b.average_rating)
    # print('b', bookRatingsA.__len__(), result / (bookRatingsA.__len__()-1))
    # print(bookRatingsA)

    # Aggregations and other QuerySet clauses
    # book = Book.objects.filter(name__startswith='book').annotate(Count('pages'))
    # print(book)
    # print(connection.queries)
    # for rating in bookRatings:
    # print(rating.rating)

    # books = Book.objects.annotate(num_authors=Count('authors')).filter(num_authors__gte=3)
    # print(books.__len__())
    # highly_rated = Count('book', filter=Q(book_rating__gte=1))

    # 过滤 annotate
    # count = Count('book', filter=Q(book__rating__gte=5))
    # authors = Author.objects.annotate(num_books=Count('book'), highly_rated_books=count)
    # for author in authors:
    #     # print(author.num_books, author.highly_rated_books)
    #     print(author)
    # authors = Author.objects.annotate(num_books=Count('book')).filter(num_books__gte=5)
    # print('-----')
    # for author in authors:
    #     print(author)

    # 顺序annotate()和filter()条款
    # publisher = Publisher.objects.annotate(num_book=Count('book', distinct=True)).filter(book__rating__gte=3)
    # print(publisher)
    # higrating = Count('book', filter=Q(book__rating__gte=3))
    # pub = Publisher.objects.annotate(num_book=Count('book', distinct=True), higrating=higrating)
    # print(pub)
    #
    # b = Publisher.objects.annotate(num_books=Count('book', distinct=True)).filter(book__rating__gt=3.0)
    # print(b)
    # annotate = Publisher.objects.filter(book__rating__gte=3).annotate(Count('book', distinct=True))
    # print(annotate)

    # rating__filter = Publisher.objects.annotate(avg_rating=Avg('book__rating')).filter(avg_rating__gt=3)
    # print(rating__filter)

    # ps1 = Publisher.objects.annotate(avg_rating=Avg('book__rating')).filter(book__rating__gt=3.0)
    # ps2 = Publisher.objects.filter(book__rating__gt=3.0).annotate(avg_rating=Avg('book__rating'))
    # print(ps1)
    # print(ps2)

    # books = Book.objects.annotate(num_authors=Count('authors')).order_by('num_authors')
    # print(books)
    # authors1 = Author.objects.annotate(average_rating=Avg('book__rating'))
    # authors2 = Author.objects.values('name','age').annotate(average_rating=Avg('book__rating'))
    # print(authors1)
    # print(authors2)

    # authors3 = Author.objects.annotate(average_rating=Avg('book__rating')).values('name', 'average_rating')
    # authors3 = Author.objects.annotate(average_rating=Avg('book__rating')).values('name', 'average_rating')
    # print(authors3)
    # authors = Author.objects.annotate(id_count=Count('id'))
    # for author in authors:
    #     print(author,author.id_count)
    #
    # print('----------')
    # authors = Author.objects.annotate(id_count=Count('id')).order_by()
    # for author in authors:
    #     print(author, author.id_count)

    books = Book.objects.annotate(num_authors=Count('authors')).aggregate(Avg('num_authors'))
    # for book in books:
    #     print(book.name, book.num_authors)
    print(books)
    print(connection.queries)
    return HttpResponse('abc')
