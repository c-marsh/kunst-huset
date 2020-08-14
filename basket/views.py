from django.shortcuts import get_object_or_404, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from artworks.models import Category, Artists, Artwork


def remove_basket(request, item_id):
    """remove specified art in the shopping basket"""

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        del basket[item_id]

        messages.success(request, 'removed item to your basket')
        request.session['basket'] = basket
        return redirect(reverse('view_basket'))


def add_to_basket(request, item_id):
    """add specified art to the shopping basket"""

    artwork = get_object_or_404(Artwork, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    # while basket[item_id] <= artwork.qty:
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Added {artwork.title} to {basket[item_id]}')

    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {artwork.title} to your basket')
    request.session['basket'] = basket
    return redirect(redirect_url)
    # basket[item_id] = quantity
    # messages.error(request, f'Not enough of {artwork.title} on sale')
    # request.session['basket'] = basket
    # return redirect(redirect_url)


# Create your views here.
def view_basket(request):
    # A view to return the basket

    return render(request, 'basket/basket.html')
