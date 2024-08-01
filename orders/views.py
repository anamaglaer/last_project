from django.shortcuts import render

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem, Order


# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = Order(user=None if request.user.is_anonymous else request.user, **form.cleaned_data)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item.get('product'),
                                         price=item.get('price'),
                                         quantity=item.get('quantity'))
            cart.clear()
            context = {
                'order': order,
            }
            return render(request, 'created.html', context)
    else:
        form = OrderCreateForm

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)