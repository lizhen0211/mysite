from django.core.management import BaseCommand

from aggregation.models import Author


class Command(BaseCommand):

    def handle(self, *args, **options):
        for index in range(5):
            Author.objects.create(name='author' + str(index), age=20 + index)
        self.stdout.write(self.style.SUCCESS('init ok'))
