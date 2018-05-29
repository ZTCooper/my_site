from django.db import models
# 扩展User表
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here

# 用户表
class UserProfile(AbstractUser):
    nick_name = models.CharField(
        max_length=24, verbose_name='用户昵称', default="")
    gender = models.CharField(max_length=10, choices=(
        ('1', '男'), ('0', '女')), default='1', verbose_name='用户性别')
    birthday = models.DateField(verbose_name='用户生日', null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True,
                              blank=True, verbose_name='电话号码')
    address = models.CharField(max_length=200, verbose_name='用户地址', default='')
    detail = models.CharField(max_length=200, verbose_name='个人简介', default='')
    email = models.EmailField()
    REQUIRED_FIELDS = ['email']

    class Meta(AbstractUser.Meta):
        verbose_name = u'用户表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

    """继承django系统自带的user创建用户表，
	    1.配置文件中要添加 AUTH_USER_MODEL = "blog.UserProfile"
	    2.引入from django.contrib.auth.models import AbstractUser
	    3.admin.py 中注册用户表 admin.site.register(UserProfile)
	    4. 如果之前先生成了数据库表，之后修改的user要重新生成表，最好先清空数据库。
	"""


# 文章分类
class Category(models.Model):
    title = models.CharField(
        max_length=20,
        verbose_name='分类名称',
        null=True,
        default='')
    detail = models.CharField(
        max_length=100,
        verbose_name='分类介绍',
        null=True,
        default='')
    icon = models.CharField(
        max_length=100,
        verbose_name='分类图标',
        null=True,
        default='')
    sort_id = models.IntegerField(verbose_name='分类排序', null=True, default=99)

    class Meta:
        verbose_name = u'博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 文章详情
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题', default='')
    content = models.TextField(verbose_name='文章正文', default='')
    category = models.ForeignKey(Category, verbose_name='所属分类', default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='文章作者', null=True, blank=True)
    create_time = models.DateTimeField(
        verbose_name='文章创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'文章更新时间', auto_now=True)

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SiteInfo(models.Model):
    site_name = models.CharField(max_length=20, verbose_name='站点名称')
    site_detail = models.CharField(
        max_length=100, verbose_name='站点介绍', default='')
    site_user = models.ForeignKey(
        UserProfile, verbose_name='管理员', null=True, blank=True)
    site_footer = models.TextField(verbose_name='站点底部代码', default='')

    class Meta:
        verbose_name = u"站点信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.site_name

class BlogImage(models.Model):
    title = models.CharField(max_length=20, verbose_name='图片标题', default='')
    path = models.ImageField(verbose_name='图片', upload_to='upload/%Y/%m', default='upload/default.jpg', max_length=100)

    class Meta:
        verbose_name = '网站相册'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
