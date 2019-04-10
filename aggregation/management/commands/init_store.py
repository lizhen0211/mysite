import random

from django.core.management import BaseCommand

from aggregation.models import Store, Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        books = Book.objects.all()

        for index in range(0, 20):
            store = Store.objects.create(name='store' + str(index))
            # 每一个书店添加随机数量的书
            randomStartIndex = random.randint(0, books.__len__() - 1)
            for bookIndex in range(0, random.randint(randomStartIndex, books.__len__() - 1)):
                store.books.add(books[bookIndex])
        self.stdout.write(self.style.SUCCESS('init store ok'))
