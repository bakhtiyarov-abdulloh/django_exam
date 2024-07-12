from datetime import timedelta

from django.db import models
from django.db.models import Model, ImageField, CharField, PositiveIntegerField, JSONField, DateTimeField, ForeignKey, \
    CASCADE, CheckConstraint, Q, IntegerField, TextChoices, EmailField, TextField, DateField
from django.utils.text import slugify
from django.utils.timezone import now
from django_ckeditor_5.fields import CKEditor5Field
from embed_video.fields import EmbedVideoField
from mptt.models import MPTTModel, TreeForeignKey

from root.settings import AUTH_USER_MODEL


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=50),

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255)
    discount = PositiveIntegerField(default=0, null=True, blank=True)
    price = IntegerField()
    description = CKEditor5Field()
    created_at = DateTimeField(auto_now_add=True)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(discount__lte=100),
                name="discount__lte__100",
            )
        ]

    def __str__(self):
        return self.name

    @property
    def current_price(self):
        return int(self.price - self.discount * self.price / 100)

    @property
    def is_new(self):
        return now() - timedelta(days=7) <= self.created_at



class ProductImage(Model):
    image = ImageField(upload_to='products/', null=True)
    product = models.ForeignKey('apps.Product', models.CASCADE, related_name='images')


class Item(models.Model):
    video = EmbedVideoField()
    product = models.ForeignKey('apps.Product',models.CASCADE,related_name='vidio')