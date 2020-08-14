from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from artworks.models import Artwork
# from profiles.models import UserProfile
# from profiles.forms import UserProfileForm
from basket.contexts import basket_content

import stripe
import json


def checkout(request):
    # import keys
    stripe_public_key = settings.STRIPE_PK
    stripe_secret_key = settings.STRIPE_SK
    basket = request.session.get('basket', {})

    # if request.method == 'POST':
    #     basket = request.session.get('basket', {})
    #     form_data = {
    #         'full_name': request.POST['full_name'],
    #         'email': request.POST['email'],
    #         'phone_number': request.POST['phone_number'],
    #         'country': request.POST['country'],
    #         'postcode': request.POST['postcode'],
    #         'town_or_city': request.POST['town_or_city'],
    #         'street_address1': request.POST['street_address1'],
    #         'street_address2': request.POST['street_address2'],
    #         'county': request.POST['county'],
    #     }

    order_form = OrderForm()
        # if order_form.is_valid():
        #     order = order_form.save(commit=False)
        #     pid = request.POST.get('client_secret').split('_secret')[0]
        #     order.stripe_pid = pid
        #     order.original_basket = json.dumps(basket)
        #     order.save()
        #     for item_id, item_data in basket.items():
        #         try:
        #             artwork = Artwork.objects.get(id=item_id)
        #             if isinstance(item_data, int):
        #                 order_line_item = OrderLineItem(
        #                     order=order,
        #                     artwork=artwork,
        #                     quantity=item_data,
        #                 )
        #                 order_line_item.save()
        #         except Artwork.DoesNotExist:
        #             messages.error(request, (
        #                 "One of the items in your basket wasn't found in our database. "
        #                 "Please call us for assistance!")
        #             )
        #             order.delete()
        #             return redirect(reverse('view_basket'))

    # return message if bag is empty
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('gallery'))

    current_basket = basket_content(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    # warning in case public key not detected
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
