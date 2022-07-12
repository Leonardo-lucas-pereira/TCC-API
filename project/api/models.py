from django.db import models

from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'is_active', 'is_superuser']



