# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-26 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20180825_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Prepared', 'Prepared'), ('Shipped', 'Shipped'), ('Paid', 'Paid')], default='Processing', max_length=120),
        ),
    ]