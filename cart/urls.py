from django.urls import path 
from . import views
app_name = 'cart'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('delete_item/<str:item>', views.delete_item, name = 'delete_item'),
]