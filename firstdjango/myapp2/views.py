import logging
from django.http import HttpResponse
from random import randint
from django.shortcuts import render

logger = logging.getLogger(__name__)


def text(title, text_site):
    return f'<h1>{title}</h1>' \
           f'<p align=center>{text_site}</p align=center>' \



def home(request):
    title = 'Главная страница'
    text_site = 'Здесь будет домашняя страница, и подробно написанна информация о сайте и компании'
    return HttpResponse(text(title, text_site))


def about(request):
    title = 'Контактная информация'
    text_site = 'Здесь будет контактная информация, и написанны номер телефона и адреса'
    return HttpResponse(text(title, text_site))