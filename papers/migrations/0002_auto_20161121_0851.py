# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-21 00:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='relation',
            new_name='relate_paper',
        ),
    ]
