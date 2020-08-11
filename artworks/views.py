from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Artwork, Artists, Category
# Create your views here.


def gallery(request):
    # Shows gallery view of all art
    artworks = Artwork.objects.all()
    artists = Artists.objects.all()
    categories = Category.objects.all()
    query = None
    category = None


# Search return
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            artworks = artworks.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "You didn't enter any criteria!")
                return redirect(reverse('gallery'))
            # Search in fields
            queries = Q(title__icontains=query) | Q(
                description__icontains=query) | Q(medium__icontains=query)
            artworks = artworks.filter(queries)

    context = {
        'artists': artists,
        'categories': categories,
        'artworks': artworks,
        'search_term': query,
    }

    return render(request, 'artworks/gallery.html', context)


def art_detail(request, art_id):
    # Shows detailed view of specific art piece
    artwork = get_object_or_404(Artwork, pk=art_id)
    artists = Artists.objects.all()
    categories = Category.objects.all()

    context = {
        'artists': artists,
        'categories': categories,
        'artwork': artwork,
    }

    return render(request, 'artworks/art_detail.html', context)
