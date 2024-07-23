from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def get_url(self):
        return reverse('menu_item', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Элементы меню'
        verbose_name_plural = 'Элементы меню'