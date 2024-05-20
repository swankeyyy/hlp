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

"""
context['reg'] = 'reg' // We overturn the reg wherever you need to remove the site bar (main.html)
{% if not reg %}
    {% include 'UI/include/sidebar.html' %}
{% endif %}

"""


class RegisterUser(SuccessMessageMixin, CreateView):
    """
    Registration
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


class ProfileUser(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Profile user
    """
    model = User
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    success_message = "Профиль изменен "

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg'] = 'reg'
        context['title'] = 'Профиль пользователя'
        return context

    def get_success_url(self):
        """
        redirect to profile
        """
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        """
        in the profile takes the logged in user
        """
        return self.request.user


def logout_user(request):
    """
    if you logged out of your account and were on the user’s page,
    it redirects to the main page
    """
    logout(request)
    try:
        return HttpResponseRedirect(reverse('main_page_view'))
    except:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
