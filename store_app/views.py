import json
from django.shortcuts import render
from django.http import JsonResponse
import datetime
from .models import *


def store(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    context = {'items':items,'order':order,'products':products,'cartItems':cartItems}
    return render(request, 'store_app/store.html', context=context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = 0

    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request, 'store_app/cart.html', context=context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = 0

    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request, 'store_app/checkout.html', context=context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId',productId)
    print('action:',action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,status=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1 )
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1 )
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added tareq', safe=False)

def placeOrder(request):
    trxn_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,status=False)
        total = float(data['form']['total'])
        order.transaction_id = trxn_id

        if total == order.get_cart_total:
            order.status = True
        order.save()

        if order.is_shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
                country = data['shipping']['country'],
            )



    else:
        print('User not logged in.')


    print('Data:',request.body )
    return JsonResponse('payment submitted', safe=False)