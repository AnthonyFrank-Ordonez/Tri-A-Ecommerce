from django.shortcuts import render

from django.http import HttpResponse
from .models import Category, Vendor, Product, ProductImages, CartOrder,  CartOrderItems, ProductReview, Wishlist, Address


def index(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'core/index.html', context)
