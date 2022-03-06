from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from .utils import generate_gravatar_url


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email')

        gravatar_url = generate_gravatar_url(self.normalize_email(email))
        user = self.model(
            email=self.normalize_email(email=email),
            gravatar_url=gravatar_url,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not password:
            raise ValueError('Admins must have a password')

        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        db_index=True,
    )
    gravatar_url = models.URLField(
        verbose_name='gravatar url',
        max_length=128,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    def token(self):
        return RefreshToken.for_user(self)

    def has_perm(self, perm, obj=None):
        '''
        Does currently logged in user has
        permission to access resource.
        Right now every logged in user has
        access to resources. we can add
        strict permission model later
        '''
        return True

    def has_module_perms(self, app_label):
        '''
        Does currently logged in user has
        permission to access resource.
        Right now every logged in user has
        access to resources. we can add
        strict permission model later
        '''
        return True

    @property
    def is_staff(self):
        '''
        Every admin of the platform is a staff
        '''
        return self.is_admin
