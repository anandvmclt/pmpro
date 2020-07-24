# Accounts/Forms.py
from django.contrib.auth.forms import PasswordChangeForm

from .models import AbstractUser, User
from django import forms
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password', 'mobile', 'city', 'userbio', 'website', 'picture')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Select Username', 'type': 'text'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email ID', 'type': 'email'}),
            'password': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Choose a Password', 'type': 'password'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your city'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website URL'}),
            'userbio': forms.Textarea(attrs={'class': 'form-control mytxt', 'placeholder': 'Persional Details'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile', 'city', 'userbio', 'website', 'job', 'skills', 'picture')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Username', 'type': 'text'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'type': 'text'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email ID', 'type': 'email'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your city'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website URL'}),
            'userbio': forms.Textarea(attrs={'class': 'form-control mytxt', 'placeholder': 'Persional Details'}),
            # 'picture': forms.FileField(attrs={'class': 'form-control-file'})
        }


class UpdatePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        widgets = {
            'old_password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Password', 'type': 'password'}),
            'new_password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a new Password', 'type': 'password'}),
            'new_password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Re-type Password', 'type': 'password'}),

        }
