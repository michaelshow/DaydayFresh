
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.user.views import RegisterView
from apps.user import views
# app.urls中设置app_name变量，否则反向解析会报错
app_name = 'user'
urlpatterns = [
    # url(r'^register$', register, name='register'), # 注册
    url(r'^register', RegisterView.as_view(), name='register')
]
