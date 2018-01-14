from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage, Category


def prhome(request):
    imageset = ProductImage.objects.all()
    queryset = Product.objects.all()
    context = {
        'object_list': queryset,
        'image_list': imageset,
    }
    return render(request, 'products/allproducts.html', context)


def product(request, id=None):
    instance = get_object_or_404(Product, id=id)
    context = {
       'title': instance.name,
       'instance': instance,
    }
    return render(request, 'products/detail.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_published=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/allproducts.html', {'category': category,
                                                    'categories': categories,
                                                    'products': products})


def product_detail(request, id, slug):
    products = get_object_or_404(Product, id=id, slug=slug, is_published=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/detail.html', {'product': product,
                                                    'cart_product_form': cart_product_form})

