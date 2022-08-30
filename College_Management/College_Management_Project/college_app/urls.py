from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    # path('about/', views.about, name='about'),
    # path('services/', views.services, name='services'),
    # path('contact/', views.contact, name='contact'),
]