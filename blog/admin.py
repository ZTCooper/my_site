from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time')
    list_filter = ('create_time',)


class UserProfileAdmin(admin.ModelAdmin):
    # 显示用户字段
    list_display = ('username', 'nick_name', 'email',
                    'gender', 'mobile', 'address')
    # 过滤器设置
    list_filter = ('username', 'nick_name', 'email')
    # 搜索
    search_fields = ('username', 'nick_name', 'email')


class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_detail', 'site_user')

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



# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SiteInfo, SiteInfoAdmin)
admin.site.register(BlogImage, BlogImageAdmin)
