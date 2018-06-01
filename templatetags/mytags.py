import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from blog.models import Article

# 引入过滤器
register = template.Library()

# 自定义过滤器
@register.filter(is_safe=True)
@stringfilter
# 显示markdown
def toMarkdown(value):
    # markdown解析器
    return mark_safe(markdown2.markdown(force_text(value), extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler"]))

@register.filter
# 分类总数
def category_count(cgr_id):
    return Article.objects.filter(category=cgr_id).count()

@register.filter
# 归档总数
def monthly_count(date):
    return Article.objects.filter(create_time__year=date.year, create_time__month=date.month).count()

@register.filter
def articles_sort_by_category(cgr_id):
    return Article.objects.filter(category=cgr_id).order_by('-create_time')
