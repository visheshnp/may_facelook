# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 08:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_remove_cards_card_hero_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cards',
            options={'verbose_name': 'Card', 'verbose_name_plural': 'Cards'},
        ),
    ]