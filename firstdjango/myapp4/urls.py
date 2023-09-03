from django.urls import path
from .views import cube, rand100, coin
from .views import get_articles, get_article, get_comment
# from .views import hello, HelloView
# from .views import year_post, MonthPost, post_detail
# from .views import my_view
# from .views import TemplIf
# from .views import view_for
# from .views import index, about
# from .views import author_posts, post_full

urlpatterns = [
    path('cube/', cube, name='cube'),
    path('coin/', coin, name='coin'),
    path('rand100/', rand100, name='rand100'),
    path('articles/<int:author_id>/', get_articles),
    path('article/<int:article_id>/', get_article, name='article'),
    path('comment/<int:comment_id>/', get_comment, name='comment'),
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
