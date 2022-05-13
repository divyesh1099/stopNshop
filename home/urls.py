from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('all', views.all, name= 'all'),
    path('login', views.my_login, name= 'login'),
    path('logout', views.my_logout, name= 'logout'),
    path('signup', views.my_signup, name = 'signup'),
    path('gallery', views.gallery, name= 'gallery'),
    path('contactus', views.contactus, name= 'contactus'),
    path('categories', views.categories, name = 'categories'),
    path('companyinformation', views.companyinformation, name= 'companyinformation'),
    # path('profile/view/', views.viewprofile, name = 'viewprofile'),
    # path('profile/edit/', views.editprofile, name = 'editprofile'),
    # path('profile/edit/profile_pic', views.editprofilepic, name = 'editprofilepic'),
    # path('profile/edit/change_password', views.editprofilepassword, name = 'editprofilepassword'),
    path('category/<str:category>', views.category, name = 'category'),
    ]