# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-22 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_products', '0006_designs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='manage_products.Designs'),
        ),
    ]
