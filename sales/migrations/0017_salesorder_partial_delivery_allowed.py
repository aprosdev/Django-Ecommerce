# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-12 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0016_merge_20171011_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='partial_delivery_allowed',
            field=models.BooleanField(default=False),
        ),
    ]