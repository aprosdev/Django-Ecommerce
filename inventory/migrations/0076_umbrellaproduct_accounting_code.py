# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-11 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0075_stocklocation_own_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='umbrellaproduct',
            name='accounting_code',
            field=models.CharField(choices=[('212', "Suzy's range"), ('211', "Suzy's custom range")], default='200', max_length=20),
        ),
    ]