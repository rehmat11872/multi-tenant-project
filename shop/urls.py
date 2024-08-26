from django.urls import path
from .views import tenant_product_list

urlpatterns = [
    path('products/', tenant_product_list, name='tenant_product_list'),
]
