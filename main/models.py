from django.db import models

# Create your models here.


class AdditionalCarImage(models.Model):
    image = models.ImageField(upload_to="additional_car_image")
    car = models.ForeignKey("Car", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car.brand} {self.car.model}'

class Car(models.Model):
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    manufacturer = models.ManyToManyField("Manufacturer")
    image = models.ImageField(upload_to="car_image", blank=True, null=True)

    def __str__(self):
        return f'{self.brand} {self.model}'

class Brand(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title







