from rest_framework import serializers
from .models import Food, Order

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Food


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Order