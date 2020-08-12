from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404


def basket_content(request):

    basket_items = []
    sub_total = 0
    items_count = 0

    if sub_total < settings.FIXED_DELIVERY_THRESHOLD:
        delivery = sub_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    else:
        delivery = Decimal(200 + sub_total * 0.005)
    insurance = Decimal(round(settings.INSURANCE_PERCENTAGE * sub_total, -1)) # set insurance value, round up to 10
    vat = Decimal(((insurance+sub_total+delivery)/100)*settings.VAT)
    grand_total = Decimal(delivery + sub_total + vat)

    context = {
        'basket_items': basket_items,
        'sub_total': sub_total,
        'items_count': items_count,
        'delivery': delivery,
        'insurance': vat,
        'vat': vat,
        'grand_total': grand_total,
    }
    return context
