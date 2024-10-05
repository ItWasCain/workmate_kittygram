from random import randint
import logging
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from cats.models import  Cat, User, Rating

DATA = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    help = 'Load data from csv file into the database'

    # def add_arguments(self, parser):
    #     parser.add_argument('filename', default='cats_data.csv', nargs='?',
    #                         type=str)

    def handle(self, *args, **options):
        try:
            # with open(
            #     os.path.join(DATA, options['filename']),
            #     newline='',
            #     encoding='utf8'
            # ) as csv_file:
            #     reader = DictReader(csv_file)
            #     for row in reader:
            #         _, created = Cat.objects.get_or_create(
            #             **row,
            #             breed=Breed.objects.order_by("?").first(),
            #             owner=User.objects.order_by("?").first()
            #         )
            for user in User.objects.all():
                for cat in Cat.objects.all():
                    _, created = Rating.objects.get_or_create(
                        user=user,
                        cat=cat,
                        rate=randint(1, 5),
                    )
        except FileNotFoundError:
            raise CommandError('Что-то пошло не так')
        logging.warning('Оценки успешно загружены')
