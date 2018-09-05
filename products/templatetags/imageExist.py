from django import template
from django.template.defaultfilters import stringfilter
from django.core.files.storage import default_storage

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def imageExist(value):
    try:
        returnValue = default_storage.exists(value)
    except:
        returnValue = False
    return returnValue
