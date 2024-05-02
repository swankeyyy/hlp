from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from blog.models import Post


class User(AbstractUser):
    """Give extension for basic user model, now user can add his image and phone if he wants"""

    image = models.ImageField(upload_to="users/images/", blank=True, null=True, verbose_name="Фото профиля")
    phone = models.IntegerField(verbose_name="Номер телефона", null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Favorite(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorite")
    post = models.ManyToManyField(to=Post, verbose_name="Избранные посты")

    class Meta:
        verbose_name = "Любимый пост"
        verbose_name_plural = "Любимые посты"
