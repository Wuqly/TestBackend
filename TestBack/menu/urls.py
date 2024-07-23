from django.urls import path
from . import views

urlpatterns = [
    path('menu/<slug:slug>/', views.menu_item, name='menu_item'),
]