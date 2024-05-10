from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from .views import *
from django.urls import reverse, reverse_lazy


app_name = "users"

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),  # регистрация
]
