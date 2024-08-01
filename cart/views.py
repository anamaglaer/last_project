from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.forms import AddProductForm
from cart.cart import Cart
from main.models import Car


# Create your views here.
def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'cart_detail.html', context)



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Car, id=product_id)
    form = AddProductForm(request.POST)
    if form.is_valid():
        cart.add(product=product, quantity=form.cleaned_data.get('quantity'),
                 update_quantity=form.cleaned_data.get('update'))
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Car, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')
