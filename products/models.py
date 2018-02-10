from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db import models
from multiselectfield import MultiSelectField
import  datetime


STATUS_CHOICES = (
    ('m', 'Man'),
    ('w', 'Woman'),
    ('c', 'Child'),
    ('d', 'Draft'),
)

CURRENCY_CHOICES = (
    ('USD', 'DOLLAR'),
    ('EUR', 'EURO'),
    ('TJS', 'SOMONI'),
    ('RUB', 'RUSSIAN RUBLE'),
    ('TRY', 'TURKISH LIRA'),
)


class Category(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    status = MultiSelectField(choices=STATUS_CHOICES)
    description = models.TextField()
    meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])


class Usage(models.Model):
    title = models.CharField(max_length=140)
    status = MultiSelectField(choices=STATUS_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.title


class Brands(models.Model):
    title = models.CharField(max_length=140)
    status = MultiSelectField(choices=STATUS_CHOICES)
    image_url = models.CharField(max_length=500, default='nourl')
    description = models.TextField()
    image = models.ImageField(upload_to='images/brands/', null=True, blank=True, width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    thumb_url = models.CharField(max_length=500, null=True, blank=True)
    thumb = models.FileField(upload_to='images/products/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(blank=True)
    usage_area = models.ForeignKey(Usage, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    old_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0.00)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES, default='TJS')
    in_stock = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sku = models.CharField(max_length=50, blank=True)
    is_bestseller = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag')

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=500, null=True, blank=True)
    image = models.FileField(upload_to='images/products/', null=True, blank=True)


def create_slug(instance, new_slag = None):
    slug = slugify(instance.name)
    if new_slag is not None:
        slug = new_slag
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exist = qs.exists()
    if exist:
        new_slag = '%s-%s' %(slug, qs.first().id)
        return create_slug(instance, new_slag=new_slag)
    return slug


def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_slug, sender=Product)
