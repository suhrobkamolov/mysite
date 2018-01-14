from django.shortcuts import render
#from .models import Carousel


def man_home(request):
    #queryset = Carousel.objects.all()
    #context = {
    #    'object_list': queryset,
    #    'active': 'p',
    #}
    return render(request, 'man/man.html')
