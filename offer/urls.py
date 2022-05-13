from django.urls import path
from . import views
app_name = 'offer'
urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.all, name='all'),
]