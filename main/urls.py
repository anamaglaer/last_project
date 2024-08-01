
from django.urls import path

from main.views import (get_page, page_add_car, get_manuf, detail, search_result, registration,
                        login_user, logout_user, kabinet, my_orders)

urlpatterns = [
    path('', get_page, name='home'),
    path('add_car/', page_add_car, name='add_car'),
    path('detail/<int:id>/', detail, name='detail'),
    # path('brand/', get_brand, name='brand'),
    path('manufacturer/', get_manuf, name='brand'),
    path('search_result/', search_result, name='search_result'),
    path('registration/', registration, name='registration'),
    path('login2/', login_user, name='login2'),
    path('logout_user', logout_user, name='logout_user'),
    path('kabinet', kabinet, name='kabinet'),
    path('my_orders', my_orders, name='my_orders')
]