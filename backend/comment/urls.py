from django.urls import path
from . import views


urlpatterns = [
    path('comment/create_comment', views.create_comment, name="create_comment"),

]