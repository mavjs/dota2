# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0004_auto_20160619_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rosters.Team'),
        ),
        migrations.AlterField(
            model_name='player',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
