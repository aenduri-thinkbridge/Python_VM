from django.urls import path
from .views import homepage,Brandpages,Categorypage,login,signup,product_view,logout_view,cart_view,add_cart
urlpatterns = [ 
    path('',homepage,name='home'),
    path('brand/<slug:nm>',Brandpages,name='brand'),
    path('category/<slug:nm>',Categorypage,name='category'),
    path('register/',signup,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout_view,name='logout'),
    path('product/<str:nm>',product_view,name='product'),
    path('cart/',cart_view,name='cart'),
    path('cart/<str:nm>',add_cart,name='add_cart'),
    ]