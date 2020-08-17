
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_details/<user_id>', views.edit_profile, name='edit_profile'),
    path('edit_artist/<user_id>', views.edit_artist, name='edit_artist'),
    path('edit_selector/<user_id>', views.edit_selector, name='edit_selector'),
    path('public_profile/<user_id>', views.public_profile, name='public_profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]
