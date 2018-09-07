# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-07 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0008_auto_20180907_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, default='Biratnagar', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, default='Nepal', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, choices=[('01', 'Province No. 1'), ('02', 'Province No. 2'), ('03', 'Province No. 3'), ('04', 'Gandaki Pradesh'), ('05', 'Province No. 5'), ('06', 'Karnali Pradesh'), ('07', 'Province No. 6')], default='01', max_length=120, null=True),
        ),
    ]
