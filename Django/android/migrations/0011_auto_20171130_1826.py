# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-30 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0010_auto_20171128_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='androiddocumentsmagic',
            old_name='app_hash',
            new_name='apphash',
        ),
    ]
