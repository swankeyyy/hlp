from typing import Any
from django.db.models import F
from django.db.models.query import QuerySet
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Post, Category
from common.views import CommonTitleMixin
from comment.forms import NewCommentForm


class AllPostsView(CommonTitleMixin, ListView):
    title = "Главная"
    model = Post
    template_name = "blog/all_posts.html"
    context_object_name = "posts"
    error_search_message = None
    paginate_by = 3

    def _get_content_by_search(self, instance, search):
        """takes search value and instance and check:
        if value in post name it returns list of posts
        elif value == tag.name it returns all posts by tag name
        elif result is null it returns empty queryset and error_message
        """

        if search:
            queryset_by_tag = instance.filter(tag__name=search)
            if queryset_by_tag:
                return queryset_by_tag
            queryset_by_icontains = instance.filter(name__iregex=search)
            if queryset_by_icontains:
                return queryset_by_icontains
            instance = []
            self.error_search_message = f"по запросу '{search}' результатов не найдено!..."

        return instance

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset().filter(is_published=True)
        search = self.request.GET.get("q")
        content = self._get_content_by_search(queryset, search)
        return content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error_search_message'] = self.error_search_message
        return context


class PostDetailView(CommonTitleMixin, DetailView):
    """Detail View of Single Post, with method for add comment to current post"""

    model = Post
    slug_field = "url"
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['title'] = self.get_object().name
        context['comments'] = self.get_object().comment.order_by('-id')
        context['comment_form'] = NewCommentForm
        return context


class CategoryView(CommonTitleMixin, ListView):
    """List of posts by chosen category
        find posts by them category slug
    """
    template_name = "blog/all_posts.html"
    context_object_name = "posts"
    paginate_by = 10
    allow_empty = True
    error_search_message = None

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Post.objects.filter(category__url=self.kwargs['slug']).select_related("category")
        if queryset:
            self.title = queryset[0].category.name
        else:
            self.error_search_message = f"Категория пуста"
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error_search_message'] = self.error_search_message
        return context