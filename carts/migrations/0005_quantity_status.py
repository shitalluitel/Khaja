# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-05 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20180527_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='status',
            field=models.CharField(default='New', max_length=32),
        ),
    ]
