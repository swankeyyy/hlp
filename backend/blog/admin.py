from django.contrib import admin
from .models import Category, Language, Tag, Post
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name", "url")
    search_fields = ("name",)
    prepopulated_fields = {"url": ("name",)}


admin.site.register(Category, CategoryAdmin)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name", "url")
    search_fields = ("name",)
    prepopulated_fields = {"url": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name", "url")
    search_fields = ("name",)
    prepopulated_fields = {"url": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name", "url")
    search_fields = ("name",)
    prepopulated_fields = {"url": ("name",)}