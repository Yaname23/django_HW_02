from django.core.management import BaseCommand
from django.db import transaction

from homeworkapp.models import Client


class Command(BaseCommand):
    """Creates products """
    def handle(self, *args, **options):
        self.stdout.write('Create clients')

        @transaction.atomic
        def handle(self, *args, **options):
            self.stdout.write('Create client')
            client, created = Client.objects.get_or_create(
                name="Василий Васечкин",
                email="Vasillliq@mail.com",
                phone="89001122121",
                address="г.Мира, ул.Победы,9",

            )

            client.save()
            self.stdout.write(f'Create client - {client}')
