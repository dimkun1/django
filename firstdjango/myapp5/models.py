from django.db import models


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    nummer_tel = models.IntegerField()
    address = models.TextField()
    date_registration = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.nummer_tel}'


class Product(models.Model):
    name_product = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date_up_product = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_product} {self.description}, цена {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.total_price} {self.date_ordered}'
