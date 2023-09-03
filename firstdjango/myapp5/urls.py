from django.urls import path
from .views import Client, Product, Order
from .views import get_orders, get_order, get_product, get_all_products_client, client_orders, client_orders_period
# from .views import year_post, MonthPost, post_detail
# from .views import my_view
# from .views import TemplIf
# from .views import view_for
# from .views import index, about



urlpatterns = [
    path('orders/<int:client_id>/', get_orders, name='orders'),
    path('order/<int:orders_id>/', get_order, name='order'),
    path('product/<int:product_id>/', get_product, name='product'),
    path('products/<int:client_id>/', get_all_products_client, name='products'),
    path('client_orders/<int:client_id>', client_orders, name='client_orders'),
    path('client_orders_period/<int:client_id>/<int:period>',
         client_orders_period, name='client_orders_period'),
    # path('comment/<int:comment_id>/', get_comment, name='comment'),
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
