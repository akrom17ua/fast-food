from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    preparation_time = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    estimated_delivery_time = models.DateTimeField()
    distance = models.PositiveIntegerField()
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f'Order {self.id} by {self.user.name}'


