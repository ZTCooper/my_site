from django.conf.urls import url
# 配置上传文件的访问处理函数
from django.views.static import serve
from django.conf import settings
from .views import *

urlpatterns = [
    url(r'^$', main_page, name='main_page'),
    url(r'^(?P<blogpost_id>\d+)$', blog_page, name='blog_page'),
    url(r'^edit/(?P<blogpost_id>\d+)$', edit_page, name='edit_page'),
    url(r'^edit/post$', post_blog, name='post_blog'),
    url(r'^tags$', blog_tags, name='blog_tags'),
    url(r'^media/(?P<path>.*)', serve, {"document_root":settings.MEDIA_ROOT}, name='media')
]
