# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-11 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0019_relationaddress_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='_xero_contact_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
