from django.core.management.base import BaseCommand
from myapp4.models import Article, Author, Comment


class Command(BaseCommand):
    help = "Find Comment Author firstnam"

    def add_arguments(self, parser):
        parser.add_argument('name_author', type=str, help='Author firstname')

    def handle(self, *args, **kwargs):
        name_author = kwargs.get('name_author')

        # author = Author.objects.filter(firstname=name_author).first()

        for comment in Comment.objects.all():
            if comment.author.firstname == name_author:
                # print(article)
                self.stdout.write(f'{comment}')



