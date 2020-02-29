from os.path import splitext

from django import template


register = template.Library()

@register.filter
def noext(value):
    return value.split('/')[1][:-6]

@register.filter
def nofront(value):
    return value.split('/')[1]


@register.filter
def hasNumber(value):
    for char in value:
        if char.isdigit():
            if int(char) == 1:
                return True
    return False


print(noext('270300/Audi_R8_1'))