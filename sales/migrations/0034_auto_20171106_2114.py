# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-06 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0033_auto_20171106_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorderproduct',
            name='input_sku',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='salesorderproduct',
            name='price_list_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.PriceListItem'),
        ),
    ]
