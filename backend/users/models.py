from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to="users/images/", blank=True, null=True, verbose_name="Фото профиля")
    phone = models.IntegerField(verbose_name="Номер телефона", null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
