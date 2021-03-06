# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0005_auto_20160619_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='country',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='mmr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='tag',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
