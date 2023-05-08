from django.contrib import admin
from .models import Product,Category,Brand,Cart,costumers,Order

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(costumers)
admin.site.register(Order)


