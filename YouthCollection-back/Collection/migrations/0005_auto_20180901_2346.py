# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-01 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collection', '0004_auto_20180901_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='introduction',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
