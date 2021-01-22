from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'product/all_products.html', {'products':products})

def detail(request, product_id):
    return render(request, 'product/detail.html')
