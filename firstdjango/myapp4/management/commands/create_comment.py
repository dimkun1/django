from random import randint, random
from django.core.management.base import BaseCommand
from myapp4.models import Article, Author, Comment


class Command(BaseCommand):
    help = "Create Comment."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Comment ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for author in Author.objects.all():
            for article in Article.objects.all():
                # print(Author.objects.all())
                for j in range(randint(1, count + 1)):
                    comment = Comment(author=author,
                                      article=article,
                                      comment=f'text comment {j} bla bla bla',
                                      update_date='1900-01-01 00:01'
                                      )
                    comment.save()
                    self.stdout.write(f'{comment}')
