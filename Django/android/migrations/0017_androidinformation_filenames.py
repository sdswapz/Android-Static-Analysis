# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-30 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0016_auto_20171130_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidinformation',
            name='filenames',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
