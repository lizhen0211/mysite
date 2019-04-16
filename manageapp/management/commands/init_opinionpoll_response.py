from datetime import datetime
import random

from django.core.management import BaseCommand

from manageapp.models import OpinionPoll, Response


class Command(BaseCommand):
    def handle(self, *args, **options):
        list = []
        for index in range(0, 5):
            object = OpinionPoll.objects.create(question=str(index), poll_date=datetime.now())
            list.append(object)
        for index in range(0, 20):
            # randomStart = random.randint(0, 2)
            # randomEnd = random.randint(3, 5)
            randIndex = random.randint(0, 4)
            Response.objects.create(poll=list[randIndex], person_name='personName' + str(index),
                                    response='asdfsadfsadfsadfsdfsadfasdfasdfasdfasdfasdfaasdfasdfasdfasdfasdfa')

        self.stdout.write(self.style.SUCCESS('init OpinionPoll ok'))
