
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_details/<user_id>', views.edit_profile, name='edit_profile'),
    path('edit_artist/<user_id>', views.edit_artist_profile, name='edit_artist_profile'),
    path('edit_type/<user_id>', views.edit_profile_type, name='edit_profile_type'),
    # path('<int:user_id>', views.profile_detail, name='profile_detail'),
]
