from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.man_home, name='prhome'),
    #url(r'^contact/$', views.contact, name='contact'),
]