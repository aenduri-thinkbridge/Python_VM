from django.contrib import admin
from .models import Product,Category,Brand,Cart,Customer,Order,OrderItem

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Order)


