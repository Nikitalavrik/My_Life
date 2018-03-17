# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='song',
            name='play_list',
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(blank=True, null=True, to='music.Song'),
        ),
    ]
