from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path("product/", ProductListView.as_view(), name="Product"),
    path("product/<int:id>", ProductDetailView.as_view(), name="ProductDetail"),
]