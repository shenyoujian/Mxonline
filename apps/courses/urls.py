#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 0:21
# @Author  : shenyoujian
# @description :
from courses.views import CourseListView, CourseDetailView
from django.urls import path, re_path
app_name = "courses"
urlpatterns = [
    # 课程列表url
    path('list/', CourseListView.as_view(), name="list"),
    # 课程详情页
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
]