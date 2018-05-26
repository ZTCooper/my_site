from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', main_page, name='main_page'),
    url(r'^(?P<blogpost_id>\d+)$', blog_page, name='blog_page'),
    url(r'^edit/(?P<blogpost_id>\d+)$', edit_page, name='edit_page'),
    url(r'^edit/post$', post_blog, name='post_blog'),
]
