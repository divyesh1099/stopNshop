from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('<str:name>', views.index, name = 'index'),
]

