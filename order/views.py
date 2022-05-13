from django.db.models.query_utils import PathInfo
from django.shortcuts import render
from cart.models import Item
from django.contrib.auth.decorators import login_required
from .models import Order
from product.models import Shipping
from offer.models import Offer
import math
# Create your views here.

@login_required
def index(request):
    items = Item.objects.all()
    if request.method == "POST":
        user = request.user
        phonenumber = request.POST["phonenumber"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zip"]
        dispatched = False
        delivered = False
        paid = False

        # Claculate order total 
        items = Item.objects.all()
        subtotal = 0
        shipping = Shipping.objects.get().shipping
        total = 0
        discount = 0
        # Discount Calculation 
        for item in items:
            discount += (item.price * item.quantity * item.name.offer.discount / 100)
    
        for item in items:
            subtotal += (item.price * item.quantity)

        total = math.ceil(subtotal - discount + shipping)
        # try:
        #     offers = Offer.objects.all()
        #     for offer in offers:
        #         products = offer.product.all()
        #         for item in items:
        #             for product in products:
        #                 if str(item) == str(product):
        #                     max_discount = 0
        #                     if max_discount<offer.discount:
        #                         max_discount = offer.discount
        #                     discount_in_percent = max_discount      
        # except:
        #     discount_in_percent = 0
        # for item in items:
        #     subtotal += (item.name.price * item.quantity)
        # discount = ((subtotal)*discount_in_percent)/100 
        # total = math.ceil(subtotal- discount+ shipping)
        if total <1:
            total = 1
        total_in_paise = total*100
        amount = total
        try:
            new_order = Order.objects.create(user = user,phonenumber = phonenumber, address = address, city = city, state = state, zip = zip_code, amount = amount, dispatched = dispatched, delivered = delivered, paid = paid)
            for product in items:
                new_order.products.add(product.name.id)
            new_order.save()
        except Exception as e:
            print("The following error occured", e)
        order = new_order
        items = Item.objects.all()
        context = {
            "order": order,
            "items": items,
            "total_in_paise": total_in_paise,
        }
        return render(request, 'payment/index.html', context)

    return render(request, 'order/index.html')

@login_required
def history(request):
    orders = Order.objects.filter(user = request.user)
    context = {
        "orders": orders,
    }
    return render(request, 'order/history.html', context)

@login_required
def delete(request, generated_order_id):
    orders = Order.objects.filter(user = request.user)
    context = {
        "orders": orders,
    }
    try:
        Order.objects.filter(generated_order_id = generated_order_id).delete()
    except Exception as e:
        print("Cannot delete order because ", e)
    return render(request, 'order/history.html', context)

@login_required
def cancel(request, generated_order_id):
    orders = Order.objects.filter(user = request.user)
    context = {
        "orders": orders,
    }
    try:
        order = Order.objects.filter(generated_order_id = generated_order_id)[0]
        order.cancelled = True
        order.save()
    except Exception as e:
        print("Cannot cancel order because ", e)
    return render(request, 'order/history.html', context)