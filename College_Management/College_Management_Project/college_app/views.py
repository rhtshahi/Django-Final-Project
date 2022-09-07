from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

#from College_Management_Project.college_app.decorators import unauthenticated_user
from .forms import CreateUserForm, PostNoticeForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .decorators import allowed_users, unauthenticated_user, page_redirect

from .forms import PostNoticeForm
from .models import Notice

# Create your views here.
# @page_redirect
def homePage(request):
    # return HttpResponse('About')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def course(request):
    return render(request, 'course.html')

def contact(request):
    return render(request, 'contact.html')

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            #username = request.user.username latest: request.user.is_authenticated
            return redirect('admin-home')
            # return redirect('home')

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
            user = form.save()
            user_name = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)

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
# @allowed_users(allowed_roles=['admin'])
@page_redirect
def adminPage(request):
    return render(request, 'adminHome.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def teacherPage(request):
    return render(request, 'teacherHome.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def studentPage(request):
    return render(request, 'studentHome.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def postNotice(request):

    form = PostNoticeForm()

    if request.method =='POST':
        form =PostNoticeForm(request.POST)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.posted_by = request.user
            instance.save()
            return redirect('teacher-home')

    context = {'form' : form}

    return render(request, 'postNotice.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student_view_notice(request):
    all_notice =  Notice.objects.all()
    context = {'all_notice': all_notice}

    return render(request, 'studentViewNotice.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student_view_basic_notice(request):
    basic_notice = Notice.objects.filter(priority='Basic').values()
    context = {'basic_notice' : basic_notice}

    return render(request, 'studentBasicNotice.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student_view_important_notice(request):
    important_notice = Notice.objects.filter(priority='Important')
    context = {'important_notice' : important_notice}

    return render(request, 'studentImportantNotice.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student_view_urgent_notice(request):
    urgent_notice = Notice.objects.filter(priority='Urgent').values()
    context = {'urgent_notice' : urgent_notice}

    return render(request, 'studentUrgentNotice.html', context)
