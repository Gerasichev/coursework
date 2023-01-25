from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='E-mail', max_length=255, unique=True)
    nickname = models.CharField(verbose_name='Имя пользователя', max_length=255)
    is_subscribed = models.BooleanField(verbose_name='Подписка', default=False)

    is_active = models.BooleanField(verbose_name='Активирован', default=False)
    is_staff = models.BooleanField(verbose_name='Персонал', default=False)
    is_superuser = models.BooleanField(verbose_name='Суперпользователь', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'