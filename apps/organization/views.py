from django.shortcuts import render
from django.views.generic.base import View
from .models import CourseOrg, CityDict
from pure_pagination import Paginator, PageNotAnInteger
from django.http import HttpResponse
from .forms import UserAskForm
# Create your views here.


# 处理课程机构列表的view
class OrgView(View):
    def get(self, request):
        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()

        # 热门机构，如果不加负号会是由小到大
        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        # 取出所有的城市
        all_citys = CityDict.objects.all()

        # 取出筛选的城市，默认值为空
        city_id = request.GET.get("city", "")
        # 如果选择了某个城市，也就是前端传过来了值
        if city_id:
            # 外键city在数据中叫city_id
            # 我们就在机构中作进一步筛选
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
            # 我们就在机构中作进一步筛选
            all_orgs = all_orgs.filter(category=category)

        # 进行排序
        sort = request.GET.get('sort',"")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-student")
            elif sort == "course":
                all_orgs = all_orgs.order_by("-course_nums")

        # 总共有多少家机构使用count进行统计
        org_nums = all_orgs.count()

        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_orgs, 4, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html",{
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_orgs": hot_orgs,
        })


# 用户添加我要学习
class AddUserAskView(View):
    # 处理表单提交当然post
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        # 判断该form是否有效
        if userask_form.is_valid():
            # 这里是modelform的区别
            # 它有model的属性
            # 当commit为True进行真正保存
            user_ask = userask_form.save(commit=True)
            # 这样就不需要把一个一个字段取出来然后存到model的对象之后save

            # 如果保存成功，返回json字符串，后面content type是告诉浏览器的
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            # 如果保存失败，返回json字符串，并将form的报错信息通过msg传递到前端
            return HttpResponse('{"status":"fail", "msg": "您的字段有错误，请检查"}', content_type='application/json')
            # return HttpResponse('{"status":"fail", "msg":"您的字段有错误,请检查"}', content_type='application/json')
