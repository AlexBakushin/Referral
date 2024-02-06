from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50, verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name='Почта')
