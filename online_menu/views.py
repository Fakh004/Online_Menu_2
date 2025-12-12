from django.http import HttpResponse
from .models import ContactMessage, Dish, Order
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home_page(request):
    # select * from tasks
    categories = ['starter', 'main', 'dessert', 'drink']
    menu = {category: Dish.objects.filter(category=category) for category in categories} 
    return render(request, 'home.html', {'menu': menu})

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
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

def add_dish(request):
    if not request.user.is_authenticated:
        return render(request, 'message.html')
    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')  
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        if not dish_name or not description or not price or not category:
            return HttpResponse('All fields are required!')

        Dish.objects.create(
            dish_name=dish_name,  
            description=description,
            price=price,
            category=category,
            image=image
        )
        return redirect('dish_list')
    return render(request, 'add_dish.html')

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'dish_list.html', {'dishes': dishes})



def dish_edit(request, dish_id):
    if request.method == 'GET':
        dish = Dish.objects.get(id=dish_id)
        return render(request, 'edit_dish.html', {'dish': dish})
    elif request.method == 'POST':
        dish = Dish.objects.get(id=dish_id)
        dish.dish_name = request.POST.get('dish_name', dish.dish_name)
        dish.description = request.POST.get('description', dish.description)
        dish.price = request.POST.get('price', dish.price)
        dish.category = request.POST.get('category', dish.category)
        if 'image' in request.FILES:
            dish.image = request.FILES.get('image')
        dish.save()
        return redirect('home_name')
    
def dish_delete(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    if not dish:
        return HttpResponse('Dish not found!')
    if request.method == 'GET':
        return render(request, 'confirm_delete.html', {'dish': dish})
    elif request.method == 'POST':
        dish.delete()
        return redirect('dish_list')
    
def order_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders = Order.objects.all()
    if request.method == 'GET':
        return render(request, 'order.html', {'orders': orders})
    elif request.method == 'POST':
        quantity = request.POST.get('quantity')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if not name or not quantity or not phone or not address:
            return HttpResponse('All fields are required!')

        Order.objects.create(
            quantity=quantity,
            name=name,
            phone=phone,
            address=address
        )
        return redirect('order_success')
    return render(request, 'order.html', {'orders': orders})

def order_success(request):
    return render(request, 'order_success.html')