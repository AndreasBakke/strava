from django import template
import sys

register = template.Library()

@register.simple_tag(takes_context=True)
def get_item (self, context):
    currentweek = context['current_week']
    return self.get(week= currentweek)


