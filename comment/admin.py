from django.contrib import admin
from .models import *

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'comment_content', 'comment_time', 'user')

admin.site.register(Comment, CommentAdmin)
