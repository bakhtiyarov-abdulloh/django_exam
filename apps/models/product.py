from django.db import models
from django.db.models import Model, ImageField, CharField, PositiveIntegerField, JSONField, DateTimeField, ForeignKey
from django.views.generic import ListView

class Category:
    name = CharField(max_length=255)


class Product:
    name = CharField(max_length=255)
    description = CharField(max_length=255)

class ProductImage(ImageField,Product):
    pass

