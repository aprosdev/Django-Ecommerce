# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-13 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0011_merge_20171013_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionorderdelivery',
            name='cost_of_transport',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='productionorderdelivery',
            name='number_of_pallets',
            field=models.IntegerField(default=0),
        ),
    ]