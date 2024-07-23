from django.contrib import admin
from .models import Menu, MenuItem

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id','menu', 'name', 'slug', 'parent']
    list_display_links = ['id', 'menu', 'name']