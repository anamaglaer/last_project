from orders.views import order_create
from django.urls import path



urlpatterns = [
    path('order_create/', order_create, name='order_create'),

]