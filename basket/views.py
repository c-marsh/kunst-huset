from django.shortcuts import render
from artworks.models import Category, Artists


# Create your views here.
def view_basket(request):
    # A view to return the bag
    artists = Artists.objects.all() 
    categories = Category.objects.all()

    context = {
        'artists': artists,
        'categories': categories,
    }

    return render(request, 'basket/basket.html', context)
