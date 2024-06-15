from django.shortcuts import render
from rest_framework import generics
from .serializers import FoodSerializer, OrderSerializer

from .models import Food, Customer, Order

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


