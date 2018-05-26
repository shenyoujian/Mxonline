"""Mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import django
from django.contrib import admin
from django.urls import path, include, re_path
# 导入x admin，替换admin
from django.views.static import serve

import users
import xadmin
from django.views.generic import TemplateView
# from users.views import user_login
from Mxonline.settings import MEDIA_ROOT
from organization.views import OrgView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    # TemplateView.as_view会将template转换为view
    path('', TemplateView.as_view(template_name="index.html"), name= "index"),

    # 基于类方法实现登录，这里是调用它的方法
    path('login/', LoginView.as_view(), name="login"),

    # 注册url
    path('register/', RegisterView.as_view(), name="register"),

    # 验证码url
    path('captcha/', include('captcha.urls')),

    # 激活用户url
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name="user_active"),

    # 忘记密码
    path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),

    # 重置密码url:用来接受来自邮箱的重置链接
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),

    # 修改密码url：用于passwordreset页面提交表单
    path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构app的url配置,使用命名空间防止重复
    path("org/", include('organization.urls', namespace='org')),

    # 课程机构首页url
    # path('org_list/', OrgView.as_view(), name="org_list"),
    # 处理图片显示的url，使用django自带serve，传入参数告诉它会去哪个路径找，我们有配置路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),

    # 课程app的url配置
    path("course/", include("courses.urls", namespace="course"))
]
