from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model as user_model    #自带用户系统

User = user_model()     #这个要注意

# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    comment_content = models.TextField(verbose_name=u'评论内容')
    comment_time = models.DateTimeField(verbose_name=u'评论时间', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=u"用户", on_delete=models.DO_NOTHING)
                                                        #删除对象（评论）不影响User

