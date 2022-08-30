from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def homePage(request):
    # return HttpResponse('About')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register.html')