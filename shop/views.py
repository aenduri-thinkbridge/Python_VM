
from django.contrib.auth.decorators import login_required
# to remove %20 in the product name
import time
from django.views.decorators.cache import never_cache

from .models import costumers
from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand, Category, Product, Cart


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
    return render(request, 'homepage.html', context)


def Brandpages(request, nm):
    brand = Brand.objects.get(name=nm)
    products = Product.objects.filter(brand=brand)
    context = {'products': products}
    context.update(navbar_items(request))
    return render(request, 'brand.html', context)


def Categorypage(request, nm):
    category = Category.objects.get(name=nm)
    products = Product.objects.filter(Category=category)
    context = {'products': products}
    context.update(navbar_items(request))
    return render(request, 'category.html', context)


def product_view(request, nm):
    product = get_object_or_404(Product, name=nm)
    print(product.id)
    context = {'product': product}
    context.update(navbar_items(request))
    return render(request, 'product.html', context)


@login_required(login_url='login')
def cart_view(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = sum([c.product.price * c.quantity for c in cart])
    total_items = sum([c.quantity for c in cart])
    context = {'cart': cart, 'total_price': total_price,
               'total_items': total_items}
    context.update(navbar_items(request))
    return render(request, 'cart.html', context)


@login_required
def add_cart(request, nm):
    product = Product.objects.get(name=nm)
    cart = Cart.objects.filter(user=request.user)
    value = 1
    if request.method == 'POST':
        value = int(request.POST.get('quantity'))
        print("value:", value)
    products = [item.product for item in cart]
    if product not in products:
        quantity = product.quantity + value
        Cart.objects.create(user=request.user,
                            product=product, quantity=quantity)
    else:
        cart = Cart.objects.get(user=request.user, product=product)
        print(type(cart.quantity), type(value))
        cart.quantity += value
        cart.save()
    return redirect('cart')


@login_required
def remove_cart(request, pk):
    item = Cart.objects.get(id=pk)
    item.delete()
    return redirect('cart')


@login_required
def update_cart(request, pk):
    item = Cart.objects.get(id=pk)
    item.quantity = request.POST['quantity']
    item.save()
    print(item.quantity)
    return redirect('cart')

def redeem_check(code):
    redeem_codes = {
        'SHOP50': [0.5, f"50% off"],
        'SHOP30': [3000, "3000 off"],
        'SHOP25': [0.25, f"25% off"],
        'SHOP20': [2000, "2000 off"],
        'SHOP15': [0.15, f"15% off"],
        'SHOP10': [1000, "1000 off"],
    }
    redeem = [i for i in redeem_codes if i == code]
    discount=redeem_codes[redeem[0]]
    return discount
@never_cache
@login_required(login_url='login')
def checkout(request):
    submitted = False

    # Retrieve cart items for the current user
    cart = Cart.objects.filter(user=request.user)

    # Compute total number of items and total price in cart
    total_items = sum([cart_item.quantity for cart_item in cart])
    total_price = sum([cart_item.product.price * cart_item.quantity for cart_item in cart])

    # Define initial context with cart information
    context = {'submitted': submitted, 'cart': cart, 'total_items': total_items, 'total_price': total_price}
    #create a session so that data can be retrieved from
    session = request.session
    session.set_expiry(30)
    if request.method == 'POST':
        if 'redeem' in request.POST:
            code = request.POST['code']
            discount = redeem_check(code)

            # Apply discount if valid code is entered
            if type(discount[0]) == int:
                total_price -= discount[0]
            elif type(discount[0]) == float:
                total_price *= discount[0]

            context.update({'discount': discount[1], 'code': code, 'total_price': total_price})
            
            #session objects
            session_data = {'discount': discount[1], 'code': code, 'total_price': total_price}
            session['checkout_data'] = session_data
            session.save()
            print('session redeem:',dict(session))
            
        elif 'customer_form' in request.POST:
            # process customer form data
            session['customer_data'] = {
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'address': request.POST['address'],
                'city': request.POST['city'],
                'country': request.POST['country'],
                'zipcode': request.POST['zipcode'],
                'phonenumber': request.POST['phonenumber']
            }
            session.save()
            #return redirect('checkout')
            # redirect to checkout page to prevent resubmission on page reload
    session_data = session.get('checkout_data', {})
    customer_data = session.get('customer_data')
    if customer_data:
        # create and save a Customer object
        customer = costumers.objects.create(
            user=request.user,
            first_name=customer_data['first_name'],
            last_name=customer_data['last_name'],
            address=customer_data['address'],
            city=customer_data['city'],
            country=customer_data['country'],
            zipcode=customer_data['zipcode'],
            phonenumber=customer_data['phonenumber']
        )
        
        # Update context with submitted form information
        customer.save()
        submitted = True
        context.update({'costumer': customer, 'submitted': submitted})

    # Update context with navbar items and render checkout page
    context.update(session_data)
    context.update(navbar_items(request))
    context['session_expiry'] = session.get_expiry_age()
    
    return render(request, 'checkout.html', context)

