from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^man/$', views.man, name='man'),
    url(r'^profile/$', views.userProfile, name='profile'),
]

handler404 = 'views.custom_404'
handler500 = 'views.custom_500'
