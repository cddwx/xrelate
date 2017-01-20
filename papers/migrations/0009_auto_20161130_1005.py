# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-30 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0008_auto_20161129_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='bib_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/bib/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='paper',
            name='bib_type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paper_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/paper/%Y/%m/%d/'),
        ),
    ]
