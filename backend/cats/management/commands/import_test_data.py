from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):
        call_command("users_import", *args, **options)
        call_command("breeds_import", *args, **options)
        call_command("cats_import", *args, **options)
        call_command("rating_import", *args, **options)
