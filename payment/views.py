from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from cart.models import Item
from order.models import *
from cart.models import *
import razorpay
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    order = Order.objects.filter(user = request.user).last()
    items = Item.objects.all()
    total_in_paise = order.amount.total *100
    context = {
        "order": order,
        "items": items,
        "total_in_paise": total_in_paise,
    }
    if request.method == 'POST':
        client = razorpay.Client(auth=("rzp_test_C3J7evdYwRoSAs", "BcybRfQTm3EoB5fygqz2DihF"))
        DATA = {
            "amount": 100,
            "currency": "INR",
        }
        client.order.create(data=DATA)

    return render(request, 'payment/index.html', context)

@csrf_exempt
def payment_success(request, generated_order_id):
    items = Item.objects.all()
    for item in items:
        product = Product.objects.get(name = item.name.name)
        variation = Variation.objects.filter(name = item.variation.name)[0]
        variation.stock = variation.stock - item.quantity
        variation.save()
        product.save()
        
    Item.objects.all().delete()
    try:
        order = Order.objects.get(generated_order_id = generated_order_id)
        order.paid = True
        order.save()
    
    except Exception as e:
        print("Order pair error is ", e)
    return render(request, 'payment/payment_success.html')