# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-15 05:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20170626_1522'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Supplier',
            new_name='Relation',
        ),
    ]
