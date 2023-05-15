from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    Category = models.ForeignKey(Category, on_delete= models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.quantity} x {self.product} 1'

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    address = models.TextField(default=None)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    phonenumber = models.TextField() #restriction
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.customer
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.product
