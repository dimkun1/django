from datetime import datetime
from random import randint
from django.core.management.base import BaseCommand
from myapp4.models import Article, Author


class Command(BaseCommand):
    help = "Create Post."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Post ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for author in Author.objects.all():
            # print(Author.objects.all())
            for j in range(randint(1, count + 1)):
                article = Article(title=f'Title{j}',
                            text=f'Text {j} is bla bla bla many long text',
                            author=author,
                            category=f'category{j}',
                            public=randint(0, 1)
                            )
                article.save()
                self.stdout.write(f'{article}')
