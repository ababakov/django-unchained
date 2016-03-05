# coding: utf-8

from django.conf.urls import url
from django.views.decorators.http import require_POST  # require_GET

from blog.views import PostDetailView, PostsListView, CommentFormView

app_name = 'blog'
urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='post-list'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/comment/$', require_POST(CommentFormView.as_view()),
        name='post-add-comment')
]
