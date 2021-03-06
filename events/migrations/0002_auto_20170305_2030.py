# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-05 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='id',
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='datafile',
            field=models.ImageField(blank=True, null=True, upload_to=events.models.upload_to, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='datafile',
            field=models.ImageField(blank=True, null=True, upload_to=events.models.upload_to, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
