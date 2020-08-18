from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from artworks.models import Artwork
from profiles.models import UserProfile


def basket_content(request):
    """return basket contents"""
    basket_items = []
    sub_total = 0
    items_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        artwork = get_object_or_404(Artwork, pk=item_id)
        sub_total += quantity * artwork.price
        items_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'artwork': artwork,
        })
    if sub_total < settings.FIXED_DELIVERY_THRESHOLD:
        delivery = sub_total * Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    else:
        delivery = 200 + (Decimal((sub_total/500) *
                          settings.STANDARD_DELIVERY_PERCENTAGE))

    vat = Decimal(((sub_total+delivery)/100)*Decimal(settings.VAT))
    grand_total = Decimal(delivery + sub_total)

    context = {
        'basket_items': basket_items,
        'sub_total': sub_total,
        'items_count': items_count,
        'delivery': delivery,
        'vat': vat,
        'grand_total': grand_total,
    }
    return context
