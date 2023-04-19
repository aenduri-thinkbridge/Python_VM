from django.urls import path
from .views import homepage,Brandpages,Categorypage,login,signup,product_view
urlpatterns = [ 
    path('',homepage,name='home'),
    path('brand/<slug:nm>',Brandpages,name='brand'),
    path('category/<slug:nm>',Categorypage,name='category'),
    path('register/',signup,name='register'),
    path('login/',login,name='login'),
    path('logout/',login,name='logout'),
    path('product/<str:nm>',product_view,name='product'),
    ]