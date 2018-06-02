from django.contrib import admin
from read_num.models import *

# Register your models here.
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')

admin.site.register(ReadNum, ReadNumAdmin)
