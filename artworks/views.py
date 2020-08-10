from django.shortcuts import render
from .models import Artwork
# Create your views here.


def gallery(request):
    # Shows galery view of all art
    artworks = Artwork.objects.all()

    context = {
        'artworks': artworks,
    }
    return render(request, 'artworks/gallery.html', context)
