from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('users/<str:custom_url>/', views.profile_view, name='profile'),
]
