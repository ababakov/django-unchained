#coding: utf-8

from django.conf.urls import url

from blog.views import PostDetailView, PostsListView

app_name = 'blog'
urlpatterns = [
  url(r'^$', PostsListView.as_view(), name='post-list'),
  url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail')
]