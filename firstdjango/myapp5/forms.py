import datetime

from django import forms


class ProductForm(forms.Form):
    name_product = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите название продукта'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание продукта'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField()
    image = forms.ImageField()
