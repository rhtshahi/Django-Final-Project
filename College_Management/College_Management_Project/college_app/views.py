from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

#from College_Management_Project.college_app.decorators import unauthenticated_user
from .forms import CreateUserForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user

# Create your views here.

def homePage(request):
    # return HttpResponse('About')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def loginPage(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            #username = request.user.username latest: request.user.is_authenticated
            return redirect('student-home')

        else:
            messages.info(request, 'Incorrect Username/Password!!!')
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user_name )
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)
        # form = CreateUserForm()

        # if request.method == 'POST':
        #     form = CreateUserForm(request.POST)
        #     if form.is_valid():
        #         form.save()
        #         user_name = form.cleaned_data.get('username')
        #         messages.success(request, 'Account was created for ' + user_name )
        #         return redirect('login')

        # context = {'form':form}
        # return render(request, 'register.html', context)

@login_required(login_url='login')
def adminPage(request):
    return render(request, 'adminHome.html')


@login_required(login_url='login')
def teacherPage(request):
    return render(request, 'teacherHome.html')


@login_required(login_url='login')
def studentPage(request):
    return render(request, 'studentHome.html')