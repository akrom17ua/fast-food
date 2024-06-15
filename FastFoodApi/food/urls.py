from django.urls import path
from .views import FoodList, OrderDetail

urlpatterns = [
    path('', FoodList.as_view(), name=''),
    path('<int:pk>/', OrderDetail.as_view(), name=''),
]