from django.contrib import admin
from .models import Artwork, Category


# Register your models here.
class ArtworkAdmin(admin.ModelAdmin):
    """
    Display fields for Artworks in Admin view
    """
    list_display = (
        'title',
        'artist',
        'category',
        'price',
        'date',
        'qty',
        'sold',
        'framed',
        'id',
        'pk'
    )
    ordering = ('artist',)


class CategoryAdmin(admin.ModelAdmin):
    """Display fields for Categories in Admin view"""
    list_display = (
        'friendly_name',
        'name',
        'id',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)
