from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import *
from blog.forms import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_read_num' , 'short_content', 'create_time', 'update_time')
    list_per_page = 10
    list_filter = ('create_time',)

    def short_content(self, obj):
        return obj.content[:50]

    short_content.short_description = u'博客内容'
    Article.get_read_num.short_description = u'阅读量'

@admin.register(BlahBlah)
class BlahBlahAdmin(admin.ModelAdmin):
    list_display = ('short_content', 'get_read_num', 'create_time', 'update_time')
    list_per_page = 10
    list_filter = ('create_time',)

    def short_content(self, obj):
        return obj.content[:50]

    short_content.short_description = u'内容'
    BlahBlah.get_read_num.short_description = u'阅读量'

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # 显示用户字段
    list_display = ('username', 'nick_name', 'email',
                    'gender', 'mobile', 'address')
    # 过滤器设置
    list_filter = ('username', 'nick_name', 'email')
    # 搜索
    search_fields = ('username', 'nick_name', 'email')

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_detail', 'site_user')

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url', 'image_data')
    readonly_fields = ('image_url', 'image_data')   # 自定义字段属性

    def image_url(self, obj):
        # 取消html转义
        return mark_safe('<a href="%s">右键复制图片地址</a>' % obj.path.url)
    def image_data(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.path.url)
    image_data.short_description = u'图片'
    image_url.short_description = u'图片地址'
