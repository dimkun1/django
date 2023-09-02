from random import randint
from django.db import models
from datetime import datetime


class Kicks(models.Model):
    result = models.BooleanField()
    kick_time = models.DateTimeField(default=datetime.now())

    @staticmethod
    def statistic(self, n: int):
        reshka = 0
        orel = 0

        for _ in range(n):
            kick = Kicks(result=randint(0, 1))

            if kick.result:
                reshka += 1
            else:
                orel += 1

        result_dict = {
            'орел': orel,
            'решка': orel,
        }
        return result_dict


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    public_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    public = models.BooleanField()

    def __str__(self):
        return f'{self.title} {self.text}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField()

    def __str__(self):
        return f'{self.comment} {self.article} {self.author}'




