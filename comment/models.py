from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model as user_model

User = user_model()

# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    comment_content = models.TextField(verbose_name=u'评论内容')
    comment_time = models.DateTimeField(verbose_name=u'评论时间', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=u"用户", on_delete=models.DO_NOTHING)
