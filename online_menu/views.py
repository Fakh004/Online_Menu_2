from django.http import HttpResponse
from .models import ContactMessage, Dish, Order
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home_page(request):
    # select * from tasks
    categories = ['starter', 'main', 'dessert', 'drink']
    menu = {category: Dish.objects.filter(category=category) for category in categories} 
    return render(request, 'home.html', {'menu': menu})

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        message = request.POST.get('message')

        if sender_name and sender_email and message:
            ContactMessage.objects.create(
                sender_name = sender_name,
                sender_email = sender_email,
                message = message 
            )
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('contact')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля.')

    return render(request, 'contact.html')

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
    return redirect('login')


def order_page(request):
    if request.method == 'GET':
        dishes = Dish.objects.all()
        return render(request, 'order.html', {'dishes': dishes})
    elif request.method == 'POST':
        quantity = request.POST.get('quantity')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if not name or not quantity or not phone or not address:
            return HttpResponse('All fields are required!')

        return redirect('order_success')
    
def detail_dish(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    return render(request, 'dish_detail.html', {'dish': dish})