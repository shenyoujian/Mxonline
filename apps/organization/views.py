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

        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        # 总共有多少家机构使用count进行统计
        org_nums = all_orgs.count()
        return render(request, "org-list.html",{
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
        })