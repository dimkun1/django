from django.core.management.base import BaseCommand
from myapp3.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        # user = User(name='Neo', email='Neo@example.com', password='secret', age=21)
        user = User(name='Jack', email='Jack@example.com', password='secret', age=59)
        user.save()
        self.stdout.write(f'{user}')
