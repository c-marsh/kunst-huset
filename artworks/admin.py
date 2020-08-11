from django.contrib import admin
from .models import Artwork, Category, Artists

# Register your models here.
admin.site.register(Category)
admin.site.register(Artwork)
admin.site.register(Artists)
