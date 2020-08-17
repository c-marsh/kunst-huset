from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'user',
        'is_artist',
        'is_customer',
        
    )

admin.site.register(UserProfile, UserProfileAdmin)