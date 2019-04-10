from django.core.management import BaseCommand

from aggregation.models import Publisher


class Command(BaseCommand):
    def handle(self, *args, **options):
        Publisher.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('del ok'))
