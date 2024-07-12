
from django.shortcuts import render
from django.views.generic import DetailView,ListView

from apps.models import Product, Category


class ProductListView(ListView):
    # queryset = Product.objects.order_by('-created_at')
    template_name = 'apps/product/product_list.html'
    paginate_by = 2
    model = Product
    context_object_name = "products"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'apps/product/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Product.objects.all()
