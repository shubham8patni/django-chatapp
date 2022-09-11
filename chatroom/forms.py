from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # required = True/False -> default = True
    first_name = forms.CharField(max_length=30, min_length=3, label='first name')
    last_name = forms.CharField(max_length=30, min_length=3, label='last name')
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField() # required = True/False -> default = True
    first_name = forms.CharField(max_length=30, min_length=3, label='first name')
    last_name = forms.CharField(max_length=30, min_length=3, label='last name')
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
