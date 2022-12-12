from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('products', views.ProductListView.as_view(), name='product_list'),
]
