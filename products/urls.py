from django.contrib import admin
from django.urls import path

from products.views import ProductFormView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('agregar/', ProductFormView.as_view(), name='product_form'),
]
