from django.shortcuts import render
from django.views.generic.base import View
from .models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


# 处理课程机构列表的view
class OrgView(View):
    def get(self, request):
        return render(request, "org-list.html")