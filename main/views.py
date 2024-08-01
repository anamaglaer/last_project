from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from main.form import AddCar, RegistrationForm, LoginForm, NewPasswordForm, NewLoginForm
from main.models import Car, Brand, Manufacturer
from cart.forms import AddProductForm

from django.shortcuts import render, redirect
from django.contrib import messages

from orders.models import Order


# Create your views here.
def get_page(request):
    cars = Car.objects.select_related('brand').all()
    brand = Brand.objects.all()
    context = {
        'cars': cars,
        'brand': brand

    }
    return render(request, 'main.html', context)


def get_add_car(request):
    forms = AddCar()
    car_all = Car.objects.all()
    if request.method == 'POST':
        forms = AddCar(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()

    context = {
        'car_all': car_all,
        'forms': forms

    }
    return render(request, 'add_car.html', context)


def detail(request, id):
    car = Car.objects.get(id=id)
    form = AddProductForm()

    context = {
        'car': car,
        'form': form,
    }
    return render(request, 'detail.html', context)


def page_add_car(request):
    forms = AddCar()
    context = {
        'forms': forms
    }
    return render(request, 'add_car.html', context)

# def get_brand(request):
#     print(request.GET)
#     brand = Brand.objects.all()
#     brand_car = Car.objects.filter(brand=request.GET.get('brand'))
#     context = {
#         'cars': brand_car,
#         # 'brand': brand
#     }
#     return render(request, 'brand.html', context)


def get_manuf(request):
    print(request.GET)
    brand_car = Car.objects.filter(brand=request.GET.get('brand'))
    brand = Brand.objects.all()
    manuf = Car.objects.filter(manufacturer__in=request.GET.getlist('manufacturer'))
    manufacturer = Manufacturer.objects.all()

    context = {
            'cars': brand_car if brand_car else manuf,
            # 'brand': brand,
            # 'manufacturer': manufacturer
        }
    return render(request, 'brand.html', context)

def search_result(request):
    results = Car.objects.filter(brand__title__icontains=request.GET.get('search')) | Car.objects.filter(description__icontains=request.GET.get('search'))
    # results = Car.objects.filter(description__icontains=request.GET.get('search'))
    context = {
        'cars': results
    }
    return render(request, 'search_result.html', context)

# def registration(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
#
#     context = {
#         'form': form
#     }
#     return render(request, 'registration.html', context)


def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)


def login_user(request):
    form = LoginForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Пользователь с такими данными не найден'
                context = {
                    'form': form,
                    'error_message': error_message
                }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def kabinet(request):
    new_log = NewLoginForm(initial={'user': request.user.username})
    pass_form = NewPasswordForm()
    context = {
        'log_form': new_log,
        'pass_form': pass_form,

    }
    if request.method == 'POST':
        new_log = NewLoginForm(request.POST)
        pass_form = NewPasswordForm(request.POST)
        if request.POST.get('username'):
            if new_log.is_valid():
                user_log = request.user
                user_log.username = new_log.cleaned_data.get('username')
                user_log.save()
                context = {
                    'log_form': new_log,
                    'pass_form': pass_form,
                    'new_username': user_log,
                }
        if request.POST.get('password'):
            if pass_form.is_valid():
                user_pass = request.user
                user_pass.set_password(pass_form.cleaned_data.get('password'))
                user_pass.save()
                context = {
                    'log_form': new_log,
                    'pass_form': pass_form,
                    'new_username': user_pass,
                }
    return render(request, 'kabinet.html', context)


def my_orders(request):
    orders = Order.objects.filter(user_id=request.user.id)
    print(orders)
    context = {
        'orders': orders,
    }
    return render(request, 'kabinet.html', context)
