# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 05:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('product_photo', models.ImageField(upload_to='dishes/')),
                ('description', models.TextField(max_length=512)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product',
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
