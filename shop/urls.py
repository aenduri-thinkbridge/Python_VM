from django.urls import path
from .views import homepage,Brandpages,Categorypage,product_view,order_view
from .views import cart_view,add_cart,remove_cart,update_cart,checkout,order_confirm
urlpatterns = [ 
    path('',homepage,name='home'),
    path('brand/<slug:nm>',Brandpages,name='brand'),
    path('category/<slug:nm>',Categorypage,name='category'),
    path('product/<str:nm>',product_view,name='product'),
    path('cart/',cart_view,name='cart'),
    path('cart/<str:nm>',add_cart,name='add_cart'),
    path('remove_cart/<int:pk>',remove_cart,name='remove'),
    path('update_cart/<int:pk>',update_cart,name='update'),
    path('checkout',checkout,name='checkout'),
    path('order_confirm',order_confirm,name='order_confirm'),
    path('orders',order_view,name='orders'),


    ]