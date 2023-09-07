from django.contrib import admin
from myapp5.models import Product, Client, Order


# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_registration']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Описание продукта (name)'
    # actions = [reset_quantity]
    fields = ['name', 'email', 'nummer_tel', 'address', 'date_registration']
    readonly_fields = ['date_registration']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'price', 'count', 'date_up_product']
    ordering = ['count']
    list_filter = ['count', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    # actions = [reset_quantity]
    fields = ['name_product', 'description', 'price', 'count', 'image', 'date_up_product']
    readonly_fields = ['date_up_product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_price', 'customer', 'date_ordered']
    ordering = ['customer']
    list_filter = ['total_price']
    search_fields = ['products']
    search_help_text = 'Поиск по полю Описание продукта (products)'
    # actions = [reset_quantity]
    fields = ['customer', 'products', 'total_price', 'date_ordered']
    readonly_fields = ['date_ordered']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
