from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<int:art_id>/', views.art_detail, name='art_detail'),
    path('add/', views.add_art, name='add_art'),
]
