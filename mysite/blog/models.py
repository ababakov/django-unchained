# coding: utf-8
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Дата публикации')
    content = RichTextField()
    author = models.ForeignKey(AUTH_USER_MODEL)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(u'Дата создания',
                                   auto_now_add=True, blank=True)
    content = models.TextField(max_length=1000)
    email = models.CharField(max_length=255, default=None, null=True)
    name = models.CharField(max_length=255, default=None, null=True)
    author = models.ForeignKey(AUTH_USER_MODEL, default=None, null=True)
    parent = models.ForeignKey('self', default=None, null=True)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.title
