from django.contrib import admin

from .models import Food, Customer, Order

admin.site.register(Food)
admin.site.register(Customer)
admin.site.register(Order)
