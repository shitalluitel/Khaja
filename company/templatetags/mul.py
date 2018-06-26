from django import template
from django.template.defaultfilters import stringfilter
import decimal
register = template.Library()


@register.filter
@stringfilter
def mul(value, arg):
    return decimal.Decimal(value) * decimal.Decimal(arg)
