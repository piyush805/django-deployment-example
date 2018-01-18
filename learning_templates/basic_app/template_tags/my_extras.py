from django import template
#create an object for registering
register = template.Library()

@register.filter(name = 'cut')
def cut(value,arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'')
#registering the filter
#name of the filter when calling, actual filter name

#register.filter('cut',cut)
