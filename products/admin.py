from django.contrib import admin
from .models import Category, Brands, Product, Usage, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at',)
    list_display_links = ('title',)
    list_per_page = 20
    ordering = ['title']
    search_fields = ['title', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'old_price', 'in_stock', 'is_published', 'created', 'updated']
    list_filter = ['is_published', 'created', 'updated', 'category']
    list_editable = ['price', 'in_stock', 'is_published']
    list_per_page = 50
    ordering = ['-created']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Brands)
admin.site.register(Product, ProductAdmin)
admin.site.register(Usage)
admin.site.register(ProductImage)
