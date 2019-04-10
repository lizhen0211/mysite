import random

from django.core.management import BaseCommand

from aggregation.models import Book, Publisher, Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        publishers = Publisher.objects.all()
        authors = Author.objects.all()

        for index in range(20):
            book = Book.objects.create(name='book' + str(index), pages=30,
                                       price="{:.2f}".format(random.uniform(1, 100)),
                                       rating="{:.2f}".format(random.uniform(1, 10)),
                                       publisher=publishers[random.randint(0, publishers.__len__() - 1)])
            for index in range(0,random.randint(0, authors.__len__() - 1)):
                book.authors.add(authors[index])
            book.save()
        self.stdout.write(self.style.SUCCESS('init Book ok'))
