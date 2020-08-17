from django.contrib import admin
from .models import Artwork, Category#, Artists

# Register your models here.
class ArtworkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'artist',
        'category',
        'price',
        'date',
        'qty',
        'sold',
        'framed',
        'image',
        'id',
    )

    ordering = ('artist',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'id',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)
# admin.site.register(Artists)
