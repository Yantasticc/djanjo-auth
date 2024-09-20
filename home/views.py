from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# test user: 
#     ID: jack
#     Passsword: Jack@2024

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
         
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login')
