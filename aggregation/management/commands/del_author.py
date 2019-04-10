from django.core.management import BaseCommand

from aggregation.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        Author.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('del ok'))
