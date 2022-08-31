from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('admin-home/', views.adminPage, name='admin-home'),
    path('teacher-home/', views.teacherPage, name='teacher-home'),
    path('student-home/', views.studentPage, name='student-home'),
    path('course/', views.course, name='course'),
    path('contact/', views.contact, name='contact'),
    path('post-notice/', views.postNotice, name='post-notice'),
    # path('about/', views.about, name='about'),
    # path('services/', views.services, name='services'),
    # 
]