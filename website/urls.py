from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('home', views.Home, name='home' ),
    path('logout', views.Logout, name='logout' ),
    path('register', views.Register, name='register' ),
]