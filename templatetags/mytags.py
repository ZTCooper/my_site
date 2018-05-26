import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

# 引入过滤器
register = template.Library()

# 自定义过滤器
@register.filter(is_safe=True)
@stringfilter

def toMarkdown(value):
    # markdown解析器
    return mark_safe(markdown2.markdown(force_text(value), extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler"]))
