# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-06 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0032_pricelistautosend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelistautosend',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Agent'),
        ),
        migrations.AlterField(
            model_name='pricelistautosend',
            name='relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Relation'),
        ),
    ]