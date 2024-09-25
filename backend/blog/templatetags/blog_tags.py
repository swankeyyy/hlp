from django import template
from blog.models import Category, Post

register = template.Library()


@register.inclusion_tag("UI/tags/header/header_menu.html", takes_context=True)
def get_header_menu(context):
    """all categories for top menu"""
    content = Category.objects.filter(mptt_level=0)
    return {"menu": content}


@register.inclusion_tag("UI/tags/main/sidebar_posts.html")
def get_sidebar_posts(num=3):
    """7 most popular posts for sidebar"""
    posts = Post.objects.filter(is_published=True).order_by('-views')[:num]
    return {"posts": posts}
