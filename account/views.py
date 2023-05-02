from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from shop.views import homepage
# Create your views here.
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


def logout_view(request):
    logout(request)
    return redirect(login)
