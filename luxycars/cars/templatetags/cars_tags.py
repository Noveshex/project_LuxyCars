from django import template
from cars.models import *

register = template.Library()


@register.simple_tag()
def get_status():
    return Status.objects.all()