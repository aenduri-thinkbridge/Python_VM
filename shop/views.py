from django.contrib import messages
from django.contrib.auth.decorators import login_required
from urllib.parse import unquote
 #to remove %20 in the product name 

from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import render,redirect,get_object_or_404
from .models import Brand,Category,Product
from django.contrib.auth import authenticate,login as auth_login,logout

def navbar_items(request):
      brand_items = Brand.objects.all()
      category_items = Category.objects.all()
      context = {'brand_items': brand_items, 
                        'category_items': category_items, 
                        }
      return context
     
def signup(request):
    if request.method == 'POST':
        print('hello')
        username =  request.POST['username']
        email =  request.POST['email']
        password =  request.POST['password']
        c_password = request.POST['confirm_password']
        if (password == c_password):
            print('sucess')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.info(request,"you have created a new account")
            return redirect(login)
        else:
           messages.info(request,"password does not match")
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
            username =  request.POST['username']
            password =  request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request,user)
                print("logged in user")
                messages.info(request,"you have logged in succesfully")
                return redirect(homepage)
            else:
                messages.info(request,"username or password incorrect")
    return render(request, 'login.html')

@login_required(login_url="/login/")
def homepage(request):
    brand = Brand.objects.all()
    category = Category.objects.all()
    products = Product.objects.all()
    context = {'brands': brand, 
               'categories': category, 
                'products': products}
    context.update(navbar_items(request))
    return render(request, 'homepage.html',context)

@login_required(login_url="/login/")
def Brandpages(request,nm):
    brand = Brand.objects.get(name=nm)
    products = Product.objects.filter(brand=brand)
    context = {'products':products}
    context.update(navbar_items(request))
    return render(request, 'brand.html',context)


@login_required(login_url="/login/")
def Categorypage(request,nm):
    category = Category.objects.get(name=nm)
    products = Product.objects.filter(Category=category)
    context = {'products':products}
    context.update(navbar_items(request))
    return render(request, 'category.html',context)

@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect(login)

def product_view(request,nm):
    product= get_object_or_404(Product,name=nm)
    print(product.id)
    context = {'product':product}
    context.update(navbar_items(request))
    return render(request, 'product.html',context)