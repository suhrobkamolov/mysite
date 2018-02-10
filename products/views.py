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


def product(request, id=None, product_slug=None):
    product = None
    products = Product.objects.all()
    instance = get_object_or_404(Product, id=id)
    context = {
       'title': instance.name,
       'instance': instance,
    }
    return render(request, 'products/detail_view.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_published=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        page_title = category.title
        meta_keywords = category.meta_keywords
        meta_description = category.meta_description
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'products/allproducts.html', context, locals())


def product_detail(request, slug):
    products = get_object_or_404(Product, slug=slug, is_published=True)
    page_title = products.name
    meta_keywords = products.meta_keywords
    meta_description = products.meta_description
    #cart_product_form = CartAddProductForm()
    return render(request, 'products/detail_view.html', {'product': product}, locals())


