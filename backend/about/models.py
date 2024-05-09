from django.db import models


class SocialItem(models.Model):
    """social links on footer"""

    name = models.CharField(max_length=50, unique=True, verbose_name="Название соцсети")
    icon = models.CharField(max_length=100, verbose_name="Font Awesome Icon")
    link = models.TextField(verbose_name="Адрес ссылки")
