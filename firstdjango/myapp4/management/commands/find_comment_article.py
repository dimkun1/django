from django.core.management.base import BaseCommand
from myapp4.models import Article, Author, Comment


class Command(BaseCommand):
    help = "Find Comment Article title"

    def add_arguments(self, parser):
        parser.add_argument('title_article', type=str, help='Article title')

    def handle(self, *args, **kwargs):
        title_article = kwargs.get('title_article')

        # author = Author.objects.filter(firstname=name_author).first()

        for comment in Comment.objects.all():
            if comment.article.title == title_article:
                # print(article)
                self.stdout.write(f'{comment}')



