from django.urls import path
from .views import homepage,Brandpages,Categorypage
urlpatterns = [ 
    path('',homepage,name='home'),
    path('brand/<slug:nm>',Brandpages,name='brand'),
    path('category/<slug:nm>',Categorypage,name='category')
    ]