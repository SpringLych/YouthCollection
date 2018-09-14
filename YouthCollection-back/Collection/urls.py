from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^article/(?P<category>\w+)$',views.article),
    url(r'^adminaeiou/$',views.admin),
    url(r'^add_article/$', views.add_article),
    url(r'^get_head_article/$',views.get_head_article),
    url(r'^add_head_article/$',views.add_head_article),
    # url(r'^ajaxtest$', views.ajaxtest),
]