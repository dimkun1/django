import logging
from django.http import HttpResponse
from random import randint

logger = logging.getLogger(__name__)


def text(title, result):
    return f'<h1>{title}</h1>' \
            f'<p>Результат для вас {result}</p>'




def coin(request):
    title = 'Бросок монеты'
    temp = randint(1,2)
    if temp == 1:
        result = 'Решко'
    else:
        result = 'Орел'
    logger.info(f'Сгенерированно значение - {result}')
    return HttpResponse(text(title, result))


def cube(request):
    title = 'Бросок кубика'
    result = randint(1, 6)
    logger.info(f'Сгенерированно значение - {result}')
    return HttpResponse(text(title, result))



def rand100(request):
    title = 'Случайное число от 1 до 100'
    result = randint(1, 100)
    logger.info(f'Сгенерированно значение - {result}')
    return HttpResponse(text(title, result))

