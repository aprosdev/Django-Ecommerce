# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-26 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0060_productmodel_size_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umbrellaproductmodel',
            name='all_patterns_present',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='all_patterns_present',
            field=models.BooleanField(default=False),
        ),
    ]
