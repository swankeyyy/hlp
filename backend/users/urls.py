from django.urls import path
from .views import *


# app_name = "users"

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),  # регистрация
    path('login/', login_user, name='login'),  # authorization
    path('logout/', logout_user, name='logout'),  # выход
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('favorites/<int:id>/', UserFavoritesView.as_view(), name='favorites'),
    path('add_to_favorite/<int:id>', add_to_favorite, name="add_to_favorite"),
    path('remove_from_favorite/<int:id>', remove_from_favorite, name="remove_from_favorite"),
    path('suggest_article/', UserArticle.as_view(), name="suggest_article"),
]


