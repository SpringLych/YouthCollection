# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    category=models.CharField(max_length=20)
    address=models.URLField()
    img_name=models.CharField(max_length=150)
    timestamp=models.DateTimeField()


class Category(models.Model):
    name=models.CharField(max_length=20)
    identify=models.CharField(max_length=50)
    weight=models.IntegerField()
