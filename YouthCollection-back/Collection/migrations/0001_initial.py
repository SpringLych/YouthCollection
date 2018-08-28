# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-16 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('address', models.URLField()),
                ('pic_path', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
