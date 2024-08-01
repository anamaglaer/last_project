from django.contrib import admin

from main.models import Car, AdditionalCarImage, Brand, Manufacturer

# Register your models here.
admin.site.register(Car)
admin.site.register(AdditionalCarImage)
admin.site.register(Brand)
admin.site.register(Manufacturer)
