from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from artworks.models import Artwork


def basket_content(request):

    basket_items = []
    sub_total = 0
    items_count = 0
    basket = request.session.get('basket', {})

    for sales_id, quantity in basket.items():
        artwork = get_object_or_404(Artwork, pk=sales_id)
        sub_total += quantity * artwork.price
        items_count += quantity
        basket_items.append({
            'item_id': sales_id,
            'quantity': quantity,
            'artwork': artwork,
        })
    if sub_total < settings.FIXED_DELIVERY_THRESHOLD:
        delivery = sub_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    else:
        delivery = round(((200) + sub_total * Decimal(0.05)), 2)

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
