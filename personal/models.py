from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up


STATUS_CHOICES = (
    ('c1', 'Carousel1'),
    ('c2', 'Carousel2'),
    ('c3', 'Carousel3'),
    ('d', 'Draft'),
)


class Carousel(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='d')
    image_url = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/carousel/', null=True, blank=True, width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class profile(models.Model):
    name = models.CharField(max_length=120)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    description = models.TextField(default='description default text')

    def __str__(self):
        return self.name


class userStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username


def my_callback(sender, **kwargs):
    print("request finished")
    print(kwargs)

user_logged_in.connect(my_callback)
