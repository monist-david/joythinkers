from os.path import splitext

from django import template


register = template.Library()

@register.filter
def noext(value):
    return splitext(value)[0]


@register.filter
def hasNumber(value):
    for char in value:
        if char.isdigit():
            if int(char) == 1:
                return False
    return True
