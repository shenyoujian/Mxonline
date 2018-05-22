from django.shortcuts import render
# django自带auth框架的函数
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View
from .models import UserProfile, EmailVerifyRecord
# 并集运算
from django.db.models import Q
# 导入自定义验证表单
from .forms import LoginForm, RegisterForm, ActiveForm
# 发送邮件
from utils.email_send import send_register_email
# Create your views here.


# 登录功能的view
class LoginView(View):
    # 直接调用get方法免去判断
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        # 类实例化需要一个字典参数dict:request.POST就是一个QueryDict所以直接传入
        # POST中的usernamepassword会对应到form中
        login_form = LoginForm(request.POST)
        # is_valid判断我们字段是否有错执行我们原有逻辑，验证失败就跳回login页面
        if login_form.is_valid():
            # 取不到时为空，username， password为前端页面name值
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            user = authenticate(username = user_name, password = pass_word)

            if user is not None:
                login(request, user)
                return render(request, "index.html")
            # 仅当用户真的密码出错时
            else:
                return render(request, "login.html", {"msg":"用户名或密码错误!"})
        # 验证不成功跳回登录页面
        # 没有成功说明里面的值是None,并再次跳转回主页面
        else:
            return render(request, "login.html", {"login_form": login_form})


# 注册功能的view
class RegisterView(View):
    # get方法直接返回页面
    def get(self, request):
        # 添加验证码
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form':register_form})

    def post(self, request):
        # 实例化form
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")

            # 实例化一个user_profile对象，将前台值存入
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name          # 因为只能使用邮箱注册

            # 加密password进行保存
            user_profile.password = make_password(pass_word)
            # 修改默认的激活状态为fasle
            user_profile.is_active = False
            send_register_email(user_name, "register")
            user_profile.save()

        return render(request, "index.html")


# 当我们配置url被这个view处理时，自动传入request对象
def user_login(request):
    # 前端向后端发送的请求方式：get或post

    # 登录提交表单为post
    if request.method == 'POST':
        # 取不到时为空，username，password为前端页面name值
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        # 成功返回user对象，失败返回null
        user = authenticate(username=user_name, password=pass_word)

        # 如果不是null说明验证成功
        if user is not None:
            # login_in 两参数：request, user
            # 实际是对request写了一部分东西进去，然后再render的时候，
            # request是要render回去的。这些信息也就随着返回浏览器。完成登录。
            login(request, user)
            # 跳转到首页，user request会被带回到首页
            return render(request, "index.html")
        # 没有成功说明里面的值是None， 并再次跳转回主页面
        else:
            return render(request, "login.html", {"msg":"用户名或密码错误！ "})

    # 获取登录页面为get
    elif request.method == 'GET':
        # render就是渲染html返回用户
        # render三变量：request，模板名称，一个字典写明传入给前端的值
        return render(request, "login.html")


# 实现用户名邮箱均可登录
# 继承ModelBackend类，因为它有方法authenticate，可点击源码查看
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因，Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))

            # django的后台中密码加密：所以不能password=password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password)

            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 激活用户的view
class ActiveUserView(View):
    def get(self, request, active_code):
        # 查询邮箱验证码记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        # 激活form负责给激活跳转进来的人加验证
        active_form = ActiveForm(request.GET)
        # 如果不为空也就是有用户
        if all_record:
            for record in all_record:
                # 获取到对应的邮箱
                email = record.email
                # 查找到邮箱对应的user
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                # 激活成功跳转到登录页面
                return render(request, "login.html")
            # 验证码输错
            else:
                return render(request, "register.html", {"msg":"您的激活链接无效","active_form": active_form})









