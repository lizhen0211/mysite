from django.core.management import BaseCommand

from manageapp.models import APersonA


class Command(BaseCommand):
    def handle(self, *args, **options):
        APersonA.people.all().delete()
        self.stdout.write(self.style.SUCCESS('del personA ok'))
