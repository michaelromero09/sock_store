# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-09 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admins',
            name='first_name',
            field=models.TextField(default='Pepper', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admins',
            name='last_name',
            field=models.TextField(default='Cat', max_length=255),
            preserve_default=False,
        ),
    ]
