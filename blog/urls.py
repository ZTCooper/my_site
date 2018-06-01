from django.conf.urls import url
# 配置上传文件的访问处理函数
from .views import *

urlpatterns = [
    url(r'^$', main_page, name='main_page'),
    url(r'^(?P<blogpost_id>\d+)$', blog_page, name='blog_page'),
    #url(r'^edit/(?P<blogpost_id>\d+)$', edit_page, name='edit_page'),
    #url(r'^edit/post$', post_blog, name='post_blog'),
    url(r'^aboutme$', about_me, name='about_me'),
    url(r'^date/(?P<year>\d+)/(?P<month>\d+)$', blog_monthly, name='blog_monthly'),
    url(r'^list$', blog_list, name='blog_list'),
    url(r'^search$', blog_search, name='blog_search'),
]
