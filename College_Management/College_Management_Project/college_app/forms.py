from secrets import choice
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Notice

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description', 'priority']
