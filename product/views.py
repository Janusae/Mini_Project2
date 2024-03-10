from django.shortcuts import render, get_list_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView , FormView
from .form import Form_AddProduct
from .models import Product , Category
# Create your views here.
class ProductView(ListView):
    template_name = "product/product.html"
    model = Product
    context_object_name = "data"
    paginate_by = 3

class Product_DetailView(DetailView):
    template_name = "product/detail.html"
    model = Product
    context_object_name = "data"
class AddForView(FormView):
    template_name = "product/adding.html"
    form_class = Form_AddProduct
    success_url = "register"
    def form_valid(self, form):
        form.save()
        return redirect(reverse("ProductView"))