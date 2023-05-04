from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('users/edit/', views.profile_edit_view, name='profile-edit'),
    path('create-post/', views.post_create_view, name='post-create'),
    path('users/<str:custom_url>/', views.profile_view, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
