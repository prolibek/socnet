from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Post, Comment

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', )

class ProfileEditForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'bio', 'custom_url', )

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('text', )

class CommentCreateForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ('text', )