from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class ProfileManager(BaseUserManager):

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.username = username
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, username, password, **extra_fields)
    
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class Profile(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key = True)
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=16, unique=True) # my_name_is_bryan
    bio = models.TextField(blank = True)
    avatar = models.ImageField(upload_to="images/avatars", blank=True)
    rating = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    custom_url = models.CharField(max_length=16, blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username or self.email.split('@')[0]
    
    def get_absolute_url(self):
        if self.custom_url:
            return f"users/{self.custom_url}/"
        else:
            return f"users/{self.id}/"
    
    def get_slug(self):
        if self.custom_url:
            return self.custom_url
        else:
            return self.id
    
    def get_username(self):
        return self.username