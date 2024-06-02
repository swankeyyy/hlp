from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Comment
from blog.models import Post


def create_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)

        comment_instance = Comment(content=content, user=user, post=post)
        comment_instance.save()
        print(1)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
