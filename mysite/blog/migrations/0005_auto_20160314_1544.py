# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 15:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160314_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='datetime',
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
    ]
