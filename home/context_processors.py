from product.models import Type
from offer.models import Offer
from cart.models import Item

def get_categories(request):
    categories = Type.objects.all()
    return {
        'categories': categories,
    }

def get_offers(request):
    offers = Offer.objects.all()
    return {
        'offers': offers,
    }

def get_cart_items(request):
    number_of_items_in_cart = len(Item.objects.all())
    return {
        'number_of_items_in_cart':number_of_items_in_cart,
    }