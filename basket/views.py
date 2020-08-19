from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from artworks.models import Artwork


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

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Added {artwork.title} to {basket[item_id]}.' +
                      'Please make sure your' +
                      ' basket total is not more than the quantity available.')

    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {artwork.title} to your basket')
    request.session['basket'] = basket
    return redirect(redirect_url)


def view_basket(request):
    """
    A view to return the basket
    """

    return render(request, 'basket/basket.html')
