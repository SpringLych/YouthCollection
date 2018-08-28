from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^article/(?P<category>\w+)$',views.article),
    url(r'^admin/$',views.admin),
    url(r'^add_article/$', views.add_article),

    # url(r'^ajaxtest$', views.ajaxtest),
]