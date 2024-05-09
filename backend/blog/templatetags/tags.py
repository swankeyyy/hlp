from django import template
from blog.models import Category


register = template.Library()


@register.inclusion_tag("UI/tags/header/header_menu.html")
def get_menu():
    """all categories for top menu"""
    content = Category.objects.all()
    return {"menu": content}

