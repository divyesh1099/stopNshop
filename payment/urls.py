from django.urls import path
from . import views
app_name = 'payment'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('payment_success/<str:generated_order_id>', views.payment_success, name = 'payment_success'),
]