from django.db import models

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