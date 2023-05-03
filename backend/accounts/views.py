from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UserLoginForm, UserRegistrationForm, ProfileEditForm


def profile_view(request, custom_url=None):
    try:
        profile = Profile.objects.get(custom_url = custom_url)
    except:
        profile = Profile.objects.get(id = int(custom_url))

    return render(request, 'accounts/profile.html', { 'profile': profile })

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(f"/")
    else:
        form = ProfileEditForm()

    return render(request, 'accounts/profile-edit.html', {'form': form })

def home_view(request):
    return render(request, 'accounts/home.html')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(
                username=username, 
                password=password
            )
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=user.password)
            if user is not None:
                login(request, user)
            else:
                print("User is not authenticated")
        return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', { 'form': form })
