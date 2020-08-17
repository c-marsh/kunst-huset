from django.shortcuts import render
from artworks.models import Category#, Artists


# Create your views here.
def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'home/index.html', context)
