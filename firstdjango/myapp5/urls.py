from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('orders/<int:client_id>/', views.get_orders, name='orders'),
    path('order/<int:orders_id>/', views.get_order, name='order'),
    path('product/<int:product_id>/', views.get_product, name='product'),
    path('products/<int:client_id>/', views.get_all_products_client, name='products'),
    path('client_orders/<int:client_id>', views.client_orders, name='client_orders'),
    path('product_form', views.product_form, name='product_form'),
    path('edit_product_form/<int:id>', views.edit_product_form, name='edit_product_form'),
    path('client_orders_period/<int:client_id>/<int:period>', views.client_orders_period, name='client_orders_period'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)