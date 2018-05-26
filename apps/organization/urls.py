#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 12:48
# @Author  : shenyoujian
# @description :
from organization.views import OrgView, OrgDescView, OrgTeacherView, AddFavView, \
    AddUserAskView, OrgCourseView, OrgHomeView
from django.urls import path, re_path

app_name = "organization"

urlpatterns = [
    # 课程机构列表url
    path('list/', OrgView.as_view(), name="org_list"),
    # 添加我要学习
    path("add_ask/", AddUserAskView.as_view(), name="add_ask"),
    # home页面，取纯数字
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name="org_home"),
    # 访问课程
    re_path('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name="org_course"),
    # 访问机构描述
    re_path('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name="org_desc"),
    # 访问机构讲师
    re_path('teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name="org_teacher"),
    # 机构收藏
    path('add_fav/', AddFavView.as_view(), name="add_fav"),
]