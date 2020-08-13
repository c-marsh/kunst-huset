from django.shortcuts import get_object_or_404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from artworks.models import Category, Artists, Artwork


def remove_basket(request, sales_id):
    """remove specified art in the shopping basket"""

    try:
        basket = request.session.get('basket', {})

        basket.pop(sales_id)
        messages.success(request, f'removed {artwork.title} to your basket')
        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)


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
