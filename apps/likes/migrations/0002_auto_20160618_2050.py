# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='likes',
            field=models.BooleanField(default=False),
        ),
    ]
