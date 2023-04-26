from django.contrib import messages
from django.contrib.auth.decorators import login_required
 #to remove %20 in the product name 
from .models import costumers
from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import render,redirect,get_object_or_404
from .models import Brand,Category,Product,Cart
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

def logout_view(request):
    logout(request)
    return redirect(login)

def product_view(request,nm):
    product= get_object_or_404(Product,name=nm)
    print(product.id)
    context = {'product':product}
    context.update(navbar_items(request))
    return render(request, 'product.html',context)

@login_required(login_url='login')
def cart_view(request):
    cart = Cart.objects.filter(user=request.user)
    print(cart)
    total_price = sum([c.product.price * c.quantity for c in cart])
    total_items = sum([c.quantity for c in cart])
    context = {'cart':cart,'total_price':total_price,'total_items':total_items}
    context.update(navbar_items(request))
    return render(request, 'cart.html',context)
@login_required
def add_cart(request,nm):
    product = Product.objects.get(name=nm)
    quantity = request.POST.get('quantity',1)
    Cart.objects.create(user= request.user, product=product, quantity=quantity)
    return redirect('cart')

@login_required
def remove_cart(request,pk):
    item=Cart.objects.get(id=pk)
    item.delete()
    return redirect('cart')
@login_required
def update_cart(request,pk):
    item=Cart.objects.get(id=pk)
    item.quantity = request.POST['quantity']
    item.save()
    print(item.quantity)
    return redirect('cart')

def checkout(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        zipcode = request.POST['zipcode']
        phonenumber = request.POST['phonenumber']
        costumers.objects.create(
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            country=country,
            zipcode=zipcode,
            phonenumber=phonenumber
        )
        return redirect('checkout.html')
    return render(request, 'checkout.html',)