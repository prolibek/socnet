from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserLoginForm, UserRegistrationForm

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
