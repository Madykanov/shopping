from django.urls import path
from .views import *

urlpatterns = [
    path('login/',loginPage,name='login'),
    path('to_log/',to_log,name='to_log'),
    path('logout',logoutUser,name='logout'),
    

    path('', home, name='home'),
    path('info/<int:pk>', info, name='info'),


    path('addcart/<str:pk>/', addToCart, name='addcart'),
    path('updateCart/<str:pk>/', updateCart, name='updateCart'),
    path('mycart/', mycart, name='mycart'),
    
    
    path('order/', order, name='order'),
    path('myOrder/', myOrder, name='myOrder'),

    path('favorite/<str:pk>/', favorite, name='favorite'),
    path('myfavorite/', myfavorite, name='myfavorite'),
    path('removeFav/<str:pk>/', removeFav, name='remove'),



]