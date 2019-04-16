from django.core.management import BaseCommand

from manageapp.models import APersonA


class Command(BaseCommand):
    def handle(self, *args, **options):
        for index in range(0, 5):
            role = ''
            if index % 2 == 0:
                role = 'A'
            else:
                role = 'B'
            APersonA.people.create(first_name='first_name' + str(index),
                                   last_name='last_name' + str(index), role=role)
        self.stdout.write(self.style.SUCCESS('init persona ok'))
