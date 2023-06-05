from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('register', views.register, name='register'),
     path('contact', views.contact, name='contact'),
]
