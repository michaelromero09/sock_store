# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-09 04:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_auto_20170709_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='admins',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admins',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
