# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-27 03:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180526_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='comapany',
            new_name='company',
        ),
    ]