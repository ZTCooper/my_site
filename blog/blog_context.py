from django.conf import settings as original_settings #必须引入
from blog.models import UserProfile, Category, SiteInfo, Article, BlahBlah # 导入一些必须的model

def blog_info(request):
    #站长及博客上下文数据管理
    siteinfo = SiteInfo.objects.get(pk=1)   # blog相关资料
    categories = Category.objects.all().order_by('sort_id')   # 根据排序获取所有分类
    #把获取的数据通过字典返回
    arts = Article.objects.all().order_by('-create_time')
    dates = Article.objects.dates('create_time', 'month', order='DESC')
    blahblahs = BlahBlah.objects.all().order_by('-create_time')
    return {'siteinfo':siteinfo, 'categories':categories, 'arts':arts[:5], 'dates': dates, 'blahblahs': blahblahs[:5]}

# 标签信息
def blog_tag_info(request):
    values = Article.objects.values('tag')
    blog_tags = []
    for value in values:
        blog_tags.extend(value['tag'].split(' '))
    blog_tags = set(blog_tags)
    blog_tags.discard('')
    return {'blog_tags': blog_tags}

def blah_tag_info(request):
    values = BlahBlah.objects.values('tag')
    blah_tags = []
    for value in values:
        blah_tags.extend(value['tag'].split(' '))
    blah_tags = set(blah_tags)
    blah_tags.discard('')
    return {'blah_tags': blah_tags}
