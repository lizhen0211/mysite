from django.core.management import BaseCommand

from aggregation.models import Publisher


class Command(BaseCommand):
    def handle(self, *args, **options):
        for index in range(5):
            Publisher.objects.create(name='publisher' + str(index))
        self.stdout.write(self.style.SUCCESS('init ok'))
