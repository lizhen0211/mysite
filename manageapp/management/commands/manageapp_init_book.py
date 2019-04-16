from django.core.management import BaseCommand

from manageapp.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        for index in range(0, 5):
            Book.objects.create(title='title' + str(index), author='Roald Dahl')
        for index in range(0, 5):
            Book.objects.create(title='title' + str(index + 5), author='Jack')
        self.stdout.write(self.style.SUCCESS('init Book ok'))
