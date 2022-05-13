from unicodedata import name
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request, shopName):
    shop = Shop.objects.get(name = shopName)
    print(shop)
    context = {
        'shop': shop
    }
    return render(request, 'shop/index.html', context)