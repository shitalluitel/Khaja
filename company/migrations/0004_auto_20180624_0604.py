# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-24 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180527_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=150),
        ),
    ]
