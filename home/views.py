from django.shortcuts import render
from artworks.models import Category, Artists


# Create your views here.
def index(request):
    artists = Artists.objects.all()
    categories = Category.objects.all()

    context = {
        'artists': artists,
        'categories': categories,
    }

    return render(request, 'home/index.html', context)
