from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from category.models import Category
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def all_products(request):
    products = Product.objects.all()
    return render(request, 'product/all_products.html', {'products':products})

def view_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        categories = Category.objects.all()
        return render(request, 'product/view_product.html', {'product':product, 'form':form, 'categories':categories})
    else:
        try:
            form = ProductForm(request.POST, instance=product)
            form.save()
            return redirect('product:all_products')
        except ValueError:
            return render(request, 'product/view_product.html', {'product':product, 'form':form, 'error':'Bad input'})

# @login_required
def create_product(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'product/create_product.html', {'form':ProductForm(), 'categories':categories})
    else:
        try:
            form = ProductForm(request.POST, request.FILES)
            # myImage = request.FILES['image']
            # print()
            # fs = FileSystemStorage()
            # filename = fs.save(myImage.name, myImage)
            # uploaded_file_url = fs.url(filename)
            newProduct = form.save(commit=False)
            # newcategory.user = request.user
            # newProduct.image = myImage.name
            newProduct.save()
            return redirect('product:all_products')
        except ValueError:
            return render(request, 'product/create_product.html', {'form':ProductForm(), 'error':'Bad data passed in. Please try again'})
    