# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('full_name', models.CharField(max_length=1024)),
                ('status', models.CharField(choices=[('Primary', 'Primary'), ('Sub', 'Sub'), ('Ineligible', 'Ineligible')], default='Primary', max_length=1024)),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(max_length=1024, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ManyToManyField(to='rosters.Team'),
        ),
    ]
