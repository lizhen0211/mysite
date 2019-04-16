from django.core.management import BaseCommand

from manageapp.models import OpinionPoll


class Command(BaseCommand):
    def handle(self, *args, **options):
        OpinionPoll.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('OpinionPoll is ok'))
