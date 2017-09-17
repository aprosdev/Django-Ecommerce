# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-17 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0079_auto_20170917_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umbrellaproductmodelimage',
            name='image',
            field=models.ImageField(upload_to='media/umbrella_product_model/images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='umbrellaproductmodelproductiondescription',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/umbrella_product_models/production_description/images/%Y/%m/%d'),
        ),
    ]