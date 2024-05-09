from pyexpat import model
from django.db import models
from blog.models import Post
from django.conf import settings


class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment", null=True,
                             blank=True)
    content = models.TextField(max_length=500)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comment", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.post}'

    class Meta:
        verbose_name = "Коммментарий"
        verbose_name_plural = "Комментарии"


        

