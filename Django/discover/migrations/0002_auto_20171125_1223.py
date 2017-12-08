# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-25 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploaddocuments',
            name='docfile',
        ),
        migrations.AddField(
            model_name='uploaddocuments',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
    ]
