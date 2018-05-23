from django.shortcuts import render
from django.views.generic.base import View
from .models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


# 处理课程机构列表的view
class OrgView(View):
    def get(self, request):
        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()

        # 取出所有的城市
        all_citys = CityDict.objects.all()

        # 总共有多少家机构使用count进行统计
        # org_nums = all_orgs.count()
        return render(request, "org-list.html",{
            "all_orgs":all_orgs,
            "all_citys": all_citys,
        })