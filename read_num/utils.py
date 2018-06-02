from django.contrib.contenttypes.models import ContentType
from read_num.models import ReadNum

# 阅读量增加
def read_increase(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_visited" % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            #存在记录（取出）
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            #不存在（创建）
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()
    return key
