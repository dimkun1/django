from datetime import datetime

from django.core.management.base import BaseCommand
from myapp4.models import Author


class Command(BaseCommand):
    help = "Create user."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Author ID')


    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            # user = User(name='John', email='john@example.com', password='secret', age=25)
            # user = User(name='Neo', email='Neo@example.com', password='secret', age=21)
            user = Author(firstname=f'Firstname{i}', lastname=f'Lastname{i}', email=f'email{i}@example.com', biography=f'biography{i}', birthday=datetime.now())
            user.save()
            self.stdout.write(f'{user}')
