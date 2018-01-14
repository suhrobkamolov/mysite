from django.contrib import admin
from .models import Category, Brands, Product, Usage, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'in_stock', 'is_published', 'created', 'updated']
    list_filter = ['is_published', 'created', 'updated', 'category']
    list_editable = ['price', 'in_stock', 'is_published']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Brands)
admin.site.register(Product, ProductAdmin)
admin.site.register(Usage)
admin.site.register(ProductImage)
