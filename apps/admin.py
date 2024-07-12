from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category, Product



class Category(ModelAdmin):
    list_display = ['id', 'name']


class Products(ModelAdmin):
    list_display = ['id','name']
