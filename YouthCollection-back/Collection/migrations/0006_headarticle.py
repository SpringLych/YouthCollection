# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-13 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collection', '0005_auto_20180901_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('img', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('addtime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
