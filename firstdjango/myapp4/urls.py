from django.urls import path
from . import views

urlpatterns = [
    path('cube/', views.cube, name='cube'),
    path('coin/', views.coin, name='coin'),
    path('rand100/', views.rand100, name='rand100'),
    path('articles/<int:author_id>/', views.get_articles),
    path('article/<int:article_id>/', views.get_article, name='article'),
    path('comment/<int:comment_id>/', views.get_comment, name='comment'),
    path('choice/', views.choice, name='choice'),
    path('author_form/', views.author_form, name='author_form'),
    path('article_form/', views.article_form, name='article_form'),
    path('comment_form/', views.comment_form, name='comment_form'),
    # path('comment_form/<int:post_id>/', views.comment_form, name='comment_form'),
    # path('posts/<int:year>/', year_post, name='year_post'),
    # path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    # path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    # path('', my_view, name='index'),
    # path('if/', TemplIf.as_view(), name='templ_if'),
    # path('for/', view_for, name='templ_for'),
    # path('index/', index, name='index'),
    # path('about/', about, name='about'),
    # path('author/<int:author_id>/', author_posts, name='author_posts'),
    # path('post/<int:post_id>/', post_full, name='post_full'),
]
