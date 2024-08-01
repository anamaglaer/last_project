from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.serializers import CarSerializer, ManufacturerSerializer
from main.models import Car, Manufacturer


# Create your views here.


@api_view(['GET', 'POST'])
# @api_view(['POST'])
def get_car_list(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(request.data)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def manufacturer(request):
    manufacturer_queryset = Manufacturer.objects.all()
    serializer = ManufacturerSerializer(manufacturer_queryset, many=True)
    if request.method == 'POST':
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # raise_exception=True если данные не валидны - выдаст ошибку
            # new_manufacturer = Manufacturer(**serializer.validated_data)
            # new_manufacturer.save()
            serializer.save()

    return Response(serializer.data)



class SearchProductView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        data = self.request.query_params
        queryset = Car.objects.filter(brand__title__icontains=data.get('brand'))

        return queryset
