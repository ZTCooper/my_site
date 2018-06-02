from django.conf.urls import url
# 配置上传文件的访问处理函数
from .views import *

urlpatterns = [
    url(r'^$', main_page, name='main_page'),
    url(r'^blog/(?P<blogpost_id>\d+)$', blog_page, name='blog_page'),
    url(r'^aboutme$', about_me, name='about_me'),
    url(r'^date/(?P<year>\d+)/(?P<month>\d+)$', blog_monthly, name='blog_monthly'),
    url(r'^list$', blog_list, name='blog_list'),
    url(r'^blog/search$', blog_search, name='blog_search'),

    url(r'^blah$', blah_list, name='blah_list'),
    url(r'^blah/(?P<blah_id>\d+)$', blah_detail, name='blah_detail'),
    url(r'^blah/search$', blah_search, name='blah_search'),
]
