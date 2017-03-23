# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-23 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=0, verbose_name='Is read'),
        ),
    ]
