# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='pictures',
            field=models.ManyToManyField(to='media.Picture'),
        ),
    ]
