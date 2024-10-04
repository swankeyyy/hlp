from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

from users.models import User, SuggestArticle


class RegisterUserForm(UserCreationForm):
    """
    регистрация пользователя

    уникальность паролей проверяет  UserCreationForm
    """
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'image': 'Аватар',

        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_email(self):
        """проверка на уникальность email"""
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже существует")
        return email


class LoginUserForm(AuthenticationForm):
    """
    authorization
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'login',
                                      'placeholder': 'Введите ваш username или email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password',
                                          'placeholder': 'Введите ваш пароль'}))

    class Meta:
        """
        get_user_model стандартная модель пользователя
        """
        model = get_user_model()
        fields = ['username', 'password']


class ProfileUserForm(forms.ModelForm):
    """
    Профиль пользователя
    disabled=True // нельзя редактировать
    """
    username = forms.CharField(disabled=True, label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(disabled=True, label="E-mail",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))



    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'image', ]
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'image': 'Аватар',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SuggestArticleForm(forms.ModelForm):
    """
    suggest article in user settings
    """

    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'comment_content',
                                     'placeholder': ' Предложить статью', 'style': "min-height: 100px"}))
    class Meta:
        model = SuggestArticle
        fields = ['content', ]
