# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-22 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20170622_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='number',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='material',
            name='mat_type',
            field=models.CharField(choices=[('TIM', 'Time'), ('FAB', 'Fabric'), ('ACC', 'Accesories'), ('FIL', 'Filling'), ('SMA', 'Small Materials')], max_length=3, verbose_name='Material type'),
        ),
        migrations.AlterField(
            model_name='material',
            name='unit_purchase',
            field=models.CharField(choices=[('MO', 'Months'), ('PC', 'Pieces'), ('PL', 'Pieces'), ('ME', 'Meters'), ('RO', 'Rolls')], max_length=2, verbose_name='Purchase unit'),
        ),
        migrations.AlterField(
            model_name='material',
            name='unit_usage',
            field=models.CharField(choices=[('HU', 'Hours'), ('PI', 'Pieces'), ('ME', 'Meters')], max_length=2, verbose_name='Usage unit'),
        ),
        migrations.AlterField(
            model_name='material',
            name='unit_usage_in_purchase',
            field=models.FloatField(verbose_name='Number of usage units in purchase unit'),
        ),
    ]