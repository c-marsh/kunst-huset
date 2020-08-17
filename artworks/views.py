from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Artwork, Category
# Create your views here.


def gallery(request):
    # Shows gallery view of all art
    artworks = Artwork.objects.all()
    categories = Category.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                artworks = artworks.annotate(lower_title=Lower('title'))
            # if sortkey == 'artist':
            #     sortkey = 'artist__name'
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            artworks = artworks.order_by(sortkey)


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
                description__icontains=query) | Q(
                    medium__icontains=query) | Q(artist__name__icontains=query)
            artworks = artworks.filter(queries)

    sorting = f'{sort}_{direction}'

    context = {
        'categories': categories,
        'artworks': artworks,
        'search_string': query,
        'sorting': sorting,
    }

    return render(request, 'artworks/gallery.html', context)


def art_detail(request, art_id):
    # Shows detailed view of specific art piece
    artwork = get_object_or_404(Artwork, pk=art_id)
    categories = Category.objects.all()
    template = 'artworks/art_detail.html'

    context = {
        'categories': categories,
        'artwork': artwork,
    }

    return render(request, template, context)
