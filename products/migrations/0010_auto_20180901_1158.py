# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-01 11:58
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180901_1050'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
