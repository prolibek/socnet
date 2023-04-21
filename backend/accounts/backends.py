from django.contrib.auth.backends import BaseBackend

class ProfileBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        return super().authenticate(request, **kwargs)