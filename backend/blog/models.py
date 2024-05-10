from django.conf import settings
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Ip(models.Model):

    """table with ip adresses"""

    ip = models.CharField(max_length=100)


def __str__(self):
    return self.ip


class Language(models.Model):
    """language model for LP`s like python, JS"""

    name = models.CharField(max_length=50, verbose_name="Название языка")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        upload_to="media/lang_images", blank=True, null=True, verbose_name="Значок ЯП"
    )
    url = models.SlugField(unique=True, max_length=50, verbose_name="URL")
    icon = models.CharField(
        max_length=100, verbose_name="Font awesome icon", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "ЯП"
        verbose_name_plural = "ЯПы"


class Tag(models.Model):
    """Tags for simple post like hashtags"""

    name = models.CharField(max_length=50, verbose_name="Имя тега")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    url = models.SlugField(unique=True, max_length=50, verbose_name="URL")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(MPTTModel):
    """Category by TreeForeignKey like Framework/Django and etc"""

    name = models.CharField(
        max_length=50, unique=True, verbose_name="Название категории"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        default="Информация скоро обновится",
    )
    url = models.SlugField(unique=True, max_length=50, verbose_name="URL")
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    icon = models.CharField(
        max_length=100, verbose_name="Font Awesome Icon", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"

    class MPTTMeta:
        level_attr = "mptt_level"
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    """Single Post model, with null author if author is admin, with category and tags"""

    name = models.CharField(max_length=150, verbose_name="Название поста")
    preview_image = models.ImageField(
        upload_to="media/previews",
        verbose_name="Изображение к посту для ленты",
        null=True,
        blank=True,
    )
    url = models.SlugField(unique=True, max_length=50, verbose_name="URL")
    description = models.TextField(verbose_name="Контент")
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name="post",
        verbose_name="Категория",
    )
    language = models.ForeignKey(
        to=Language,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="post",
        verbose_name="ЯП",
    )
    tag = models.ManyToManyField(to=Tag, verbose_name="Теги", blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Автор поста, если пост предложен пользователем",
    )
    is_published = models.BooleanField(default=True)
    time_created = models.DateField(auto_now_add=True)
    views = models.ManyToManyField(to=Ip, related_name="post_views", blank=True, verbose_name="Просмотры")
    
    def total_views(self):
        return self.views.count()

    def __str__(self):
        return f"{self.name} - {self.category}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class PostImage(models.Model):
    """images for post(if it needs)"""

    name = models.CharField(max_length=50, verbose_name="Название изображения")
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        verbose_name="Изображение к посту",
        related_name="image",
    )
    image = models.ImageField(upload_to="media/post_images", verbose_name="Изображение")
