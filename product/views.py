from django import utils
from django.db.models.fields import related
from django.http.request import MediaType
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from cart.models import Item

# Create your views here.
def index(request, name):
    product = Product.objects.get(name = name)
    try:
        related_products = Product.objects.filter(type=product.type).exclude(name=name)[:2]
        context = {
            "product": product,
            "related_products": related_products,
        }
    except Exception as e:
        print("The Review Finding Error is ", e)

    if request.method == "POST":
        cart_product = request.POST["cart_product"]
        quantity = request.POST['quantity']
        try:
            generated_variation_id = request.POST['variation']
            variation = Variation.objects.get(generated_variation_id = generated_variation_id)
            new_size = variation.size
            new_color = variation.color
            new_price = variation.price
            new_product = variation.product
            if new_product in Item.objects.all():
                Item.objects.filter(name = new_product).update(quantity = quantity)
                Item.objects.filter(name = new_product).update(size = str(new_size))
                Item.objects.filter(name = new_product).update(color = new_color)
                Item.objects.filter(name = new_product).update(price = new_price)
                Item.objects.filter(name = new_product).update(variation = variation)
            else:
                try:
                    Item.objects.update_or_create(name=new_product, defaults={'quantity': quantity})
                    Item.objects.filter(name=new_product).update(size = str(new_size), color = new_color, price = new_price, variation = variation)
                except Exception as e:
                    print(e)
        except Exception as e:
            print("Variation Error is ", e)
        return redirect('cart:index')
    else:
        return render(request, 'product/index.html', context)