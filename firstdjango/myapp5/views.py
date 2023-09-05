from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from datetime import datetime
import logging

import datetime
from datetime import date, timedelta
from . import models
from . import forms
from django.core.files.storage import FileSystemStorage


def get_orders(request, client_id):
    title = "Заказы клиента"
    orders = models.Order.objects.filter(customer__pk=client_id)
    # print(len(orders))
    context = {'title': title, 'orders': orders}
    return render(request, 'myapp5/orders.html', context)


def get_order(request, orders_id):
    title = "Продукты внутри заказа"
    order = models.Order.objects.filter(pk=orders_id).first()
    products = models.Product.objects.filter(order=order)
    # print(len(products))
    context = {'title': title, 'order': order, 'products': products}
    return render(request, 'myapp5/order.html', context)


def get_product(request, product_id):
    title = "Описание продукта"
    product = models.Product.objects.filter(pk=product_id).first()
    # print(len(products))
    context = {'title': title, 'product': product}
    return render(request, 'myapp5/product.html', context)


def get_all_products_client(request, client_id):
    today = datetime.date.today()
    title = f"Товары приобретенные клиентом {client_id}"
    # orders = Order.objects.filter(customer__pk=client_id, date_ordered=today)
    orders = models.Order.objects.filter(customer__pk=client_id)
    print(orders)
    products1 = []

    for order in orders:
        # products = Product.objects.filter(date_ordered=today)
        products = models.Product.objects.filter(order=order)
        # print(order.date_ordered)

        for prod in products:
            # print(prod.date_up_product)
            products1.append(prod)
    products = list(set(products1))
    # print(products)

    context = {'title': title, 'products': products}
    return render(request, 'myapp5/products.html', context)


def client_orders(request, client_id):
    cont = {}
    for order in models.Order.objects.all():
        if order.customer.id == client_id:
            client_name = order.customer.name
            pr_list = []
            for product in order.products.all():
                pr_list.append(product.name_product)
            cont[f'Заказ № {order.id}'] = pr_list
    context = {'orders': cont, 'client': client_name}
    return render(request, 'myapp5/client_orders.html', context)


def client_orders_period(request, client_id, period):
    time = date.today() - timedelta(days=period)
    cont = {}
    for order in models.Order.objects.all():
        # print(order.date_ordered)
        if order.date_ordered >= time:
            if order.customer.id == client_id:
                client_name = order.customer.name
                product_list = []
                for product in order.products.all():
                    if product.name not in product_list:
                        product_list.append(product.name)
    context = {'product_list': product_list, 'client': client_name, 'period': period}
    return render(request, 'myapp5/client_orders_period.html', context)


def product_form(request):
    message = 'Добавление продкта'
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        message = 'Добавление продкта: ошибка в данных'
        if form.is_valid():
            name_product = form.cleaned_data['name_product']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()

            product = models.Product(name_product=name_product,
                                     description=description,
                                     price=price, count=count,
                                     image=image)

            product.save()
            message = f'Продукт {product} успещно добавлен'
            form = forms.ProductForm()

    else:
        form = forms.ProductForm()
        message = 'Добавление продкта: заполните форму'
    return render(request, 'myapp5/product_form.html', {'form': form, 'message': message})


def edit_product_form(request, id):
    message = 'Изменение продкта: заполните форму'
    product = models.Product.objects.get(id=id)
    # image_product = models.Gallery.objects.get(product_id=id).first()
    if request.method == 'POST' and 'FILES':
        product.name_product = request.POST.get('name_product')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.count = request.POST.get('count')
        product.image = request.FILES.get('image')
        fs = FileSystemStorage()

        if product.image:
            product.save()
        else:
            product.save(update_fields=["name_product", 'description', 'price', 'count'])

        message = f'Продукт {product} успещно изменён'
        return HttpResponse(f'<h1>{message}</h1>')
    else:
        message = 'Изменение продкта: заполните форму'
        return render(request, 'myapp5/edit_product_form.html',
                      {'product': product, 'message': message})
