#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 12:48
# @Author  : shenyoujian
# @description :
from organization.views import OrgView
from django.urls import path, re_path
from .views import AddUserAskView


app_name = "organization"
urlpatterns = [
    # 课程机构列表url
    path('list/', OrgView.as_view(), name="org_list"),
    # 添加我要学习
    path("add_ask/", AddUserAskView.as_view(), name="add_ask")
]