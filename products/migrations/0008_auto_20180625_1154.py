# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-25 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20180624_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=20),
        ),
    ]