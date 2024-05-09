from django.urls import path
from . import views


urlpatterns = [
    path('', views.AllPostsView.as_view(), name="main_page_view"),

]