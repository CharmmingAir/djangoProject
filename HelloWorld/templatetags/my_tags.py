from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def my_filter(v1, v2): # 该装饰器的参数最多只能有两个
    return v1 * v2

@register.simple_tag # 利用该装饰器自定义标签
def my_tag1(v1, v2, v3):
    return v1 * v2 * v3

@register.simple_tag
def my_html(v1, v2):
    temp_html = "<input type = 'text' id = '%s' class = '%s' />" %(v1, v2)
    return mark_safe(temp_html)

