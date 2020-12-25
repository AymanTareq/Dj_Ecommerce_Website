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
    price = models.FloatField()
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

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True)
    order  = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name + '\t' + str(self.order.id)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order  = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    address = models.CharField(max_length=512,null=False)
    city = models.CharField(max_length=25,null=False)
    state = models.CharField(max_length=25,null=False)
    zipcode = models.CharField(max_length=10,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address






