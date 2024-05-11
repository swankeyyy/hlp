from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *



class RegisterUser(SuccessMessageMixin, CreateView):
    """
    регистрация
    """
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy('main_page_view')
    success_message = "Вы успешно зарегистрировались! "


class LoginUser(SuccessMessageMixin, LoginView):
    """
    авторизация
    """
    form_class = LoginUserForm
    # template_name = 'users/login.html'
    template_name = 'base.html'
    extra_context = {'title': 'Авторизация'}
    success_message = "Вы успешно авторизованы! "

    def get_success_url(self):
        # перенапровление
        return reverse_lazy('main_page_view')



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main_page_view'))