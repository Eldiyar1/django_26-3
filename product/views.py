from django.shortcuts import get_object_or_404
from .models import Product
from django.views.generic import DetailView, ListView


class ProductListView(ListView):
    # queryset = models.Product.objects.filter().order_by('-id')
    template_name = "products/product_list.html"
    queryset = Product.objects.filter(tag__name="телефон")

    def get_queryset(self):
        return Product.objects.filter(tag__name="телефон")


class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=product_id)
