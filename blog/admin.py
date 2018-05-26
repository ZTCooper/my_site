from django.contrib import admin
from blog.models import UserProfile, Category, Article, SiteInfo


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


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SiteInfo, SiteInfoAdmin)
