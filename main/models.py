import datetime
from django.db import models
import random
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50, verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name='Почта')
    referral_code = models.CharField(max_length=7, default=random.randint(1000000, 9999999),
                                     verbose_name='Ваш реферальный код')
    expiration_date = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(days=5)),
                                           verbose_name='Код действителен до')
    owner = models.CharField(max_length=7, verbose_name='Реферальный код, другового пользователя', **NULLABLE)
    referrals = models.ManyToManyField('self', verbose_name='Мои рефералы', blank=True)

    def __str__(self):
        return self.username


@receiver(post_save, sender=User)
def delete_expired_referral_code(sender, instance, **kwargs):
    """
    Автоматически стирает реферальный код по истичению времени
    """
    if instance.expiration_date.timestamp() <= datetime.datetime.now().timestamp():
        instance.referral_code = ''
        instance.save()
