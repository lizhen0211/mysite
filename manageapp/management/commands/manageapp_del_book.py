from django.core.management import BaseCommand

from manageapp.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        Book.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('del manageapp book ok'))
