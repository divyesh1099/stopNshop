from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    return render(request, 'users/index.html')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        try:
            profile = Profile.objects.get_or_create(user = request.user)[0]
        except Exception as e:
            print("Following error occured :", e)
        if request.FILES:
            image = request.FILES["image"]
            profile.image = image
            profile.save()
        if request.POST["first_name"]:
            first_name = request.POST["first_name"]
            user.first_name = first_name
            user.save()
        if request.POST["last_name"]:
            last_name = request.POST["last_name"]
            user.last_name = last_name
            user.save()
        if request.POST["email"]:
            email = request.POST["email"]
            user.email = email
            user.save()
        if request.POST["phonenumber"]:
            phonenumber = request.POST["phonenumber"]
            profile.phonenumber = phonenumber
            profile.save()
        if request.POST["state"]:
            state = request.POST["state"]
            profile.state = state
            profile.save()
        if request.POST["zip_code"]:
            zip_code = request.POST["zip_code"]
            profile.zip_code = zip_code
            profile.save()
        if request.POST["city"]:
            city = request.POST["city"]
            profile.city = city
            profile.save()
        if request.POST["address"]:
            address = request.POST["address"]
            profile.address = address
            profile.save()

        return render(request, 'users/index.html')
        # form = EditProfileForm(request.POST, instance=request.user)
        # profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)  # request.FILES is show the selected image or file

        # if form.is_valid() and profile_form.is_valid():
            # user_form = form.save()
            # custom_form = profile_form.save(False)
            # custom_form.user = user_form
            # custom_form.save()
            # return render(request, 'users/index.html')
        # return render(request, 'users/index.html')
        
    else:
        profile = Profile.objects.get_or_create(user = request.user)[0]
        context = {
            "profile":profile
        }
        # form = EditProfileForm(instance=request.user)
        # profile_form = ProfileForm(instance=request.user.profile)
        # args = {}
        # args.update(csrf(request))
        # args['form'] = form
        # args['profile_form'] = profile_form
        return render(request, 'users/edit_profile.html', context)

# @login_required
# def edit_profile_image(request):
#     if request.method == 'POST' and request.FILES['image']:
#         try:
#             profile = Profile.objects.get_or_create(user = request.user)[0]
#         except Exception as e:
#             print("Following error occured :", e)
#         image = request.FILES["image"]
#         profile.image = image
#         profile.save()
#         return render(request, 'users/index.html')
#     return render(request, 'users/index.html')

@login_required
def delete(request):
    try:
        user = User.objects.get(username = request.user.username)
        user.delete
    except Exception as e:
        print("User delete error is ", e)
        logout(request)
        return render(request, 'home/login.html')
    return render(request, 'home/signup.html')