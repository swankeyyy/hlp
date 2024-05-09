from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import Post


class AllPostsView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    context_object_name = 'posts'
