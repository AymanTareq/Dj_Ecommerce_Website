from django.shortcuts import render
from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store_app/store.html', context=context)

def cart(request):
    context = {}
    return render(request, 'store_app/cart.html', context=context)

def checkout(request):
    context = {}
    return render(request, 'store_app/checkout.html', context=context)