from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from artworks.models import Category, Artists, Artwork


def add_to_basket(request, sales_id):
    """add specified art to the shopping basket"""

    artwork = get_object_or_404(Artwork, pk=sales_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    if sales_id in list(basket.keys()):
        basket[sales_id] += quantity
        messages.success(
            request, f'Added {artwork.title} to {basket[sales_id]}')

    else:
        basket[sales_id] = quantity
        messages.success(request, f'Added {artwork.title} to your basket')
    request.session['basket'] = basket
    return redirect(redirect_url)


# Create your views here.
def view_basket(request):
    # A view to return the basket

    return render(request, 'basket/basket.html')
