from django.urls import path
from . import views


urlpatterns = [
    path('', views.AllPostsView.as_view(), name="main_page_view"),
    path('/<slug:slug>', views.PostDetailView.as_view(), name="post_detail_view")
]