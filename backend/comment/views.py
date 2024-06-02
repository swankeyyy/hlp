from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Comment
from blog.models import Post


def create_comment(request):
    """controller for new comment, it takes post_id by hidden label in template, user from current user
        works without permissions only by condition on template
    """
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)

        comment_instance = Comment(content=content, user=user, post=post)
        comment_instance.save()
        print(1)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


def delete_comment(request, *args, **kwargs):
    """takes comment id from template, if current user is comment author it delete comment by id"""

    if request.method == 'GET':
        comment_id = kwargs['id']
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.user == request.user:
            comment.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
