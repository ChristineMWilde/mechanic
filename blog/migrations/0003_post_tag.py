# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180831_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]