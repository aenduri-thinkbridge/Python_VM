from django.urls import path
from .views import login,signup,logout_view
urlpatterns = [ 

    path('register/',signup,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout_view,name='logout'),
]