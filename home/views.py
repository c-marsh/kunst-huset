from django.shortcuts import render
import random
from artworks.models import Category
from profiles.models import UserProfile


# Create your views here.
def index(request):
    """
    Return homepage
    """
    categories = Category.objects.all()
    items = UserProfile.objects.all()

    random_item = random.choice(items)
    context = {
        'categories': categories,
        'artist': random_item
    }

    return render(request, 'home/index.html', context)
