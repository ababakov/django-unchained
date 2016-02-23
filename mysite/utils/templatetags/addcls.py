from django import template
register = template.Library()

@register.filter(name='addcls')
def addcls(field, cls):
   return field.as_widget(attrs={"class":cls})