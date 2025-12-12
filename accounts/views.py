from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if not username or not email or not password or not confirmPassword:
                return HttpResponse('ALL FIELDS ARE REQUIRED !!!')
    
        if password != confirmPassword:
                return HttpResponse("Passwords don't match!")
    
        if User.objects.filter(username=username).exists():
                return HttpResponse("Username already taken!")
    
        user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=name,
                last_name=surname
            )
        return redirect ('login')

def login_view(request):
    if request.method == 'GET':
        return render (request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home_name')
        else:
            return HttpResponse('Invalid username or password')

def logout_view(request):
    logout(request)
    return redirect('home_name')


