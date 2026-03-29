from django.views.generic import ListView
from .models import Product


class SqlDataListView(ListView):
    model = Product
    template_name = 'viewer/product_list.html'
    context_object_name = 'products'
    paginate_by = 20
