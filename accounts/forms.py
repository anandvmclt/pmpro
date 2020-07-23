# Accounts/Forms.py
from .models import AbstractUser, User
from django.contrib.auth.models import AbstractUser
from django import forms
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password','mobile', 'city', 'userbio', 'website', 'picture')

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password', 'mobile', 'city', 'userbio', 'website', 'picture')
