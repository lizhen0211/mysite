from django.core.management import BaseCommand

from aggregation.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        Book.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('del book ok'))
