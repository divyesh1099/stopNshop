from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.db import IntegrityError
from product.models import *
from .models import *
from users.models import *
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.conf import settings
from django.core.mail import send_mail
from users.models import Profile
from offer.models import *

# Create your views here.
def index(request):
    user = request.user
    try:
        Profile.objects.get_or_create(user = request.user)[0]
    except Exception as e:
        print("Profile Creation Error from home page is ", e)
    carousel_images = CarouselImage.objects.get_or_create()[0]
    offered_products =list()
    products = Product.objects.all()
    count = 0
    for product in products:
        if product.offer and count <7:
            offered_products.append(product)
            count += 1

    context = {
        'carousel_images': carousel_images,
        'offered_products': offered_products,
        }
    return render(request, 'home/index.html', context)

def all(request):
    products = Product.objects.all()
    sizes = ['36','38','40','42','44','46','48','50','S','M','L','XL','XXL','XXXL']
    paginator = Paginator(products, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    context = {
        "products": products,
        "sizes":sizes,
    }
    return render(request, 'home/all.html', context)

def gallery(request):
    gallery_list = Gallery.objects.all()
    gallery = list()
    for gallerie in gallery_list:
        gallery.append(Product.objects.get(name = gallerie))
    context = {
        'gallery': gallery
        }
    return render(request, 'home/gallery.html', context)

def categories(request):
    categories = Type.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'home/categories.html', context)

def category(request, category):
    categorie = get_object_or_404(Type, name = category)
    products = Product.objects.filter(type = categorie.id)
    paginator = Paginator(products, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    context = {
        'category': categorie,
        'products': products,
    }
    return render(request, 'home/category.html', context)

def my_login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "home/login.html", {
                "error": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html")

def my_logout(request):
    logout(request)
    return redirect("/")

def my_signup(request):
    customer_group = Group.objects.get_or_create(name='Customer')[0]

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password1"]
        confirmation = request.POST["password2"]
        if password != confirmation:
            return render(request, "home/signup.html", {
                "error": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.set_password(password)
            user.is_active=True
            user.is_staff=True
            customer_group.user_set.add(user)
            user.save()
            profile = Profile.objects.create(user = user)
            profile.save()
        except IntegrityError:
            return render(request, "home/signup.html", {
                "error": "Username already taken."
            })
        login(request, user)
        return redirect("/")
    else:
        return render(request, "home/signup.html")

def contactus(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message'] + " ---from--- " + name + " Email id: " + email
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_from]
        try:
            send_mail(subject, message, email_from, recipient_list)
        except Exception as e:
            print("Email error is ", e)
            return render(request, 'home/contactus.html', {
                'fail': "Failed, Try Again Later"
            })
        return render(request, 'home/contactus.html', {
            'success': "Thanks For contacting us."
        })

    return render(request, 'home/contactus.html')

def companyinformation(request):
    return render(request, 'home/companyinformation.html')