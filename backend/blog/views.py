from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import Post
from common.views import CommonTitleMixin

# asdsad
class AllPostsView(CommonTitleMixin, ListView):
    title = "Главная"
    model = Post
    template_name = 'blog/all_posts.html'
    context_object_name = 'posts'
    
    
