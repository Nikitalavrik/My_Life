from django import template

register = template.Library()

@register.filter(name="name_edit")
def name_edit(value):
    
    if len(value) > 35:
        value = value[0:32]+"\n" + value[32::]
    return value

