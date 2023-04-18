from django.shortcuts import render
from .models import Brand,Category,Product


def navbar_items(request):
      brand_items = Brand.objects.all()
      category_items = Category.objects.all()
      context = {'brand_items': brand_items, 
                        'category_items': category_items, 
                        }
      return context
     

def homepage(request):
    brand = Brand.objects.all()
    category = Category.objects.all()
    products = Product.objects.all()
    context = {'brands': brand, 
               'categories': category, 
                'products': products}
    context.update(navbar_items(request))
    return render(request, 'homepage.html',context)

def Brandpages(request,nm):
    brand = Brand.objects.get(name=nm)
    products = Product.objects.filter(brand=brand)
    context = {'products':products}
    context.update(navbar_items(request))
    return render(request, 'brand.html',context)


def Categorypage(request,nm):
    category = Category.objects.get(name=nm)
    products = Product.objects.filter(Category=category)
    context = {'products':products}
    context.update(navbar_items(request))
    return render(request, 'category.html',context)

