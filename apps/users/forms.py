#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 14:08
# @Author  : shenyoujian
# @description :

# 引入django表单
from django import forms


# 登录表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)







