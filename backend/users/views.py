from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import User, Favorite
from django.contrib.auth import authenticate, login
from django.contrib import messages
from common.views import CommonTitleMixin
from blog.models import Post

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
    success_message = "Вы успешно зарегистрировались! Для входа в систему ,авторизуйтесь."

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


class UserFavoritesView(View):
    title = "Избранное"

    def get(self, request, *args, **kwargs):
        user = self.request.user
        posts = Favorite.objects.filter(user=user)[0].post.all()
        return render(request, "blog/all_posts.html", {'posts': posts, 'title': self.title})


def add_to_favorite(request, *args, **kwargs):
    """Add post to users bookmarks(favorite posts), take user from request, takes post from post_id"""
    if request.method == "GET":
        user = request.user
        post_id = kwargs["id"]
        favorite = Favorite.objects.filter(user=user)
        if not favorite:
            favorite = Favorite.objects.create(user=user)
        else:
            favorite = favorite[0]
        favorite.post.add(Post.objects.get(id=post_id))
        print(user.favorite)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


class UserArticle(SuccessMessageMixin, CreateView):
    """
    Подключаем комментарии к посту
    """
    form_class = SuggestArticleForm  # форма
    template_name = 'users/suggest_article.html'
    success_message = "Форма отправлена"

    def form_valid(self, form):
        """
        связываем коммент к посту, формируем запись без занесения в бд,
        определяем пользователя , после сохраняем в бд
        """
        # form.instance.com_id = self.kwargs.get("pk")
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Предложить новость'
        context['description'] = ('Здесь вы можете предложить статью для размещения на сайте '
                                  'или высказать свои пожелания, '
                                  'какие материалы хотели бы увидеть у нас.')
        context['reg'] = 'reg'
        return context

    def get_success_url(self):
        """
        redirect to profile
        """
        return reverse_lazy('suggest_article')
