# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-09 09:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2018, 3, 9, 9, 29, 42, 9698, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]