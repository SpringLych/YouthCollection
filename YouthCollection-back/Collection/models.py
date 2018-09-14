# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    category=models.CharField(max_length=20)
    address=models.URLField()
    img_name=models.TextField(max_length=1000)
    timestamp=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=100)
    introduction=models.CharField(max_length=200)

 
class Category(models.Model):
    name=models.CharField(max_length=20)
    identify=models.CharField(max_length=50)
    weight=models.IntegerField()

class HeadArticle(models.Model):
    # 要跳转的链接
    url = models.URLField()
    img = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    addtime=models.DateTimeField(auto_now=True)