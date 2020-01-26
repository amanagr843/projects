from django.shortcuts import render
from .models import Products
from .forms import ProductForm, Product_raw
# Create your views here.
def product_create_view(request):
    form = Product_raw()
    if request.method == "POST":
        form = Product_raw(request.POST)
        if form.is_valid():
            Products.objects.create(**form.cleaned_data)
            form = Product_raw()
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "product/create.html",context)

def product_detail_view(request):
    n = len(Products.objects.all())
    name = []
    description = []
    price = []
    obj = Products.objects.all()

    context = {
        "list": obj
    }
    return render(request, "product/detail.html",context)
