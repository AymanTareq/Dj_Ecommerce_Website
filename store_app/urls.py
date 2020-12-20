from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]