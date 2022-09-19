from unicodedata import name
from django.urls import path

from orders.models import Order
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('orders/', views.ItemDetailView, name='pay_order'),
    path('order/<int:pk >', views.ItemDetailView, name='order_detail'),
]


