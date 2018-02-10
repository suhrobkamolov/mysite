from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Carousel
from products.models import Product, Category


def index(request):
    queryset = Carousel.objects.all()
    categories = Category.objects.all()
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 12)  # Show 3 contacts per page

    page = request.GET.get('page')
    num_pages = paginator.num_pages
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    index = contacts.number - 1
    max_index = len(paginator.page_range)
    start_index = index-5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    context = {
        'object_list': queryset,
        'categories': categories,
        'contacts': contacts, 'page_range': page_range,
    }
    return render(request, 'personal/home.html', context)


def about(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    content = {
        'categories': categories, 'products': products,
        'content': ['If you would like to contact me, please email me', 'mehvarcompany@gmail.com']
    }
    return render(request, 'personal/about.html', content)


def man(request):
    content = {
        'content': ['If you would like to contact me, please email me', 'hskinsley@gmail.com']
    }
    return render(request, 'personal/index.html', content)


def custom404(request):
    return render(request, 'personal/404.html')


def custom500(request):
    return render(request, 'personal/500.html')


@login_required()
def userProfile(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    user = request.user
    context = {'user': user, 'categories': categories, 'products': products, }
    template = 'personal/profile.html'
    return render(request, template, context)
