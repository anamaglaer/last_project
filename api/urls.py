from django.urls import path
from api.views import get_car_list, manufacturer, SearchProductView

urlpatterns = [
    path('get_car_list/', get_car_list),
    path('manufacturer/', manufacturer),
    path('search_product/', SearchProductView.as_view()),
]