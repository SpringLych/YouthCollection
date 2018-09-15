# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Article, Category, HeadArticle
from datetime import datetime
# from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
from PIL import Image
import os
import urllib
# Create your views here.
save_dir = '../static/images/'

def index(request):
    category = Category.objects.all().order_by('weight')
    return render(request, 'index.html', {'category': category})


def article(request, category):
    # title 美人志etc
    title = Category.objects.get(identify=category).name
    articles = Article.objects.filter(category=title).values(
        'address', 'img_name', 'timestamp', 'title', 'introduction').order_by('-timestamp')
    # articles = serializers.serialize("json", articles)

    articles = list(articles)
    # return render(request,'article.html',{'title':title,'articles':articles})
    # 格式化得到的数据

    format_arc = []
    for item in articles:
        fort = {
            "src": '',
            "title": '',
            "desc": '',
            "url": ''
        }
        fort["src"] = save_dir+item["img_name"]
        fort["title"] = item["title"]
        fort["desc"] = item["introduction"]
        fort["url"] = item["address"]
        format_arc.append(fort)

    res = {"title": title, "articles": format_arc}
    return JsonResponse(res, safe=False)


def admin(request):
    category = Category.objects.all().order_by('weight')
    return render(request, 'admin.html', {'category': category})


def add_article(request):
    if request.method == "POST":
        try:
            # img = request.FILES.get('image')
            # baseDir = os.path.dirname(os.path.abspath(__file__))
            # baseDir = os.path.dirname(baseDir)
            # imgdir = os.path.join(baseDir, 'static', 'images')
            # num = Article.objects.count() + 1
            # filename = "youth" + str(num) + img.name
            # filepath = os.path.join(imgdir, filename)
            # while(os.path.exists(filepath)):
            #     num = num + 1
            #     filename = "youth" + str(num) + img.name
            #     filepath = os.path.join(imgdir, filename)
            # fileobj = open(filepath, 'wb')
            # for chrunk in img.chunks():
            #     fileobj.write(chrunk)
            # fileobj.close()
            category = request.POST.get('category')
            address = request.POST.get('address')
            title = request.POST.get('title')
            introduction = request.POST.get('introduction')
            # img_name = filename
            img_url = request.POST.get('image')
            img_name = save_img(img_url, category, 1)
            article = Article(category=category, address=address, img_name=img_name,
                              title=title, introduction=introduction)
            article.save()
            return render(request, 'success.html')
        except:
            return render(request, 'error.html', {'info': '系统异常,添加失败'})
    else:
        return render(request, 'error.html', {'info': '系统异常,添加失败'})


def get_head_article(request):
    head_art = HeadArticle.objects.filter().values(
        'url', 'img', 'title').order_by('-addtime')
    head_art = list(head_art)
    for item in head_art:
        item['img'] = save_dir + item['img']
    # 只获取最新的三个
    return_art = head_art[0:3]
    return JsonResponse(return_art, safe=False)


def add_head_article(request):
    if request.method == "POST":
        try:
            # 跳转至地址
            head_address = request.POST.get('headAddress')
            head_title = request.POST.get('headTitle')
            # 添加的图片链接
            head_img_url = request.POST.get('headImage')
            head_img_name = save_img(head_img_url, 'head', 2)
            head_img_name = head_img_name
            head_article = HeadArticle(url=head_address,img=head_img_name,title=head_title)
            head_article.save()
            return render(request, 'success.html')
        except:
            return render(request, 'error.html', {'info': '系统异常,添加失败'})
    else:
        return render(request, 'error.html', {'info': '系统异常,添加失败'})


def save_img(img_url, catg, index):
    try:
        baseDir = os.path.dirname(os.path.abspath(__file__))
        baseDir = os.path.dirname(baseDir)
        imgdir = os.path.join(baseDir, 'static', 'images/')
        timesnap = datetime.now().strftime('%Y%m%d%H%M%S')
        file_suffix = '.jpg'
        img_name = '{}{}{}'.format(catg,timesnap, file_suffix)
        img_path = '{}{}'.format(imgdir, img_name)
        num =  1
        while(os.path.exists(img_path)):
            num = num + 1
            timesnap = timesnap + str(num)
            img_name = '{}{}{}'.format(catg,timesnap, file_suffix)
            img_path = '{}{}'.format(imgdir, img_name)
        urllib.urlretrieve(img_url, filename=img_path)
        # 压缩图片
        im = Image.open(img_path)
        w,h = im.size
        if index==1:
            size=(100,100)
        else:
            size = (w/2,h/2)
        im.thumbnail(size)
        im.save(img_path,'jpeg')
    except IOError as e:
        print e
    except Exception as ee:
        print ee
    return img_name