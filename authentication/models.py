from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    


class User(AbstractBaseUser,PermissionsMixin):
        email = models.EmailField(max_length = 255,unique = True)
        is_verified = models.BooleanField(default = True)
        is_staff = models.BooleanField(default = False)
        name = models.TextField()
        created_at = models.DateTimeField(auto_now_add = True)

        objects = CustomUserManager()

        USERNAME_FIELD = 'email'
        EMAIL_FIELD = 'email'
        
        def tokens(self):
             token = RefreshToken.for_user(self) 
             return {
                  'refresh':str(token),
                  'access' : str(token.access_token)
             }

