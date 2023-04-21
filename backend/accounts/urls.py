from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register')
]
