# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-26 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('products', '0003_auto_20180219_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='comapany',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='company.Company'),
            preserve_default=False,
        ),
    ]