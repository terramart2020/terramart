from django.shortcuts import render
from product.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'main/home.html', {'products':products})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def terms(request):
    return render(request, 'main/terms.html')