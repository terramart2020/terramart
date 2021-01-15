from django.shortcuts import render, get_object_or_404
from .models import Category

def signupuser(request):
    return render(request, '')

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'category/all_categories.html', {'categories':categories})