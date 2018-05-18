from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
        # 自定义的性别选择规则
        GENDER_CHOICES = (
            ("male", u"男"),
            ("female", u"女")
        )

        # 昵称
        nick_name = models.CharField(max_length=50, default='', verbose_name=u"昵称")
        # 生日，可以为空
        birthday = models.DateField(null=True, blank=True, verbose_name=u"生日")
        # 性别 只能男或女，默认女
        gender = models.CharField(
            max_length=5,
            choices=GENDER_CHOICES,
            default="female",
            verbose_name=u"性别"
        )
        # 地址
        address = models.CharField(max_length=100, default='', verbose_name=u"地址")
        # 电话
        mobile = models.CharField(max_length=11, null=True, blank=True)
        # 头像 默认使用default.png
        image = models.ImageField(
            upload_to="image/%Y/%m",
            default=u"image/default.png",
            max_length=100
        )

        # meta信息，即后台栏目名
        class Meta:
            verbose_name = "用户信息"
            verbose_name_plural = verbose_name

        # 重载__str__方法，打印实例会打印username，username为继承自abstractuser
        def __str__(self):
            return self.username
