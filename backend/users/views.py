from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


class RegisterUser(SuccessMessageMixin, CreateView):
    """
    регистрация
    """

    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("main_page_view")
    success_message = "Вы успешно зарегистрировались! "

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg'] = 'reg'
        return context


# class LoginUser(SuccessMessageMixin, LoginView):
#     """
#     авторизация
#     """
#     form_class = LoginUserForm
#     # template_name = 'users/login.html'
#     template_name = 'base.html'
#     extra_context = {'title': 'Авторизация'}
#     success_message = "Вы успешно авторизованы! "

#     def get_success_url(self):
#         # перенапровление
#         return reverse_lazy('main_page_view')


def login_user(request):
    """view for login user, it takes data from templatetag
    check user by it email or login, if user exists takes his username
    and request password authenticate and login
    """

    if request.method == "POST":
        log = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(Q(username=log) | Q(email=login)).first()
        if user:
            user = authenticate(username=user.username, password=password)

            if user:
                login(request, user)
                messages.success(request, "Вы успешно авторизованы")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
