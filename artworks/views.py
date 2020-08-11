from django.shortcuts import render, get_object_or_404
from .models import Artwork
# Create your views here.


def gallery(request):
    # Shows gallery view of all art
    artworks = Artwork.objects.all()

    context = {
        'artworks': artworks,
    }
    return render(request, 'artworks/gallery.html', context)


def art_detail(request, art_id):
    # Shows detailed view of specific art piece
    artwork = get_object_or_404(Artwork, pk=art_id)

    context = {
        'artwork': artwork,
    }
    return render(request, 'artworks/art_detail.html', context)
