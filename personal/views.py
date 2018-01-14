from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Carousel
from products.models import Product


def index(request):
    queryset = Carousel.objects.all()
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 3)  # Show 3 contacts per page

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
        'contacts': contacts, 'page_range': page_range,
    }
    return render(request, 'personal/home.html', context)


def about(request):
    content = {
        'content': ['If you would like to contact me, please email me', 'hskinsley@gmail.com']
    }
    return render(request, 'personal/about.html', content)


@login_required()
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'personal/profile.html'
    return render(request, template, context)
