from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', views.SuccessView.as_view()),  
    path('cancelled/', views.CancelledView.as_view()),  
]
