from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def shortDescription(value):
    return (value[:75] + '..') if len(value) > 75 else value
