from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class GetContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ContactUs
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'inputBox'}),
            'name': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
            # 'phone': forms.TextInput(attrs={'class': 'inputBox'}),
            'phone': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
            # 'email': forms.TextInput(attrs={'class': 'inputBox'}),
            'email': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
            'message': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email',)
