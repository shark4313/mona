from django import template
register = template.Library()

@register.filter
def to_integer(str):
    return int(str)