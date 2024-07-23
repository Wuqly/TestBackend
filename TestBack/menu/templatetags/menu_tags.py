from django import template
from django.urls import resolve
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/drow_menu.html')
def draw_menu():
    menu = Menu.objects.all()
    return {'menu': menu}
