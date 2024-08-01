from rest_framework import serializers

from main.models import Manufacturer


class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


# class ManufacturerSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    description = serializers.CharField()
    image = serializers.ImageField()
    brand = BrandSerializer()
    # manufacturer = ManufacturerSerializer(many=True)



class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


    def create(self, validated_data):
        return Manufacturer.objects.create(**validated_data)