# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-16 09:39
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VEDA_OS01', '0005_auto_20171127_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='edx_id',
            field=models.TextField(verbose_name=b'VEDA Video ID'),
        ),
    ]
