from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_completed/<order_number>', views.checkout_completed,
         name='checkout_completed'),
]
