from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('history', views.history, name = 'history'),
    path('cancel/<str:generated_order_id>', views.cancel, name = 'cancel'),
    path('delete/<str:generated_order_id>', views.delete, name = 'delete'),
]