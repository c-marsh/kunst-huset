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


import json



def checkout(request):
    basket = request.session.get('basket', {})

    order_form = OrderForm()

    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('gallery'))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HFlKfIydNOawJAwaLoNwIaGlZQi4oqEEYhni7KNRyYDlsB1ISOtVpVrJ4m8WNKT9byeGDD3Y2ziT5Oq23q8RVsZ00u9YUvNik',
        'client_secret': 'test client secret',

    }

    return render(request, template, context)

