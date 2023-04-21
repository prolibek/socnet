from rest_framework import generic, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import ProfileLoginSerializer
from django.contrib.auth import authenticate

class ProfileLoginAPIView(generic.GenericAPIViews):
    pass