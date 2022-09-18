from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemListView.as_view(), name='items'),

    path('items/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('create-checkout-session/<int:pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),


    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),  
    path('cancelled/', views.CancelledView.as_view()),  
]
