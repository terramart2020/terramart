from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm

def signupuser(request):
    return render(request, '')

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'category/all_categories.html', {'categories':categories})

def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return render(request, 'category/detail.html', {'category':category, 'form':form})
    else:
        try:
            form = CategoryForm(request.POST, instance=category)
            form.save()
            return redirect('category:all_categories')
        except ValueError:
            return render(request, 'category/detail.html', {'category':category, 'form':form, 'error':'Bad input'})
    

# def detail(request, todo_pk):
#     todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
#     if request.method == 'GET':
#         form = TodoForm(instance=todo)
#         return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form})
#     else:
#         try:
#             form = TodoForm(request.POST, instance=todo)
#             form.save()
#             return redirect('currenttodos')
#         except ValueError:
#             return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form, 'error':'Bad info'})
