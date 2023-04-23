from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserLoginForm(forms.AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())

class UserRegistrationForm(forms.UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', )

class ProfileEditForm(forms.Form):
    user = get_user_model()

    username = forms.CharField(initial = user.username)
    custom_url = forms.CharField(initial = user.get_slug)
    bio = forms.Textarea(initial = user.bio)