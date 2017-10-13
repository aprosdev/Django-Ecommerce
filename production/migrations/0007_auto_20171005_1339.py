# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-05 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0102_product__created_in_sprintpack'),
        ('production', '0006_auto_20170918_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionOrderDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier', models.CharField(max_length=3)),
                ('est_delivery_date', models.DateField()),
                ('production_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.ProductionOrder')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionOrderDeliveryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product')),
                ('production_order_delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.ProductionOrderDelivery')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='productionorderdeliveryitem',
            unique_together=set([('product', 'production_order_delivery')]),
        ),
    ]
