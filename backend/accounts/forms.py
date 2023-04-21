from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', )