from django.contrib import admin
from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post")
    list_display_links = ("id", "user", "post")
    search_fields = ("post",)

