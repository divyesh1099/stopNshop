from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]