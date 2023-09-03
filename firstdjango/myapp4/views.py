from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from datetime import datetime
import logging
from random import randint
from .models import Author, Article, Comment

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'myapp4/index.html')


def about(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    context = {'datetime': datetime.now(), 'client_ip': ip}
    return render(request, 'myapp4/about.html', context)


def coin(request):
    title = 'Бросок монеты'
    temp = randint(1, 2)
    if temp == 1:
        result = 'Решко'
    else:
        result = 'Орел'
    logger.info(f'Сгенерированно значение - {result}')
    context = {'title': title, 'result': result}
    return render(request, 'myapp4/coin.html', context)


def cube(request):
    title = 'Бросок кубика'
    result = randint(1, 6)
    logger.info(f'Сгенерированно значение - {result}')
    context = {'title': title, 'result': result}
    return render(request, 'myapp4/cube.html', context)


def rand100(request):
    title = 'Случайное число от 1 до 100'
    result = randint(1, 100)
    logger.info(f'Сгенерированно значение - {result}')
    context = {'title': title, 'result': result}
    return render(request, 'myapp4/rand100.html', context)


def get_articles(request, author_id):
    title = "Статьи по автору"
    articles = Article.objects.filter(author__pk=author_id)
    # print(len(articles))
    context = {'title': title, 'articles': articles}
    # context = {'articles': articles}
    return render(request, 'myapp4/articles.html', context)


def get_article(request, article_id):
    title = "Статья"
    article = Article.objects.filter(pk=article_id).first()
    comments = Comment.objects.filter(article_id=article_id).order_by('id')[:10]
    print(len(comments))
    article.count += 1
    article.save()
    # print(len(articles))
    context = {'title': title, 'article': article, 'comments': comments}
    # context = {'articles': articles}
    return render(request, 'myapp4/get_article.html', context)


def get_comment(request, comment_id):
    title = "Коментарий"
    comment = Comment.objects.filter(pk=comment_id).first()
    context = {'title': title, 'comment': comment}
    return render(request, 'myapp4/get_comment.html', context)
