
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# app_name = 'goods'
from apps.goods import views
# 为什么没有导入时找不到？user中没有导入可以找到视图

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
