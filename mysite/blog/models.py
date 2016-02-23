# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
  title = models.CharField(max_length=255)
  datetime = models.DateTimeField(u'Дата публикации')
  content = RichTextField()

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return "/post/%i/" % self.id