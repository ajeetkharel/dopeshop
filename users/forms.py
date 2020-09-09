from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Owner, Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']