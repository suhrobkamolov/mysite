from django.contrib import admin
from personal.models import Carousel, profile, userStripe


class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile

admin.site.register(profile, profileAdmin)


class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe

admin.site.register(userStripe, userStripeAdmin)


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_display_links = ['title']
    list_editable = ['status']
    list_filter = ['title']
    search_fields = ['title', 'description']
    actions = [make_published]

    class Meta:
        model = Carousel

admin.site.register(Carousel, PostModelAdmin)
