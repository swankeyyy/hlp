from django import template
from users.forms import LoginUserForm


register = template.Library()


@register.inclusion_tag("UI/tags/header/modal_login.html")
def get_login_modal():
    login_form = LoginUserForm()
    return {"login_form": login_form}

    