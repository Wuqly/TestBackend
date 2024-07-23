from .models import MenuItem
from django.shortcuts import render, get_object_or_404

def menu_item(request, slug):
    item = get_object_or_404(MenuItem, slug=slug)
    return render(request, 'menu/item.html', {'item': item})    