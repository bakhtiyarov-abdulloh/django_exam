from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.views import ProductListView
from root import settings

urlpatterns = [

                  path('', ProductListView.as_view(),name = 'product_list'),
                  path('product-detail/<int:pk>', ProductListView.as_view(),name = 'product_detail')


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
