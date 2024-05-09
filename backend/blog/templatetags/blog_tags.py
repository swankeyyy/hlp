from django import template
from blog.models import Category


register = template.Library()


@register.inclusion_tag("UI/tags/header/header_menu.html", takes_context=True)
def get_header_menu(context):
    """all categories for top menu"""
    content = Category.objects.filter(mptt_level=0)
    return {"menu": content}

