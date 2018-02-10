from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import contactForm
from products.models import Category, Product


def contact(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    title = 'Feel free to contact us@@'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from Mehvar Co'
        message = '%s %s' % (comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = 'Thanks!!!'
        confirm_message = 'We will contact you soon.'
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message, 'categories': categories, 'products': products, }
    return render(request, 'contact/contact.html', context)
