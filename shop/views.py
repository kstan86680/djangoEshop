from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shop/product_list.html', context)

def login(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shop/login.html', context)