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
    path('student-view-notice/', views.student_view_notice, name='student-view-notice'),
    path('student-view-basic-notice/', views.student_view_basic_notice, name='student-view-basic-notice'),
    path('student-view-important-notice/', views.student_view_important_notice, name='student-view-important-notice'),
    path('student-view-urgent-notice/', views.student_view_urgent_notice, name='student-view-urgent-notice'),
    # path('about/', views.about, name='about'),
    # path('services/', views.services, name='services'),
    # 
]