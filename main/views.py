from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    return render(request, 'main/home.html', {'products':products})

@login_required
def about(request):
    return render(request, 'main/about.html')

@login_required
def contact(request):
    return render(request, 'main/contact.html')

@login_required
def privacy(request):
    return render(request, 'main/privacy.html')

@login_required
def terms(request):
    return render(request, 'main/terms.html')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match.'})
        else:
            login(request, user)
            return redirect('home')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'main/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == '' or request.POST['username'] == '':
            return render(request, 'main/signupuser.html', {'form':UserCreationForm(), 'error':'Username and password are required.'})
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('home')
                except IntegrityError:
                    return render(request, 'main/signupuser.html', {'form':UserCreationForm(), 'error':'The username is already been taken. Please choose a new username.'})
            else:
                return render(request, 'main/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

@login_required    
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        pass




