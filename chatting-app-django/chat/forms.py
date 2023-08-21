from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


from django.forms import TextInput

from django.db import models
from .models import MyUser
from django.forms import ModelForm, TextInput, Textarea, FileField


class UserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['name', 'password']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'maxLength': '20'
            }),

            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            })
        }


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields=['username','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
        }