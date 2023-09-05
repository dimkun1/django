from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from datetime import datetime
import logging
from random import randint
from . import models
from . import forms

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
        result = 'Решка'
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
    articles = models.Article.objects.filter(author__pk=author_id)
    # print(len(articles))
    context = {'title': title, 'articles': articles}
    # context = {'articles': articles}
    return render(request, 'myapp4/articles.html', context)


def get_article(request, article_id):
    title = "Статья"
    article = models.Article.objects.filter(pk=article_id).first()
    comments = models.Comment.objects.filter(article_id=article_id).order_by('id')[:10]
    print(len(comments))
    article.count += 1
    article.save()
    # print(len(articles))
    context = {'title': title, 'article': article, 'comments': comments}
    # context = {'articles': articles}
    return render(request, 'myapp4/get_article.html', context)


def get_comment(request, comment_id):
    title = "Коментарий"
    comment = models.Comment.objects.filter(pk=comment_id).first()
    context = {'title': title, 'comment': comment}
    return render(request, 'myapp4/get_comment.html', context)


def choice(request):
    if request.method == 'POST':
        form = forms.ChoiceForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'd':
                return redirect('cube')
                # return cube(request, count=count)
            elif game == 'r':
                # return redirect('rand100')
                return rand100(request)
            elif game == 'c':
                # return coin(request, count=count)
                return redirect('coin')
    else:
        form = forms.ChoiceForm()

    return render(request, 'myapp4/choice.html', {'form': form})


def author_form(request):
    message = 'Добавление автора'
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            author = models.Author(firstname=form.cleaned_data['firstname'], lastname=form.cleaned_data['lastname'],
                                   email=form.cleaned_data['email'], biography=form.cleaned_data['biography'],
                                   birthday=form.cleaned_data['birthday'])
            author.save()
            message = 'Автор успещно сохранен'
    else:
        form = forms.AuthorForm()
    return render(request, 'myapp4/author_form.html', {'form': form, 'message': message})


def article_form(request):
    message = 'Добавление статьи'
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST)
        message = 'Добавление статьи: ошибка в данных'
        if form.is_valid():
            article = models.Article(title=form.cleaned_data['title'], text=form.cleaned_data['text'],
                                     author=form.cleaned_data['author'],
                                     category=form.cleaned_data['category'])
            article.save()
            message = 'Статья успещно сохранена'
    else:
        form = forms.ArticleForm()
        message = 'Добавление статьи: заполните форму'
    return render(request, 'myapp4/article_form.html', {'form': form, 'message': message})


def comment_form(request):
    message = 'Добавление комментария'
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        message = 'Добавление комментария: ошибка в данных'
        if form.is_valid():
            comment = models.Comment(author=form.cleaned_data['author'],
                                     article=form.cleaned_data['article'],
                                     comment=form.cleaned_data['comment'])
            comment.save()
            message = 'Комментарий успещно сохранен'
    else:
        form = forms.CommentForm()
        message = 'Добавление комментария: заполните форму'
    return render(request, 'myapp4/comment_form.html', {'form': form, 'message': message})



def comment_form1(request, article_id):
    message = 'Добавление комментария'
    article = models.Article.objects.filter(pk=article_id).first()
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        message = 'Добавление комментария: ошибка в данных'
        if form.is_valid():
            comment = models.Comment(author=form.cleaned_data['author'],
                                     article=article,
                                     comment=form.cleaned_data['comment'])
            comment.save()
            message = 'Комментарий успещно сохранен'
    else:
        form = forms.CommentForm()
        message = 'Добавление комментария: заполните форму'
    return render(request, 'myapp4/comment_form.html', {'form': form, 'message': message})