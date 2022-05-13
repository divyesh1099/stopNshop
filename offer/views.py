from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from product.models import Product

# Create your views here.
def index(request):
    return render(request, 'offer/index.html')

def all(request):
    all_products = Product.objects.all()
    products = list()
    for product in all_products:
        if product.offer:
            products.append(product)
    paginator = Paginator(products, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    context = {
        'products':products,
    }
    return render(request, 'home/all.html', context)