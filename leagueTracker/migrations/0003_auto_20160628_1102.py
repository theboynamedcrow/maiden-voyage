# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-28 15:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagueTracker', '0002_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfer',
            name='display_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='golfer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
