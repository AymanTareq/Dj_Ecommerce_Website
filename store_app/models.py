from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True,blank=True)
    digital = models.BooleanField(default=False,null=True,blank=False)

    def __str__(self):
        return self.name
        
    @property
    def image_url(self):
        try:
            img_url = self.image.url
        except:
            img_url = ''
        return img_url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def is_shipping(self):
        shipping = False
        orderItems = self.orderitem_set.all()
        for item in orderItems:
            if item.product.digital == False:
                shipping = True
        return shipping

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True)
    order  = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order  = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    address = models.CharField(max_length=512,null=False)
    city = models.CharField(max_length=25,null=False)
    state = models.CharField(max_length=25,null=False)
    zipcode = models.CharField(max_length=10,null=False)
    country = models.CharField(max_length=25,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address






