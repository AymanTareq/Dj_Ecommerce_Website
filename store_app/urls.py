from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='home'),
    path('cart/', views.cart, name='cart'),
    path('store/', views.store, name='store'),
    path('checkout/', views.checkout, name='checkout'),

    path('update_item/',views.updateItem,name='update-item'),
    path('process-order/',views.placeOrder,name='process-order'),

]