from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


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
        fields = ['username', 'email', 'first_name', 'last_name',  'password1', 'password2']
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
    авторизация
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
