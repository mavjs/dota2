# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0003_auto_20160619_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='player',
            order_with_respect_to=None,
        ),
    ]
