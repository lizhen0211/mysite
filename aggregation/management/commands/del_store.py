from django.core.management import BaseCommand

from aggregation.models import Store


class Comman(BaseCommand):
    def handle(self, *args, **options):
        Store.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('del store ok'))
