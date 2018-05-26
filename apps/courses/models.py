from django.db import models
from datetime import datetime
from organization.models import CourseOrg
from organization.models import Teacher
# Create your models here.


# 课程信息表
class Course(models.Model):
    DEGREE_CHOICES = (
        ("cj", u"初级"),
        ("zj", u"中级"),
        ("gj", u"高级"),
    )
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    # TextField允许我们不输入长度。可以输入到无限大。暂时定义为TextFiled，之后更新为富文本
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(max_length=2, choices=DEGREE_CHOICES, verbose_name=u"课程等级")
    # 使用分钟做后台记录(存储最小单位)前台转换
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    # 保存学习的人数：点击开始学习才算
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(
        upload_to="courses/%Y/%m",
        max_length=100,
        verbose_name=u"课程封面图"
    )
    # 保存点击量，点击页面就算
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time  = models.DateTimeField(default=datetime.now, verbose_name=u"课程添加的时间")
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name=u"所属机构", null=True, blank=True)
    category = models.CharField(max_length=20, default=u"", verbose_name=u"课程类别")
    tag = models.CharField(max_length=15, verbose_name=u"课程标签", default=u"")
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师", on_delete=models.CASCADE, null=True, blank=True)
    you_need_know = models.CharField(max_length=300, default=u"一颗勤学的心是本课程必要前提", verbose_name=u"课前须知")
    teacher_tell = models.CharField(max_length=300, default=u"按时交作业，不然叫家长", verbose_name=u"老师告诉你")

    # 获取课程章节数的方法
    def get_zj_nums(self):
        return self.lesson_set.all().count()

    # 获取学习这门课程的用户
    def get_learn_users(self):
        # 谁的里面添加了它做外键，他都可以取出来
        return self.usercourse_set.all()[:5]

    # 教师数自定义函数
    def get_teacher_nums(self):
        return self.teacher_set.all().count

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name


# 章节
class Lesson(models.Model):
    # 因为一个课程对应很多章节。所以在章节表中将课程设置为外键。
    # 作为一个字段来让我们可以知道这个章节对应那个课程
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"章节添加的时间")

    def __str__(self):
        return '《{0}》课程的章节 >> {1}'.format(self.course, self.name)

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


# 每章视频
class Video(models.Model):
    # 因为一个章节对应很多视频。所以在视频表中将章节设置为外键。
    # 作为一个字段来存储让我们可以知道这个视频对应哪个章节.
    lesson = models.ForeignKey(Lesson,  on_delete=models.CASCADE, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"该视频添加的时间")
    url = models.CharField(max_length=200, default="http://blog.mtianyan.cn/", verbose_name=u"访问地址")
    # 使用分钟做后台记录(存储最小单位)前台转换
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


# 课程资源
class CourseResource(models.Model):
    # 因为一个课程对应很多资源。所以在课程资源表中将课程设置为外键。
    # 作为一个字段来让我们可以知道这个资源对应那个课程
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name=u"资源文件",
        max_length=100,
    )
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"该资源添加的时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name












