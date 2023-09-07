from django.contrib import admin
from myapp4.models import Author, Article, Comment


# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'birthday']
    ordering = ['birthday']
    list_filter = ['firstname', 'lastname']
    search_fields = ['biography']
    search_help_text = 'Поиск по полю Описание продукта (biography)'
    # actions = [reset_quantity]
    fields = ['firstname', 'lastname', 'email', 'biography', 'birthday']



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'public_date', 'author', 'category']
    ordering = ['count']
    list_filter = ['public', 'category']
    search_fields = ['text']
    search_help_text = 'Поиск по полю Описание продукта (text)'
    # actions = [reset_quantity]
    fields = ['title', 'text', 'public_date', 'author', 'category', 'count', 'public']



class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'article']
    ordering = ['create_date']
    list_filter = ['author', 'article']
    search_fields = ['comment']
    search_help_text = 'Поиск по полю Описание продукта (comment)'
    # actions = [reset_quantity]
    fields = ['author', 'article', 'comment', 'create_date', 'update_date']





admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
