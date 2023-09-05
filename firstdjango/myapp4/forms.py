from django import forms
import datetime
from . import models

class ChoiceForm(forms.Form):
    game = forms.ChoiceField(choices=[('d', 'Кубик'), ('r', 'Случайное число'), ('c', 'Монетка')])
    count = forms.IntegerField(min_value=1, max_value=64)


class AuthorForm(forms.Form):
    firstname = forms.CharField(label='Имя', max_length=100)
    lastname = forms.CharField(label='Фамилия', max_length=100)
    email = forms.EmailField(label='Емайл')
    biography = forms.CharField(label='О себе', widget=forms.Textarea)
    birthday = forms.DateField(label='Дата др', initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'type': 'date'}))

class ArticleForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=200)
    text = forms.CharField(label='Статья', widget=forms.Textarea)
    category = forms.CharField(label='Категория', max_length=100)
    author = forms.ModelChoiceField(label='Автор', queryset=models.Author.objects.all())




class CommentForm(forms.Form):
    author = forms.ModelChoiceField(label='Автор', queryset=models.Author.objects.all())
    article = forms.ModelChoiceField(label='Статья', queryset=models.Article.objects.all())
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea)

