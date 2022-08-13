from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home,name='home'),
    path('userlogout/',views.userlogout),

]
